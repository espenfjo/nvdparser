# ./_patch.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:8d8e1ad239bb68b885342d90bb6167ec288bb4e6
# Generated 2014-10-24 20:20:21.299956 by PyXB version 1.2.4 using Python 3.4.1.final.0
# Namespace http://scap.nist.gov/schema/patch/0.1 [xmlns:patch]

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
import lib.nvd._scap_core as _ImportedBinding__scap_core

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://scap.nist.gov/schema/patch/0.1', create_if_missing=True)
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


# Complex type {http://scap.nist.gov/schema/patch/0.1}patchType with content type ELEMENT_ONLY
class patchType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://scap.nist.gov/schema/patch/0.1}patchType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'patchType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/patch_0.1.xsd', 24, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://scap.nist.gov/schema/patch/0.1}title uses Python identifier title
    __title = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'title'), 'title', '__httpscap_nist_govschemapatch0_1_patchType_httpscap_nist_govschemapatch0_1title', False, pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/patch_0.1.xsd', 26, 6), )

    
    title = property(__title.value, __title.set, None, 'Human-formatted title for the patch.  If none given, then duplicate of the name.')

    
    # Element {http://scap.nist.gov/schema/patch/0.1}references uses Python identifier references
    __references = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'references'), 'references', '__httpscap_nist_govschemapatch0_1_patchType_httpscap_nist_govschemapatch0_1references', False, pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/patch_0.1.xsd', 31, 6), )

    
    references = property(__references.value, __references.set, None, None)

    
    # Element {http://scap.nist.gov/schema/patch/0.1}notes uses Python identifier notes
    __notes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'notes'), 'notes', '__httpscap_nist_govschemapatch0_1_patchType_httpscap_nist_govschemapatch0_1notes', True, pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/patch_0.1.xsd', 38, 6), )

    
    notes = property(__notes.value, __notes.set, None, None)

    
    # Element {http://scap.nist.gov/schema/patch/0.1}check uses Python identifier check
    __check = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'check'), 'check', '__httpscap_nist_govschemapatch0_1_patchType_httpscap_nist_govschemapatch0_1check', True, pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/patch_0.1.xsd', 39, 6), )

    
    check = property(__check.value, __check.set, None, None)

    
    # Element {http://scap.nist.gov/schema/patch/0.1}supersedes uses Python identifier supersedes
    __supersedes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'supersedes'), 'supersedes', '__httpscap_nist_govschemapatch0_1_patchType_httpscap_nist_govschemapatch0_1supersedes', True, pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/patch_0.1.xsd', 40, 6), )

    
    supersedes = property(__supersedes.value, __supersedes.set, None, 'Patches that superceded by the referenced patch.')

    
    # Element {http://scap.nist.gov/schema/patch/0.1}superseded-by uses Python identifier superseded_by
    __superseded_by = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'superseded-by'), 'superseded_by', '__httpscap_nist_govschemapatch0_1_patchType_httpscap_nist_govschemapatch0_1superseded_by', True, pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/patch_0.1.xsd', 45, 6), )

    
    superseded_by = property(__superseded_by.value, __superseded_by.set, None, 'Patches that supersede the patch comprising the current XML document.')

    
    # Attribute identifier uses Python identifier identifier
    __identifier = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'identifier'), 'identifier', '__httpscap_nist_govschemapatch0_1_patchType_identifier', pyxb.binding.datatypes.double, required=True)
    __identifier._DeclarationLocation = pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/patch_0.1.xsd', 51, 4)
    __identifier._UseLocation = pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/patch_0.1.xsd', 51, 4)
    
    identifier = property(__identifier.value, __identifier.set, None, 'Identifier unique within the XML document for the given patch.')

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__httpscap_nist_govschemapatch0_1_patchType_name', pyxb.binding.datatypes.string, required=True)
    __name._DeclarationLocation = pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/patch_0.1.xsd', 56, 4)
    __name._UseLocation = pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/patch_0.1.xsd', 56, 4)
    
    name = property(__name.value, __name.set, None, 'Vendor supplied name for the patch.  Will use lower case and underscores for spaces, consistent with CPE naming conventions.')

    
    # Attribute superseded uses Python identifier superseded
    __superseded = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'superseded'), 'superseded', '__httpscap_nist_govschemapatch0_1_patchType_superseded', pyxb.binding.datatypes.boolean, required=True)
    __superseded._DeclarationLocation = pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/patch_0.1.xsd', 61, 4)
    __superseded._UseLocation = pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/patch_0.1.xsd', 61, 4)
    
    superseded = property(__superseded.value, __superseded.set, None, 'Boolean value.  True of patch is superseded.  False if not.')

    
    # Attribute deprecated uses Python identifier deprecated
    __deprecated = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'deprecated'), 'deprecated', '__httpscap_nist_govschemapatch0_1_patchType_deprecated', pyxb.binding.datatypes.boolean)
    __deprecated._DeclarationLocation = pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/patch_0.1.xsd', 66, 4)
    __deprecated._UseLocation = pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/patch_0.1.xsd', 66, 4)
    
    deprecated = property(__deprecated.value, __deprecated.set, None, 'Indicates that a patch should not be used -- regardless of supersession.')

    _ElementMap.update({
        __title.name() : __title,
        __references.name() : __references,
        __notes.name() : __notes,
        __check.name() : __check,
        __supersedes.name() : __supersedes,
        __superseded_by.name() : __superseded_by
    })
    _AttributeMap.update({
        __identifier.name() : __identifier,
        __name.name() : __name,
        __superseded.name() : __superseded,
        __deprecated.name() : __deprecated
    })
