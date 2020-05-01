from opencmiss.zinc.context import Context
from opencmiss.zinc.field import Field
from opencmiss.zinc.glyph import Glyph
from opencmiss.zinc.status import OK as ZINC_OK
from opencmiss.zinc.material import Material
from opencmiss.utils.zinc.field import getGroupList
from opencmiss.utils.zinc.general import ChangeManager

from math import sqrt


def magnitude(v):
    return sqrt(sum(v[i] * v[i] for i in range(len(v))))


def sub(u, v):
    return [u[i] - v[i] for i in range(len(u))]


class DataModel(object):

    def __init__(self, ex_data_file):
        self._context = Context('DataTrimmer')
        self._region = self._context.createRegion()
        self._region.setName('TrimRegion')
        self._field_module = self._region.getFieldmodule()
        #  read the EX Zinc data file
        self._coordinate_field = None
        self._groups = None
        self._initialise_ex_data(ex_data_file)
        self._material_module = self._context.getMaterialmodule()
        self._initialise_glyph_material()
        self._initialise_tessellation(12)

        self._initialise_scene()

    def _discover_groups(self):
        with ChangeManager(self._field_module):
            self._groups = [group.getName() for group in getGroupList(self._field_module)]

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

    def _create_rgb_spectrum(self):
        field = self._field_module.findFieldByName('rgb')
        spectrummodule = self._scene.getSpectrummodule()
        spectrum = None
        # dataProjections.setSpectrum(spectrum)
        # dataProjections.setName("displayDataProjections")
        # dataProjections.setVisibilityFlag(self.isDisplayDataProjections())

    def create_graphics(self):
        # self._create_rgb_spectrum()
        points = self._scene.createGraphicsPoints()
        points.setFieldDomainType(Field.DOMAIN_TYPE_NODES)
        points.setCoordinateField(self._coordinate_field)
        point_attr = points.getGraphicspointattributes()
        point_attr.setGlyphShapeType(Glyph.SHAPE_TYPE_POINT)
        point_size = self._get_auto_point_size()
        point_attr.setBaseSize(point_size)
        points.setMaterial(self._material_module.findMaterialByName('silver'))
        points.setName('display_points')

    def get_context(self):
        return self._context

    def get_groups(self):
        return self._groups

    def get_region(self):
        return self._region

    def get_scene(self):
        return self._region.getScene()
