# ./_cpe_lang.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:5caf83f456b01aed7af2bffd4d1b8437e0c7ff59
# Generated 2014-10-24 20:20:21.299149 by PyXB version 1.2.4 using Python 3.4.1.final.0
# Namespace http://cpe.mitre.org/language/2.0 [xmlns:cpe_lang]

from __future__ import unicode_literals
import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys
import pyxb.utils.six as _six

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:6a0e222e-5baa-11e4-9adb-e4ce8f358f7e')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.4'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes
import pyxb.binding.xml_

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://cpe.mitre.org/language/2.0', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword default_namespace The L{pyxb.Namespace} instance to use as the
    default namespace where there is no default namespace in scope.
    If unspecified or C{None}, the namespace of the module containing
    this function will be used.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement, default_namespace=default_namespace)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, _six.text_type):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)


# Atomic simple type: {http://cpe.mitre.org/language/2.0}operatorEnumeration
class operatorEnumeration (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """The OperatorEnumeration simple type defines acceptable operators. Each operator defines how to evaluate multiple arguments."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'operatorEnumeration')
    _XSDLocation = pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/cpe-language_2.1.xsd', 68, 6)
    _Documentation = 'The OperatorEnumeration simple type defines acceptable operators. Each operator defines how to evaluate multiple arguments.'
operatorEnumeration._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=operatorEnumeration)
operatorEnumeration.AND = operatorEnumeration._CF_enumeration.addEnumeration(unicode_value='AND', tag='AND')
operatorEnumeration.OR = operatorEnumeration._CF_enumeration.addEnumeration(unicode_value='OR', tag='OR')
operatorEnumeration._InitializeFacetMap(operatorEnumeration._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'operatorEnumeration', operatorEnumeration)

# Atomic simple type: {http://cpe.mitre.org/language/2.0}namePattern
class namePattern (pyxb.binding.datatypes.anyURI):

    """Define the format for acceptable CPE Names. A URN format is used with the id starting with the word cpe followed by :/ and then some number of individual  components separated by colons."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'namePattern')
    _XSDLocation = pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/cpe-language_2.1.xsd', 93, 6)
    _Documentation = 'Define the format for acceptable CPE Names. A URN format is used with the id starting with the word cpe followed by :/ and then some number of individual  components separated by colons.'
namePattern._CF_pattern = pyxb.binding.facets.CF_pattern()
namePattern._CF_pattern.addPattern(pattern='[c][pP][eE]:/[AHOaho]?(:[A-Za-z0-9\\._\\-~%]*){0,6}')
namePattern._InitializeFacetMap(namePattern._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'namePattern', namePattern)

# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """This element is the root element of a CPE Language XML documents and therefore acts as a container for child platform definitions."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/cpe-language_2.1.xsd', 20, 12)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://cpe.mitre.org/language/2.0}platform uses Python identifier platform
    __platform = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'platform'), 'platform', '__httpcpe_mitre_orglanguage2_0_CTD_ANON_httpcpe_mitre_orglanguage2_0platform', True, pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/cpe-language_2.1.xsd', 22, 24), )

    
    platform = property(__platform.value, __platform.set, None, None)

    _ElementMap.update({
        __platform.name() : __platform
    })
    _AttributeMap.update({
        
    })



