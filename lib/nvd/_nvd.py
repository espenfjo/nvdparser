# ./_nvd.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:8fe022686c06c832adf01afe4d37fedb9cfa9dd4
# Generated 2014-10-24 20:20:21.301747 by PyXB version 1.2.4 using Python 3.4.1.final.0
# Namespace http://scap.nist.gov/schema/feed/vulnerability/2.0

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
import lib.nvd._vuln as _ImportedBinding__vuln

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://scap.nist.gov/schema/feed/vulnerability/2.0', create_if_missing=True)
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


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """The root element of the NVD CVE feed. Multiple "entry" child elements describe specific NVD CVE entries."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/nvd.xsd', 35, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://scap.nist.gov/schema/feed/vulnerability/2.0}entry uses Python identifier entry
    __entry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'entry'), 'entry', '__httpscap_nist_govschemafeedvulnerability2_0_CTD_ANON_httpscap_nist_govschemafeedvulnerability2_0entry', True, pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/nvd.xsd', 55, 1), )

    
    entry = property(__entry.value, __entry.set, None, 'A CVE entry.')

    
    # Attribute nvd_xml_version uses Python identifier nvd_xml_version
    __nvd_xml_version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'nvd_xml_version'), 'nvd_xml_version', '__httpscap_nist_govschemafeedvulnerability2_0_CTD_ANON_nvd_xml_version', pyxb.binding.datatypes.decimal, required=True)
    __nvd_xml_version._DeclarationLocation = pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/nvd.xsd', 43, 3)
    __nvd_xml_version._UseLocation = pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/nvd.xsd', 43, 3)
    
    nvd_xml_version = property(__nvd_xml_version.value, __nvd_xml_version.set, None, 'The schema version number supported by the feed.')

    
    # Attribute pub_date uses Python identifier pub_date
    __pub_date = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'pub_date'), 'pub_date', '__httpscap_nist_govschemafeedvulnerability2_0_CTD_ANON_pub_date', pyxb.binding.datatypes.dateTime, required=True)
    __pub_date._DeclarationLocation = pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/nvd.xsd', 48, 3)
    __pub_date._UseLocation = pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/nvd.xsd', 48, 3)
    
    pub_date = property(__pub_date.value, __pub_date.set, None, 'The date the feed was generated.')

    _ElementMap.update({
        __entry.name() : __entry
    })
    _AttributeMap.update({
        __nvd_xml_version.name() : __nvd_xml_version,
        __pub_date.name() : __pub_date
    })



nvd = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'nvd'), CTD_ANON, documentation='The root element of the NVD CVE feed. Multiple "entry" child elements describe specific NVD CVE entries.', location=pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/nvd.xsd', 31, 1))
Namespace.addCategoryObject('elementBinding', nvd.name().localName(), nvd)

entry = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'entry'), _ImportedBinding__vuln.vulnerabilityType, documentation='A CVE entry.', location=pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/nvd.xsd', 55, 1))
Namespace.addCategoryObject('elementBinding', entry.name().localName(), entry)



CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'entry'), _ImportedBinding__vuln.vulnerabilityType, scope=CTD_ANON, documentation='A CVE entry.', location=pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/nvd.xsd', 55, 1)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/nvd.xsd', 37, 4))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'entry')), pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/nvd.xsd', 37, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton()

