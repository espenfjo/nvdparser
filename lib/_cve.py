# ./_cve.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:d8321b44601264d267a190190d13bb0b67ebe529
# Generated 2014-10-11 12:09:17.505766 by PyXB version 1.2.3
# Namespace http://scap.nist.gov/schema/cve/0.1 [xmlns:cve]

import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:a8ecad70-512e-11e4-9ece-c82a144a09be')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.3'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# Import bindings for namespaces imported into schema
import _scap_core as _ImportedBinding__scap_core
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI(u'http://scap.nist.gov/schema/cve/0.1', create_if_missing=True)
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
        return CreateFromDOM(dom.documentElement)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, unicode):
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


# Atomic simple type: {http://scap.nist.gov/schema/cve/0.1}cveNamePatternType
class cveNamePatternType (pyxb.binding.datatypes.token):

    """Format for CVE Names is CVE-YYYY-NNNN, where YYYY is the year of publication and NNNN is a sequence number."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'cveNamePatternType')
    _XSDLocation = pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cve_0.1.xsd', 19, 2)
    _Documentation = u'Format for CVE Names is CVE-YYYY-NNNN, where YYYY is the year of publication and NNNN is a sequence number.'
cveNamePatternType._CF_pattern = pyxb.binding.facets.CF_pattern()
cveNamePatternType._CF_pattern.addPattern(pattern=u'CVE-([1,2])\\d{3}-\\d{4}')
cveNamePatternType._InitializeFacetMap(cveNamePatternType._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'cveNamePatternType', cveNamePatternType)

# Atomic simple type: {http://scap.nist.gov/schema/cve/0.1}cveStatus
class cveStatus (pyxb.binding.datatypes.token, pyxb.binding.basis.enumeration_mixin):

    """Enumeration containing valid values for CVE status: Candidate, Entry, and Deprecated"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'cveStatus')
    _XSDLocation = pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cve_0.1.xsd', 30, 2)
    _Documentation = u'Enumeration containing valid values for CVE status: Candidate, Entry, and Deprecated'
cveStatus._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=cveStatus, enum_prefix=None)
cveStatus.CANDIDATE = cveStatus._CF_enumeration.addEnumeration(unicode_value=u'CANDIDATE', tag=u'CANDIDATE')
cveStatus.ENTRY = cveStatus._CF_enumeration.addEnumeration(unicode_value=u'ENTRY', tag=u'ENTRY')
cveStatus.DEPRECATED = cveStatus._CF_enumeration.addEnumeration(unicode_value=u'DEPRECATED', tag=u'DEPRECATED')
cveStatus._InitializeFacetMap(cveStatus._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'cveStatus', cveStatus)

# Complex type {http://scap.nist.gov/schema/cve/0.1}cveType with content type ELEMENT_ONLY
class cveType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://scap.nist.gov/schema/cve/0.1}cveType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'cveType')
    _XSDLocation = pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cve_0.1.xsd', 46, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://scap.nist.gov/schema/cve/0.1}status uses Python identifier status
    __status = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'status'), 'status', '__httpscap_nist_govschemacve0_1_cveType_httpscap_nist_govschemacve0_1status', False, pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cve_0.1.xsd', 48, 6), )

    
    status = property(__status.value, __status.set, None, u'Status of Vulnerability -- Candidate, Entry, Deprecated')

    
    # Element {http://scap.nist.gov/schema/cve/0.1}description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'description'), 'description', '__httpscap_nist_govschemacve0_1_cveType_httpscap_nist_govschemacve0_1description', False, pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cve_0.1.xsd', 53, 6), )

    
    description = property(__description.value, __description.set, None, u'Free text field to describe the vulnerability')

    
    # Element {http://scap.nist.gov/schema/cve/0.1}references uses Python identifier references
    __references = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'references'), 'references', '__httpscap_nist_govschemacve0_1_cveType_httpscap_nist_govschemacve0_1references', True, pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cve_0.1.xsd', 58, 6), )

    
    references = property(__references.value, __references.set, None, u'Discretionary information and links relevant to a given vulnerability referenced by the CVE')

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'id'), 'id', '__httpscap_nist_govschemacve0_1_cveType_id', cveNamePatternType, required=True)
    __id._DeclarationLocation = pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cve_0.1.xsd', 64, 4)
    __id._UseLocation = pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cve_0.1.xsd', 64, 4)
    
    id = property(__id.value, __id.set, None, u'CVE name in the CVE-YYYY-NNNN format')

    _ElementMap.update({
        __status.name() : __status,
        __description.name() : __description,
        __references.name() : __references
    })
    _AttributeMap.update({
        __id.name() : __id
    })
Namespace.addCategoryObject('typeBinding', u'cveType', cveType)




cveType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'status'), cveStatus, scope=cveType, documentation=u'Status of Vulnerability -- Candidate, Entry, Deprecated', location=pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cve_0.1.xsd', 48, 6)))

cveType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'description'), pyxb.binding.datatypes.string, scope=cveType, documentation=u'Free text field to describe the vulnerability', location=pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cve_0.1.xsd', 53, 6)))

cveType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'references'), _ImportedBinding__scap_core.referenceType, scope=cveType, documentation=u'Discretionary information and links relevant to a given vulnerability referenced by the CVE', location=pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cve_0.1.xsd', 58, 6)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cve_0.1.xsd', 48, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cve_0.1.xsd', 53, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cve_0.1.xsd', 58, 6))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(cveType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'status')), pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cve_0.1.xsd', 48, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(cveType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'description')), pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cve_0.1.xsd', 53, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(cveType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'references')), pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cve_0.1.xsd', 58, 6))
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
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
cveType._Automaton = _BuildAutomaton()

