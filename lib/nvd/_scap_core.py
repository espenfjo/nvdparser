# ./_scap_core.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:3bfcb53e9961e20955101335b4ddf3943f6ea4d1
# Generated 2014-10-24 20:20:21.299538 by PyXB version 1.2.4 using Python 3.4.1.final.0
# Namespace http://scap.nist.gov/schema/scap_core/0.1 [xmlns:scap_core]

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
Namespace = pyxb.namespace.NamespaceForURI('http://scap.nist.gov/schema/scap_core/0.1', create_if_missing=True)
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


# Atomic simple type: {http://scap.nist.gov/schema/scap_core/0.1}cpeNamePatternType
class cpeNamePatternType (pyxb.binding.datatypes.anyURI):

    """Define the format for acceptable CPE Names. An urn format is used with the id starting with the word oval followed by a unique string, followed by the three letter code 'def', and ending with an integer."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'cpeNamePatternType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/scap_core_0.1.xsd', 95, 6)
    _Documentation = "Define the format for acceptable CPE Names. An urn format is used with the id starting with the word oval followed by a unique string, followed by the three letter code 'def', and ending with an integer."
cpeNamePatternType._CF_pattern = pyxb.binding.facets.CF_pattern()
cpeNamePatternType._CF_pattern.addPattern(pattern='[c][pP][eE]:/[AHOaho]?(:[A-Za-z0-9\\\\._\\\\-~]*){0,6}')
cpeNamePatternType._InitializeFacetMap(cpeNamePatternType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'cpeNamePatternType', cpeNamePatternType)

# Atomic simple type: {http://scap.nist.gov/schema/scap_core/0.1}cpeSearchableNamePatternType
class cpeSearchableNamePatternType (pyxb.binding.datatypes.anyURI):

    """Define the format for acceptable
                        searchableCPE Names.  The URI escaped code '%25' may be used
                        to represent the character '%' which will be interpreted as a
                        wildcard."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'cpeSearchableNamePatternType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/scap_core_0.1.xsd', 104, 6)
    _Documentation = "Define the format for acceptable\n                        searchableCPE Names.  The URI escaped code '%25' may be used\n                        to represent the character '%' which will be interpreted as a\n                        wildcard."
cpeSearchableNamePatternType._CF_pattern = pyxb.binding.facets.CF_pattern()
cpeSearchableNamePatternType._CF_pattern.addPattern(pattern='[c][pP][eE]:/[AHOaho]?(:[A-Za-z0-9\\\\._\\\\-~*]*){0,6}')
cpeSearchableNamePatternType._InitializeFacetMap(cpeSearchableNamePatternType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'cpeSearchableNamePatternType', cpeSearchableNamePatternType)

# Atomic simple type: {http://scap.nist.gov/schema/scap_core/0.1}cpeComponentPatternType
class cpeComponentPatternType (pyxb.binding.datatypes.token):

    """The name pattern of a CPE component."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'cpeComponentPatternType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/scap_core_0.1.xsd', 116, 6)
    _Documentation = 'The name pattern of a CPE component.'
cpeComponentPatternType._CF_pattern = pyxb.binding.facets.CF_pattern()
cpeComponentPatternType._CF_pattern.addPattern(pattern='[A-Za-z0-9\\._\\-~]*')
cpeComponentPatternType._InitializeFacetMap(cpeComponentPatternType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'cpeComponentPatternType', cpeComponentPatternType)

# Atomic simple type: {http://scap.nist.gov/schema/scap_core/0.1}cweNamePatternType
class cweNamePatternType (pyxb.binding.datatypes.token):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'cweNamePatternType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/scap_core_0.1.xsd', 134, 6)
    _Documentation = None
cweNamePatternType._CF_pattern = pyxb.binding.facets.CF_pattern()
cweNamePatternType._CF_pattern.addPattern(pattern='CWE-[1-9]\\d{0,5}')
cweNamePatternType._InitializeFacetMap(cweNamePatternType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'cweNamePatternType', cweNamePatternType)

# Atomic simple type: {http://scap.nist.gov/schema/scap_core/0.1}cpePartComponentPatternType
class cpePartComponentPatternType (cpeComponentPatternType):

    """The name pattern of the CPE part component."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'cpePartComponentPatternType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/scap_core_0.1.xsd', 125, 6)
    _Documentation = 'The name pattern of the CPE part component.'
cpePartComponentPatternType._CF_pattern = pyxb.binding.facets.CF_pattern()
cpePartComponentPatternType._CF_pattern.addPattern(pattern='[hoaHOA]')
cpePartComponentPatternType._InitializeFacetMap(cpePartComponentPatternType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'cpePartComponentPatternType', cpePartComponentPatternType)