# Complex type {http://cpe.mitre.org/language/2.0}PlatformType with content type ELEMENT_ONLY
class PlatformType (pyxb.binding.basis.complexTypeDefinition):
    """The platform element represents the description or qualifications of a particular IT platform type. The platform is defined by the logical-test child element. The id attribute holds a locally unique name for the platform. There is no defined format for this id, it just has to be unique to the containing language document.The optional title element may appear as a child to a platform element. It provides a human-readable title for it. To support uses intended for multiple languages, this element supports the ‘xml:lang’ attribute. At most one title element can appear for each language.The optional remark element may appear as a child of a platform element. It provides some additional description. Zero or more remark elements may appear. To support uses intended for multiple languages, this element supports the ‘xml:lang’ attribute. There can be multiple remarks for a single language."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PlatformType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/cpe-language_2.1.xsd', 35, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://cpe.mitre.org/language/2.0}title uses Python identifier title
    __title = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'title'), 'title', '__httpcpe_mitre_orglanguage2_0_PlatformType_httpcpe_mitre_orglanguage2_0title', True, pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/cpe-language_2.1.xsd', 42, 18), )

    
    title = property(__title.value, __title.set, None, None)

    
    # Element {http://cpe.mitre.org/language/2.0}remark uses Python identifier remark
    __remark = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'remark'), 'remark', '__httpcpe_mitre_orglanguage2_0_PlatformType_httpcpe_mitre_orglanguage2_0remark', True, pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/cpe-language_2.1.xsd', 43, 18), )

    
    remark = property(__remark.value, __remark.set, None, None)

    
    # Element {http://cpe.mitre.org/language/2.0}logical-test uses Python identifier logical_test
    __logical_test = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'logical-test'), 'logical_test', '__httpcpe_mitre_orglanguage2_0_PlatformType_httpcpe_mitre_orglanguage2_0logical_test', False, pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/cpe-language_2.1.xsd', 44, 18), )

    
    logical_test = property(__logical_test.value, __logical_test.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__httpcpe_mitre_orglanguage2_0_PlatformType_id', pyxb.binding.datatypes.anyURI, required=True)
    __id._DeclarationLocation = pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/cpe-language_2.1.xsd', 46, 12)
    __id._UseLocation = pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/cpe-language_2.1.xsd', 46, 12)
    
    id = property(__id.value, __id.set, None, None)

    _ElementMap.update({
        __title.name() : __title,
        __remark.name() : __remark,
        __logical_test.name() : __logical_test
    })
    _AttributeMap.update({
        __id.name() : __id
    })
Namespace.addCategoryObject('typeBinding', 'PlatformType', PlatformType)


# Complex type {http://cpe.mitre.org/language/2.0}TextType with content type SIMPLE
class TextType (pyxb.binding.basis.complexTypeDefinition):
    """This type allows the xml:lang attribute to associate a specific language with an element's string content."""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TextType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/cpe-language_2.1.xsd', 80, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute {http://www.w3.org/XML/1998/namespace}lang uses Python identifier lang
    __lang = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'lang'), 'lang', '__httpcpe_mitre_orglanguage2_0_TextType_httpwww_w3_orgXML1998namespacelang', pyxb.binding.xml_.STD_ANON_lang)
    __lang._DeclarationLocation = None
    __lang._UseLocation = pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/cpe-language_2.1.xsd', 86, 24)
    
    lang = property(__lang.value, __lang.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __lang.name() : __lang
    })
Namespace.addCategoryObject('typeBinding', 'TextType', TextType)


