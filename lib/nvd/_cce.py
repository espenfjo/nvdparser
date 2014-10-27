# ./_cce.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:5c0d762d4b3131738ed0eec9d1949938a547d7a5
# Generated 2014-10-24 20:20:21.300354 by PyXB version 1.2.4 using Python 3.4.1.final.0
# Namespace http://scap.nist.gov/schema/cce/0.1 [xmlns:cce]

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
Namespace = pyxb.namespace.NamespaceForURI('http://scap.nist.gov/schema/cce/0.1', create_if_missing=True)
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


# Atomic simple type: {http://scap.nist.gov/schema/cce/0.1}cceNamePatternType
class cceNamePatternType (pyxb.binding.datatypes.token):

    """The format for a CCE name is CCE-NNNNNNNNNNN, where NNNNNNNNNNN is a sequence number."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'cceNamePatternType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/cce_0.1.xsd', 20, 2)
    _Documentation = 'The format for a CCE name is CCE-NNNNNNNNNNN, where NNNNNNNNNNN is a sequence number.'
cceNamePatternType._CF_pattern = pyxb.binding.facets.CF_pattern()
cceNamePatternType._CF_pattern.addPattern(pattern='CCE-[1-9]\\d{0,10}')
cceNamePatternType._InitializeFacetMap(cceNamePatternType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'cceNamePatternType', cceNamePatternType)

# Complex type {http://scap.nist.gov/schema/cce/0.1}cceParameterType with content type ELEMENT_ONLY
class cceParameterType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://scap.nist.gov/schema/cce/0.1}cceParameterType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'cceParameterType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/cce_0.1.xsd', 46, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://scap.nist.gov/schema/cce/0.1}value uses Python identifier value_
    __value = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'value'), 'value_', '__httpscap_nist_govschemacce0_1_cceParameterType_httpscap_nist_govschemacce0_1value', True, pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/cce_0.1.xsd', 48, 6), )

    
    value_ = property(__value.value, __value.set, None, None)

    
    # Attribute identifier uses Python identifier identifier
    __identifier = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'identifier'), 'identifier', '__httpscap_nist_govschemacce0_1_cceParameterType_identifier', pyxb.binding.datatypes.token)
    __identifier._DeclarationLocation = pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/cce_0.1.xsd', 50, 4)
    __identifier._UseLocation = pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/cce_0.1.xsd', 50, 4)
    
    identifier = property(__identifier.value, __identifier.set, None, 'TODO: What does this identify?')

    
    # Attribute operator uses Python identifier operator
    __operator = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'operator'), 'operator', '__httpscap_nist_govschemacce0_1_cceParameterType_operator', pyxb.binding.datatypes.token)
    __operator._DeclarationLocation = pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/cce_0.1.xsd', 55, 4)
    __operator._UseLocation = pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/cce_0.1.xsd', 55, 4)
    
    operator = property(__operator.value, __operator.set, None, 'TODO: should this be an enumeration?')

    _ElementMap.update({
        __value.name() : __value
    })
    _AttributeMap.update({
        __identifier.name() : __identifier,
        __operator.name() : __operator
    })
Namespace.addCategoryObject('typeBinding', 'cceParameterType', cceParameterType)


# Complex type {http://scap.nist.gov/schema/cce/0.1}cceType with content type ELEMENT_ONLY
class cceType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://scap.nist.gov/schema/cce/0.1}cceType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'cceType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/cce_0.1.xsd', 34, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://scap.nist.gov/schema/cce/0.1}definition uses Python identifier definition
    __definition = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'definition'), 'definition', '__httpscap_nist_govschemacce0_1_cceType_httpscap_nist_govschemacce0_1definition', False, pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/cce_0.1.xsd', 36, 6), )

    
    definition = property(__definition.value, __definition.set, None, None)

    
    # Element {http://scap.nist.gov/schema/cce/0.1}parameter uses Python identifier parameter
    __parameter = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'parameter'), 'parameter', '__httpscap_nist_govschemacce0_1_cceType_httpscap_nist_govschemacce0_1parameter', True, pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/cce_0.1.xsd', 37, 6), )

    
    parameter = property(__parameter.value, __parameter.set, None, None)

    
    # Element {http://scap.nist.gov/schema/cce/0.1}technical-mechanisms uses Python identifier technical_mechanisms
    __technical_mechanisms = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'technical-mechanisms'), 'technical_mechanisms', '__httpscap_nist_govschemacce0_1_cceType_httpscap_nist_govschemacce0_1technical_mechanisms', True, pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/cce_0.1.xsd', 38, 6), )

    
    technical_mechanisms = property(__technical_mechanisms.value, __technical_mechanisms.set, None, None)

    
    # Element {http://scap.nist.gov/schema/cce/0.1}references uses Python identifier references
    __references = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'references'), 'references', '__httpscap_nist_govschemacce0_1_cceType_httpscap_nist_govschemacce0_1references', True, pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/cce_0.1.xsd', 39, 6), )

    
    references = property(__references.value, __references.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__httpscap_nist_govschemacce0_1_cceType_id', cceNamePatternType, required=True)
    __id._DeclarationLocation = pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/cce_0.1.xsd', 41, 4)
    __id._UseLocation = pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/cce_0.1.xsd', 41, 4)
    
    id = property(__id.value, __id.set, None, None)

    _ElementMap.update({
        __definition.name() : __definition,
        __parameter.name() : __parameter,
        __technical_mechanisms.name() : __technical_mechanisms,
        __references.name() : __references
    })
    _AttributeMap.update({
        __id.name() : __id
    })
Namespace.addCategoryObject('typeBinding', 'cceType', cceType)




cceParameterType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'value'), pyxb.binding.datatypes.string, scope=cceParameterType, location=pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/cce_0.1.xsd', 48, 6)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(cceParameterType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'value')), pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/cce_0.1.xsd', 48, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
cceParameterType._Automaton = _BuildAutomaton()




cceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'definition'), pyxb.binding.datatypes.string, scope=cceType, location=pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/cce_0.1.xsd', 36, 6)))

cceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'parameter'), cceParameterType, scope=cceType, location=pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/cce_0.1.xsd', 37, 6)))

cceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'technical-mechanisms'), pyxb.binding.datatypes.string, scope=cceType, location=pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/cce_0.1.xsd', 38, 6)))

cceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'references'), _ImportedBinding__scap_core.referenceType, scope=cceType, location=pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/cce_0.1.xsd', 39, 6)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/cce_0.1.xsd', 36, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/cce_0.1.xsd', 37, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/cce_0.1.xsd', 38, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/cce_0.1.xsd', 39, 6))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(cceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'definition')), pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/cce_0.1.xsd', 36, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(cceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'parameter')), pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/cce_0.1.xsd', 37, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(cceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'technical-mechanisms')), pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/cce_0.1.xsd', 38, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(cceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'references')), pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/cce_0.1.xsd', 39, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
cceType._Automaton = _BuildAutomaton_()