# Complex type {http://scap.nist.gov/schema/scap_core/0.1}checkReferenceType with content type EMPTY
class checkReferenceType (pyxb.binding.basis.complexTypeDefinition):
    """Data type for the check element, a checking system specification URI, string content, and an optional external file reference. The checking system specification should be the URI for a particular version of OVAL or a related system testing language, and the content will be an identifier of a test written in that language. The external file reference could be used to point to the file in which the content test identifier is defined."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'checkReferenceType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/scap_core_0.1.xsd', 20, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute system uses Python identifier system
    __system = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'system'), 'system', '__httpscap_nist_govschemascap_core0_1_checkReferenceType_system', pyxb.binding.datatypes.anyURI, required=True)
    __system._DeclarationLocation = pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/scap_core_0.1.xsd', 24, 12)
    __system._UseLocation = pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/scap_core_0.1.xsd', 24, 12)
    
    system = property(__system.value, __system.set, None, None)

    
    # Attribute href uses Python identifier href
    __href = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'href'), 'href', '__httpscap_nist_govschemascap_core0_1_checkReferenceType_href', pyxb.binding.datatypes.anyURI, required=True)
    __href._DeclarationLocation = pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/scap_core_0.1.xsd', 25, 12)
    __href._UseLocation = pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/scap_core_0.1.xsd', 25, 12)
    
    href = property(__href.value, __href.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__httpscap_nist_govschemascap_core0_1_checkReferenceType_name', pyxb.binding.datatypes.token)
    __name._DeclarationLocation = pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/scap_core_0.1.xsd', 26, 12)
    __name._UseLocation = pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/scap_core_0.1.xsd', 26, 12)
    
    name = property(__name.value, __name.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __system.name() : __system,
        __href.name() : __href,
        __name.name() : __name
    })
Namespace.addCategoryObject('typeBinding', 'checkReferenceType', checkReferenceType)


# Complex type {http://scap.nist.gov/schema/scap_core/0.1}checkSearchType with content type EMPTY
class checkSearchType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://scap.nist.gov/schema/scap_core/0.1}checkSearchType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'checkSearchType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/scap_core_0.1.xsd', 29, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute system uses Python identifier system
    __system = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'system'), 'system', '__httpscap_nist_govschemascap_core0_1_checkSearchType_system', pyxb.binding.datatypes.anyURI, required=True)
    __system._DeclarationLocation = pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/scap_core_0.1.xsd', 30, 12)
    __system._UseLocation = pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/scap_core_0.1.xsd', 30, 12)
    
    system = property(__system.value, __system.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__httpscap_nist_govschemascap_core0_1_checkSearchType_name', pyxb.binding.datatypes.token)
    __name._DeclarationLocation = pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/scap_core_0.1.xsd', 31, 12)
    __name._UseLocation = pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/scap_core_0.1.xsd', 31, 12)
    
    name = property(__name.value, __name.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __system.name() : __system,
        __name.name() : __name
    })
Namespace.addCategoryObject('typeBinding', 'checkSearchType', checkSearchType)


# Complex type {http://scap.nist.gov/schema/scap_core/0.1}notesType with content type ELEMENT_ONLY
class notesType (pyxb.binding.basis.complexTypeDefinition):
    """The notesType defines an element that consists of one or more child note elements. It is assumed that each of these note elements are representative of the same language as defined by their parent."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'notesType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/scap_core_0.1.xsd', 37, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://scap.nist.gov/schema/scap_core/0.1}note uses Python identifier note
    __note = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'note'), 'note', '__httpscap_nist_govschemascap_core0_1_notesType_httpscap_nist_govschemascap_core0_1note', True, pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/scap_core_0.1.xsd', 42, 18), )

    
    note = property(__note.value, __note.set, None, None)

    _ElementMap.update({
        __note.name() : __note
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'notesType', notesType)


# Complex type {http://scap.nist.gov/schema/scap_core/0.1}tagType with content type EMPTY
class tagType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://scap.nist.gov/schema/scap_core/0.1}tagType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tagType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/scap_core_0.1.xsd', 61, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__httpscap_nist_govschemascap_core0_1_tagType_name', pyxb.binding.datatypes.token, required=True)
    __name._DeclarationLocation = pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/scap_core_0.1.xsd', 62, 12)
    __name._UseLocation = pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/scap_core_0.1.xsd', 62, 12)
    
    name = property(__name.value, __name.set, None, None)

    
    # Attribute value uses Python identifier value_
    __value = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'value'), 'value_', '__httpscap_nist_govschemascap_core0_1_tagType_value', pyxb.binding.datatypes.token, required=True)
    __value._DeclarationLocation = pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/scap_core_0.1.xsd', 63, 12)
    __value._UseLocation = pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/scap_core_0.1.xsd', 63, 12)
    
    value_ = property(__value.value, __value.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __name.name() : __name,
        __value.name() : __value
    })
