import os
import json

from opencmiss.zinc.context import Context
from opencmiss.zinc.field import Field
from opencmiss.zinc.glyph import Glyph
from opencmiss.zinc.graphics import Graphics
from opencmiss.zinc.material import Material
from opencmiss.zinc.spectrum import Spectrumcomponent
from opencmiss.zinc.status import OK as ZINC_OK
from opencmiss.utils.zinc.general import ChangeManager

from math import sqrt


def magnitude(v):
    return sqrt(sum(v[i] * v[i] for i in range(len(v))))


def sub(u, v):
    return [u[i] - v[i] for i in range(len(u))]


class DataModel(object):

    def __init__(self, ex_data_file, location):
        self._context = Context('DataTrimmer')
        self._region = self._context.createRegion()
        self._region.setName('TrimRegion')
        self._field_module = self._region.getFieldmodule()
        self._ex_filename = ex_data_file
        self._location = location
        self._output_filename = None
        self._coordinate_field = None
        self._mesh = None
        self._groups = None
        self._group_fields = None
        self._group_dct = None
        self._settings = {}
        #  read the EX Zinc data file
        self._initialise_ex_data(ex_data_file)
        self._load_settings()
        self._material_module = self._context.getMaterialmodule()
        self._initialise_glyph_material()
        self._init_graphics_module()
        self._initialise_tessellation(12)
        self._scene_change_callback = None

        self._initialise_scene()

    def _load_settings(self):
        try:
            with open(self._get_settings_filename(), "r") as f:
                saved_settings = json.loads(f.read())
                self._settings.update(saved_settings)
        except:
            pass

    def _save_settings(self):
        with open(self._get_settings_filename(), "w") as f:
            f.write(json.dumps(self._settings, sort_keys=False, indent=4))

    def _get_settings_filename(self):
        return self._location + "-display-settings.json"

    def _discover_groups(self):
        with ChangeManager(self._field_module):
            self._group_fields, self._groups = self._get_group_fields()
        for group in self._groups:
            self._settings[group.getName()] = True

    def _get_group_fields(self):
        group_fields = []
        groups = []
        field_iter = self._field_module.createFielditerator()
        field = field_iter.next()
        while field.isValid():
            group = field.castGroup()
            if group.isValid():
                group_fields.append(field)
                groups.append(group)
            field = field_iter.next()
        return group_fields, groups

    def _get_data_coordinate_field(self):
        node_point_set = self._field_module.findNodesetByFieldDomainType(Field.DOMAIN_TYPE_NODES)
        node_points = node_point_set.createNodeiterator().next()
        if not node_points.isValid():
            raise ValueError('Empty data!')
        cache = self._field_module.createFieldcache()
        cache.setNode(node_points)
        field_iter = self._field_module.createFielditerator()
        field = field_iter.next()
        while field.isValid():
            if field.isTypeCoordinate() and (field.getNumberOfComponents() <= 3):
                if field.isDefinedAtLocation(cache):
                    return field
            field = field_iter.next()
        raise ValueError('Could not determine the coordinate field')

    def _get_highest_dimension_mesh(self):
        mesh = [self._field_module.findMeshByDimension(d + 1) for d in range(3)]
        for d in range(2, -1, -1):
            m = mesh[d]
            if m.getSize() > 0:
                self._mesh = m
                return

    def _get_auto_point_size(self):
        minimums, maximums = self._get_data_range()
        data_size = magnitude(sub(maximums, minimums))
        return 0.25 * data_size

    def _get_data_range(self):
        data_points = self._field_module.findNodesetByFieldDomainType(Field.DOMAIN_TYPE_NODES)
        minimums, maximums = self._get_nodeset_minimum_maximum(data_points, self._coordinate_field)
        return minimums, maximums

    def _get_nodeset_minimum_maximum(self, nodeset, field):
        count = field.getNumberOfComponents()
        minimums_field = self._field_module.createFieldNodesetMinimum(field, nodeset)
        maximums_field = self._field_module.createFieldNodesetMaximum(field, nodeset)
        cache = self._field_module.createFieldcache()
        result, minimums = minimums_field.evaluateReal(cache, count)
        if result != ZINC_OK:
            minimums = None
        result, maximums = maximums_field.evaluateReal(cache, count)
        if result != ZINC_OK:
            maximums = None
        del minimums_field
        del maximums_field
        return minimums, maximums

    def _initialise_glyph_material(self):
        self._glyph_module = self._context.getGlyphmodule()
        self._glyph_module.defineStandardGlyphs()

    def _initialise_tessellation(self, res):
        self._tessellationmodule = self._context.getTessellationmodule()
        self._tessellationmodule = self._tessellationmodule.getDefaultTessellation()
        self._tessellationmodule.setRefinementFactors([res])

    def _init_graphics_module(self):
        with ChangeManager(self._material_module):
            self._material_module.defineStandardMaterials()
            trans_blue = self._material_module.createMaterial()
            trans_blue.setName("trans_blue")
            trans_blue.setManaged(True)
            trans_blue.setAttributeReal3(Material.ATTRIBUTE_AMBIENT, [0.0, 0.2, 0.6])
            trans_blue.setAttributeReal3(Material.ATTRIBUTE_DIFFUSE, [0.0, 0.7, 1.0])
            trans_blue.setAttributeReal3(Material.ATTRIBUTE_EMISSION, [0.0, 0.0, 0.0])
            trans_blue.setAttributeReal3(Material.ATTRIBUTE_SPECULAR, [0.1, 0.1, 0.1])
            trans_blue.setAttributeReal(Material.ATTRIBUTE_ALPHA, 0.3)
            trans_blue.setAttributeReal(Material.ATTRIBUTE_SHININESS, 0.2)

    def _initialise_scene(self):
        self._scene = self._region.getScene()

    def _initialise_ex_data(self, data_file):
        sir = self._region.createStreaminformationRegion()
        data_resource = sir.createStreamresourceFile(data_file)
        sir.setResourceDomainTypes(data_resource, Field.DOMAIN_TYPE_NODES)
        result = self._region.read(sir)
        if result != ZINC_OK:
            raise ValueError('Failed to initiate EX data.')
        self._coordinate_field = self._get_data_coordinate_field()
        self._discover_groups()
        self._get_highest_dimension_mesh()

    def _create_rgb_spectrum(self):
        spectrum_module = self._scene.getSpectrummodule()
        self._rgb_spectrum = spectrum_module.findSpectrumByName("rgb")
        if not self._rgb_spectrum.isValid():
            with ChangeManager(spectrum_module):
                self._rgb_spectrum = spectrum_module.createSpectrum()
                self._rgb_spectrum.setName("rgb")
                self._rgb_spectrum.setMaterialOverwrite(True)
                colour_mapping_types = (Spectrumcomponent.COLOUR_MAPPING_TYPE_RED,
                                        Spectrumcomponent.COLOUR_MAPPING_TYPE_GREEN,
                                        Spectrumcomponent.COLOUR_MAPPING_TYPE_BLUE)
                for c in range(3):
                    spectrum_component = self._rgb_spectrum.createSpectrumcomponent()
                    spectrum_component.setFieldComponent(c + 1)
                    spectrum_component.setColourMappingType(colour_mapping_types[c])
                    spectrum_component.setColourMinimum(0.0)
                    spectrum_component.setColourMaximum(1.0)
                    spectrum_component.setRangeMinimum(0.0)
                    spectrum_component.setRangeMaximum(1.0)

    def create_graphics(self, groups: []):
        self._create_rgb_spectrum()
        for group in groups:
            if group in self._group_dct.keys():
                group_field = self._group_dct[group]
                points = self._scene.createGraphicsPoints()
                points.setSubgroupField(group_field)
                points.setFieldDomainType(Field.DOMAIN_TYPE_NODES)
                points.setCoordinateField(self._coordinate_field)
                points.setDataField(self._field_module.findFieldByName('rgb'))
                point_attr = points.getGraphicspointattributes()
                point_attr.setGlyphShapeType(Glyph.SHAPE_TYPE_POINT)
                point_size = self._get_auto_point_size()
                point_attr.setBaseSize(point_size)
                points.setSpectrum(self._rgb_spectrum)
                points.setName(str(group) + '_points')
                if group in self._settings.keys():
                    if self._settings[group]:
                        points.setVisibilityFlag(True)
                    else:
                        points.setVisibilityFlag(False)
                if self._mesh.getDimension() > 1:
                    lines = self._scene.createGraphicsLines()
                    lines.setCoordinateField(self._coordinate_field)
                    lines.setExterior(True)
                    lines.setName(str(group) + '_lines')
                    lines.setVisibilityFlag(True)
                    surfaces = self._scene.createGraphicsSurfaces()
                    surfaces.setCoordinateField(self._coordinate_field)
                    surfaces.setRenderPolygonMode(Graphics.RENDER_POLYGON_MODE_SHADED)
                    surfaces.setExterior(True if (self._mesh.getDimension() == 3) else False)
                    surfaces_material = self._material_module.findMaterialByName('trans_blue')
                    surfaces.setMaterial(surfaces_material)
                    surfaces.setName(str(group) + '_surfaces')
                    surfaces.setVisibilityFlag(True)

    def destroy_groups(self, groups: []):
        if groups is None:
            return
        mesh1d = self._field_module.findMeshByDimension(1)
        nodeset = self._field_module.findNodesetByFieldDomainType(Field.DOMAIN_TYPE_NODES)
        with ChangeManager(self._field_module):
            for group in groups:
                if group in self._group_dct.keys():
                    # print("Deleting dimension {0} for group {1}".format(dimension, group))
                    mesh1d.destroyElementsConditional(self._group_dct[group])
                    nodeset.destroyNodesConditional(self._group_dct[group])
                    self._group_dct[group].setManaged(False)
                    del self._group_dct[group]

    def done(self):
        self._save_settings()

    def get_context(self):
        return self._context

    def get_group_names(self):
        group_names = [group.getName() for group in self._groups]
        self._group_dct = dict(zip(group_names, self._groups))
        return group_names

    def get_output_filename(self):
        return self._output_filename

    def get_region(self):
        return self._region

    def get_scene(self):
        return self._region.getScene()

    def get_settings(self):
        return self._settings

    def register_scene_change_callback(self, scene_change_callback):
        self._scene_change_callback = scene_change_callback

    def remove_graphics(self, groups):
        with ChangeManager(self._scene):
            for group in groups:
                self._settings[group] = False
                points = self._scene.findGraphicsByName(str(group) + '_points')
                points.setVisibilityFlag(False)
                if self._mesh.getDimension() > 1:
                    lines = self._scene.findGraphicsByName(str(group) + '_lines')
                    lines.setVisibilityFlag(False)
                    surfaces = self._scene.findGraphicsByName(str(group) + '_surfaces')
                    surfaces.setVisibilityFlag(False)

    def show_graphics(self, groups):
        with ChangeManager(self._scene):
            for group in groups:
                self._settings[group] = True
                points = self._scene.findGraphicsByName(str(group) + '_points')
                points.setVisibilityFlag(True)
                if self._mesh.getDimension() > 1:
                    lines = self._scene.findGraphicsByName(str(group) + '_lines')
                    lines.setVisibilityFlag(True)
                    surfaces = self._scene.findGraphicsByName(str(group) + '_surfaces')
                    surfaces.setVisibilityFlag(True)

    def write_model(self):
        filename = os.path.basename(self._ex_filename).split('.')[0] + '-trimmed.ex'
        self._output_filename = os.path.join(self._location, filename)
        self._region.writeFile(self._output_filename)