Namespace.addCategoryObject('typeBinding', 'patchType', patchType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/patch_0.1.xsd', 32, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://scap.nist.gov/schema/patch/0.1}reference uses Python identifier reference
    __reference = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'reference'), 'reference', '__httpscap_nist_govschemapatch0_1_CTD_ANON_httpscap_nist_govschemapatch0_1reference', True, pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/patch_0.1.xsd', 34, 12), )

    
    reference = property(__reference.value, __reference.set, None, None)

    _ElementMap.update({
        __reference.name() : __reference
    })
    _AttributeMap.update({
        
    })



patch = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'patch'), patchType, location=pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/patch_0.1.xsd', 17, 2))
Namespace.addCategoryObject('elementBinding', patch.name().localName(), patch)



patchType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'title'), _ImportedBinding__scap_core.textType, scope=patchType, documentation='Human-formatted title for the patch.  If none given, then duplicate of the name.', location=pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/patch_0.1.xsd', 26, 6)))

patchType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'references'), CTD_ANON, scope=patchType, location=pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/patch_0.1.xsd', 31, 6)))

patchType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'notes'), _ImportedBinding__scap_core.notesType, scope=patchType, location=pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/patch_0.1.xsd', 38, 6)))

patchType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'check'), _ImportedBinding__scap_core.checkReferenceType, scope=patchType, location=pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/patch_0.1.xsd', 39, 6)))

patchType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'supersedes'), patchType, scope=patchType, documentation='Patches that superceded by the referenced patch.', location=pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/patch_0.1.xsd', 40, 6)))

patchType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'superseded-by'), patchType, scope=patchType, documentation='Patches that supersede the patch comprising the current XML document.', location=pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/patch_0.1.xsd', 45, 6)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/patch_0.1.xsd', 26, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/patch_0.1.xsd', 31, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/patch_0.1.xsd', 38, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/patch_0.1.xsd', 39, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/patch_0.1.xsd', 40, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/patch_0.1.xsd', 45, 6))
    counters.add(cc_5)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(patchType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'title')), pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/patch_0.1.xsd', 26, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(patchType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'references')), pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/patch_0.1.xsd', 31, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(patchType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'notes')), pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/patch_0.1.xsd', 38, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(patchType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'check')), pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/patch_0.1.xsd', 39, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(patchType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'supersedes')), pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/patch_0.1.xsd', 40, 6))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(patchType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'superseded-by')), pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/patch_0.1.xsd', 45, 6))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
patchType._Automaton = _BuildAutomaton()




CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'reference'), _ImportedBinding__scap_core.referenceType, scope=CTD_ANON, location=pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/patch_0.1.xsd', 34, 12)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'reference')), pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/patch_0.1.xsd', 34, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton_()