# Complex type {http://cpe.mitre.org/language/2.0}LogicalTestType with content type ELEMENT_ONLY
class LogicalTestType (pyxb.binding.basis.complexTypeDefinition):
    """The logical-test element appears as a child of a platform element, and may also be nested to create more complex logical tests. The content consists of one or more elements: fact-ref, and logical-test children are permitted. The operator to be applied, and optional negation of the test, are given as attributes."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LogicalTestType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/cpe-language_2.1.xsd', 48, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://cpe.mitre.org/language/2.0}logical-test uses Python identifier logical_test
    __logical_test = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'logical-test'), 'logical_test', '__httpcpe_mitre_orglanguage2_0_LogicalTestType_httpcpe_mitre_orglanguage2_0logical_test', True, pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/cpe-language_2.1.xsd', 53, 18), )

    
    logical_test = property(__logical_test.value, __logical_test.set, None, None)

    
    # Element {http://cpe.mitre.org/language/2.0}fact-ref uses Python identifier fact_ref
    __fact_ref = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'fact-ref'), 'fact_ref', '__httpcpe_mitre_orglanguage2_0_LogicalTestType_httpcpe_mitre_orglanguage2_0fact_ref', True, pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/cpe-language_2.1.xsd', 54, 18), )

    
    fact_ref = property(__fact_ref.value, __fact_ref.set, None, None)

    
    # Attribute operator uses Python identifier operator
    __operator = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'operator'), 'operator', '__httpcpe_mitre_orglanguage2_0_LogicalTestType_operator', operatorEnumeration, required=True)
    __operator._DeclarationLocation = pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/cpe-language_2.1.xsd', 56, 12)
    __operator._UseLocation = pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/cpe-language_2.1.xsd', 56, 12)
    
    operator = property(__operator.value, __operator.set, None, None)

    
    # Attribute negate uses Python identifier negate
    __negate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'negate'), 'negate', '__httpcpe_mitre_orglanguage2_0_LogicalTestType_negate', pyxb.binding.datatypes.boolean, required=True)
    __negate._DeclarationLocation = pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/cpe-language_2.1.xsd', 57, 12)
    __negate._UseLocation = pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/cpe-language_2.1.xsd', 57, 12)
    
    negate = property(__negate.value, __negate.set, None, None)

    _ElementMap.update({
        __logical_test.name() : __logical_test,
        __fact_ref.name() : __fact_ref
    })
    _AttributeMap.update({
        __operator.name() : __operator,
        __negate.name() : __negate
    })
Namespace.addCategoryObject('typeBinding', 'LogicalTestType', LogicalTestType)


# Complex type {http://cpe.mitre.org/language/2.0}FactRefType with content type EMPTY
class FactRefType (pyxb.binding.basis.complexTypeDefinition):
    """The fact-ref element appears as a child of a logical-test element. It is simply a reference to a CPE Name that always evaluates to a Boolean result."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'FactRefType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/cpe-language_2.1.xsd', 59, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__httpcpe_mitre_orglanguage2_0_FactRefType_name', namePattern, required=True)
    __name._DeclarationLocation = pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/cpe-language_2.1.xsd', 63, 12)
    __name._UseLocation = pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/cpe-language_2.1.xsd', 63, 12)
    
    name = property(__name.value, __name.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __name.name() : __name
    })
Namespace.addCategoryObject('typeBinding', 'FactRefType', FactRefType)


platform_specification = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'platform-specification'), CTD_ANON, documentation='This element is the root element of a CPE Language XML documents and therefore acts as a container for child platform definitions.', location=pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/cpe-language_2.1.xsd', 16, 6))
Namespace.addCategoryObject('elementBinding', platform_specification.name().localName(), platform_specification)

logical_test = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'logical-test'), LogicalTestType, location=pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/cpe-language_2.1.xsd', 30, 6))
Namespace.addCategoryObject('elementBinding', logical_test.name().localName(), logical_test)



CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'platform'), PlatformType, scope=CTD_ANON, location=pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/cpe-language_2.1.xsd', 22, 24)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'platform')), pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/cpe-language_2.1.xsd', 22, 24))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton()




PlatformType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'title'), TextType, scope=PlatformType, location=pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/cpe-language_2.1.xsd', 42, 18)))

PlatformType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'remark'), TextType, scope=PlatformType, location=pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/cpe-language_2.1.xsd', 43, 18)))

PlatformType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'logical-test'), LogicalTestType, scope=PlatformType, location=pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/cpe-language_2.1.xsd', 44, 18)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/cpe-language_2.1.xsd', 42, 18))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/cpe-language_2.1.xsd', 43, 18))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(PlatformType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'title')), pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/cpe-language_2.1.xsd', 42, 18))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(PlatformType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'remark')), pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/cpe-language_2.1.xsd', 43, 18))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(PlatformType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'logical-test')), pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/cpe-language_2.1.xsd', 44, 18))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
PlatformType._Automaton = _BuildAutomaton_()




LogicalTestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'logical-test'), LogicalTestType, scope=LogicalTestType, location=pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/cpe-language_2.1.xsd', 53, 18)))

LogicalTestType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'fact-ref'), FactRefType, scope=LogicalTestType, location=pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/cpe-language_2.1.xsd', 54, 18)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/cpe-language_2.1.xsd', 53, 18))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/cpe-language_2.1.xsd', 54, 18))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(LogicalTestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'logical-test')), pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/cpe-language_2.1.xsd', 53, 18))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(LogicalTestType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'fact-ref')), pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/cpe-language_2.1.xsd', 54, 18))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
LogicalTestType._Automaton = _BuildAutomaton_2()

