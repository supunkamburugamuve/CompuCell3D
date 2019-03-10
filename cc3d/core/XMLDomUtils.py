from cc3d.core.XMLUtils import dictionaryToMapStrStr as d2mss

class XMLElemAdapter:
    """
    This class gives easy access to XML attributes
    """
    def __init__(self, reference_elem=None, super_parent=None):

        # reference to the C++ XML element representation

        self.__allowed_assignment_properties = []
        self.__reference_elem = reference_elem

        # usually stores reference to Plugin, Steppable or Potts elements - modules that will have to be initialized
        self.__super_parent = super_parent

        self._dirty_flag = False
        if reference_elem is not None:
            self.init_attributes()

    @property
    def super_parent(self):
        return self.__super_parent

    def init_attributes(self):
        """
        adds new properties to the object base on attributes of the self.__reference_element
        The goal is to give user an object that is easy to manipulate

        :return: None
        """
        if self.__reference_elem is None:
            return

        attributes = self.__reference_elem.getAttributes()

        setattr(self, 'cdata', self.__reference_elem.cdata)
        self.__allowed_assignment_properties.append('cdata')

        for attr_key in attributes.keys():
            setattr(self, attr_key, attributes[attr_key])
            self.__allowed_assignment_properties.append(attr_key)

        # self.__setattr__ = self.__attr_setter
        self.attribs_initialized = True

    def set_dirty(self, flag=True):
        self._dirty_flag = flag


    @property
    def dirty(self):
        return self._dirty_flag

    # def __attr_setter(self, key, value):
    def __setattr__(self, key, value):

        try:
            self.attribs_initialized
            be_selective = True
        except (KeyError,AttributeError):
            be_selective = False
            print('self.attribs_initialized does not exist')

        if not be_selective:
            self.__dict__[key] = value
        else:
            if key == '_dirty_flag':
                self.__dict__['_dirty_flag'] = value
                return
            if key in self.__allowed_assignment_properties:
                self.__dict__[key] = value

                # changing underlying element
                if key == 'cdata':
                    self.__reference_elem.cdata = str(value)
                else:
                    self.__reference_elem.updateElementAttributes(d2mss({key: value}))


                self.__dict__['_dirty_flag'] = True
                # print
            else:
                raise AttributeError('Attribute {attr} is not assignable. '
                                     'The list of assignable attributes is: {attr_list}'.format(
                    attr=key,
                    attr_list=self.__allowed_assignment_properties

                ))

class XMLIdLocator:
    def __init__(self, root_elem):

        self.root_elem = root_elem
        self.node_stack = []
        self.super_parent_stack = []

        # dict labeled by the value of the id element
        self.id_elements_dict = {}

        self._recently_accessed_elems = {}
        # self.recently_modified_elems = {}

    def reset(self):
        self._recently_accessed_elems = {}

    @property
    def recently_accessed_elems(self):
        return self._recently_accessed_elems

    def locate_id_elements(self):
        """

        :return:
        """
        self.walk_and_locate_id_elements(elem=self.root_elem)

    def walk_and_locate_id_elements(self, elem):
        """

        :return:
        """

        id_elem_list = []
        children = elem.children
        self.node_stack.append(elem)

        print('elem=', elem.name)

        if elem.name in ['Potts', 'Plugin', 'Steppable']:
            self.super_parent_stack.append(elem)
            print('adding super_parent=', elem.name)

        # direct iteration like for child_elem in  root_elem.children: does not work with SWIG
        for child_idx in range(children.size()):
            child = children[child_idx]
            attributes = child.getAttributes()
            if 'id' in attributes.keys():
                elem_with_id = XMLElemAdapter(reference_elem=child, super_parent=self.super_parent_stack[-1])
                id_attr = child.getAttribute('id')
                self.id_elements_dict[id_attr] = elem_with_id

            # print(attributes)
            self.walk_and_locate_id_elements(elem=child)

        popped_elem = self.node_stack.pop()
        if popped_elem.name in ['Potts', 'Plugin', 'Steppable']:
            self.super_parent_stack.pop()

    def get_xml_element(self, id):
        try:
            elem = self.id_elements_dict[id]
            self._recently_accessed_elems[id] = elem
            return elem
        except KeyError:
            return None