Namespace.addCategoryObject('typeBinding', 'tagType', tagType)


# Complex type {http://scap.nist.gov/schema/scap_core/0.1}textType with content type SIMPLE
class textType (pyxb.binding.basis.complexTypeDefinition):
    """This type allows the xml:lang attribute to associate a specific language with an element's string content."""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'textType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/scap_core_0.1.xsd', 68, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute {http://www.w3.org/XML/1998/namespace}lang uses Python identifier lang
    __lang = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'lang'), 'lang', '__httpscap_nist_govschemascap_core0_1_textType_httpwww_w3_orgXML1998namespacelang', pyxb.binding.xml_.STD_ANON_lang)
    __lang._DeclarationLocation = None
    __lang._UseLocation = pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/scap_core_0.1.xsd', 74, 24)
    
    lang = property(__lang.value, __lang.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __lang.name() : __lang
    })
Namespace.addCategoryObject('typeBinding', 'textType', textType)


# Complex type {http://scap.nist.gov/schema/scap_core/0.1}searchableCpeReferencesType with content type ELEMENT_ONLY
class searchableCpeReferencesType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://scap.nist.gov/schema/scap_core/0.1}searchableCpeReferencesType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'searchableCpeReferencesType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/scap_core_0.1.xsd', 86, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://scap.nist.gov/schema/scap_core/0.1}cpe-name uses Python identifier cpe_name
    __cpe_name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'cpe-name'), 'cpe_name', '__httpscap_nist_govschemascap_core0_1_searchableCpeReferencesType_httpscap_nist_govschemascap_core0_1cpe_name', True, pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/scap_core_0.1.xsd', 81, 18), )

    
    cpe_name = property(__cpe_name.value, __cpe_name.set, None, None)

    
    # Element {http://scap.nist.gov/schema/scap_core/0.1}cpe-searchable-name uses Python identifier cpe_searchable_name
    __cpe_searchable_name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'cpe-searchable-name'), 'cpe_searchable_name', '__httpscap_nist_govschemascap_core0_1_searchableCpeReferencesType_httpscap_nist_govschemascap_core0_1cpe_searchable_name', True, pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/scap_core_0.1.xsd', 82, 18), )

    
    cpe_searchable_name = property(__cpe_searchable_name.value, __cpe_searchable_name.set, None, None)

    _ElementMap.update({
        __cpe_name.name() : __cpe_name,
        __cpe_searchable_name.name() : __cpe_searchable_name
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'searchableCpeReferencesType', searchableCpeReferencesType)


# Complex type {http://scap.nist.gov/schema/scap_core/0.1}referenceType with content type SIMPLE
class referenceType (textType):
    """Type for a reference in the description of a CPE item. This would normally be used to point to extra descriptive material, or the supplier's web site, or the platform documentation. It consists of a piece of text (intended to be human-readable) and a URI (intended to be a URL, and point to a real resource)."""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'referenceType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/scap_core_0.1.xsd', 48, 6)
    _ElementMap = textType._ElementMap.copy()
    _AttributeMap = textType._AttributeMap.copy()
    # Base type is textType
    
    # Attribute lang inherited from {http://scap.nist.gov/schema/scap_core/0.1}textType
    
    # Attribute href uses Python identifier href
    __href = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'href'), 'href', '__httpscap_nist_govschemascap_core0_1_referenceType_href', pyxb.binding.datatypes.anyURI)
    __href._DeclarationLocation = pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/scap_core_0.1.xsd', 54, 24)
    __href._UseLocation = pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/scap_core_0.1.xsd', 54, 24)
    
    href = property(__href.value, __href.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __href.name() : __href
    })
Namespace.addCategoryObject('typeBinding', 'referenceType', referenceType)




notesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'note'), textType, scope=notesType, location=pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/scap_core_0.1.xsd', 42, 18)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(notesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'note')), pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/scap_core_0.1.xsd', 42, 18))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
notesType._Automaton = _BuildAutomaton()




searchableCpeReferencesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'cpe-name'), cpeNamePatternType, scope=searchableCpeReferencesType, location=pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/scap_core_0.1.xsd', 81, 18)))

searchableCpeReferencesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'cpe-searchable-name'), cpeSearchableNamePatternType, scope=searchableCpeReferencesType, location=pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/scap_core_0.1.xsd', 82, 18)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(searchableCpeReferencesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'cpe-name')), pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/scap_core_0.1.xsd', 81, 18))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(searchableCpeReferencesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'cpe-searchable-name')), pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/scap_core_0.1.xsd', 82, 18))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
searchableCpeReferencesType._Automaton = _BuildAutomaton_()

