# ./_vuln.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:a1e85f0bb46ce56fe33ad4f3828508124f19838a
# Generated 2014-10-24 20:20:21.301391 by PyXB version 1.2.4 using Python 3.4.1.final.0
# Namespace http://scap.nist.gov/schema/vulnerability/0.4 [xmlns:vuln]

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
import lib.nvd._cce as _ImportedBinding__cce
import pyxb.binding.xml_
import lib.nvd._cvssv2 as _ImportedBinding__cvssv2
import lib.nvd._cpe_lang as _ImportedBinding__cpe_lang
import pyxb.binding.datatypes
import lib.nvd._cve as _ImportedBinding__cve
import lib.nvd._patch as _ImportedBinding__patch
import lib.nvd._scap_core as _ImportedBinding__scap_core

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://scap.nist.gov/schema/vulnerability/0.4', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_patch = _ImportedBinding__patch.Namespace
_Namespace_patch.configureCategories(['typeBinding', 'elementBinding'])

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


# Atomic simple type: {http://scap.nist.gov/schema/vulnerability/0.4}fixActionDescriptionEnumType
class fixActionDescriptionEnumType (pyxb.binding.datatypes.token, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'fixActionDescriptionEnumType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 35, 2)
    _Documentation = None
fixActionDescriptionEnumType._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=fixActionDescriptionEnumType)
fixActionDescriptionEnumType.PATCH = fixActionDescriptionEnumType._CF_enumeration.addEnumeration(unicode_value='PATCH', tag='PATCH')
fixActionDescriptionEnumType.SOFTWARE_UPDATE = fixActionDescriptionEnumType._CF_enumeration.addEnumeration(unicode_value='SOFTWARE_UPDATE', tag='SOFTWARE_UPDATE')
fixActionDescriptionEnumType.CONFIGURATION_CHANGE = fixActionDescriptionEnumType._CF_enumeration.addEnumeration(unicode_value='CONFIGURATION_CHANGE', tag='CONFIGURATION_CHANGE')
fixActionDescriptionEnumType.POLICY_CHANGE = fixActionDescriptionEnumType._CF_enumeration.addEnumeration(unicode_value='POLICY_CHANGE', tag='POLICY_CHANGE')
fixActionDescriptionEnumType.EXTERNAL_MITIGATION = fixActionDescriptionEnumType._CF_enumeration.addEnumeration(unicode_value='EXTERNAL_MITIGATION', tag='EXTERNAL_MITIGATION')
fixActionDescriptionEnumType._InitializeFacetMap(fixActionDescriptionEnumType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'fixActionDescriptionEnumType', fixActionDescriptionEnumType)

# Atomic simple type: {http://scap.nist.gov/schema/vulnerability/0.4}fixActionTypeEnumType
class fixActionTypeEnumType (pyxb.binding.datatypes.token, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'fixActionTypeEnumType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 47, 2)
    _Documentation = None
fixActionTypeEnumType._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=fixActionTypeEnumType)
fixActionTypeEnumType.MITIGATION = fixActionTypeEnumType._CF_enumeration.addEnumeration(unicode_value='MITIGATION', tag='MITIGATION')
fixActionTypeEnumType.REMEDIATION = fixActionTypeEnumType._CF_enumeration.addEnumeration(unicode_value='REMEDIATION', tag='REMEDIATION')
fixActionTypeEnumType._InitializeFacetMap(fixActionTypeEnumType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'fixActionTypeEnumType', fixActionTypeEnumType)

# Atomic simple type: {http://scap.nist.gov/schema/vulnerability/0.4}fixEffectivenessEnumType
class fixEffectivenessEnumType (pyxb.binding.datatypes.token, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'fixEffectivenessEnumType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 56, 2)
    _Documentation = None
fixEffectivenessEnumType._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=fixEffectivenessEnumType)
fixEffectivenessEnumType.PARTIAL = fixEffectivenessEnumType._CF_enumeration.addEnumeration(unicode_value='PARTIAL', tag='PARTIAL')
fixEffectivenessEnumType.COMPLETE = fixEffectivenessEnumType._CF_enumeration.addEnumeration(unicode_value='COMPLETE', tag='COMPLETE')
fixEffectivenessEnumType._InitializeFacetMap(fixEffectivenessEnumType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'fixEffectivenessEnumType', fixEffectivenessEnumType)

# Atomic simple type: {http://scap.nist.gov/schema/vulnerability/0.4}vulnerabilityReferenceCategoryEnumType
class vulnerabilityReferenceCategoryEnumType (pyxb.binding.datatypes.token, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'vulnerabilityReferenceCategoryEnumType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 65, 2)
    _Documentation = None
vulnerabilityReferenceCategoryEnumType._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=vulnerabilityReferenceCategoryEnumType)
vulnerabilityReferenceCategoryEnumType.PATCH = vulnerabilityReferenceCategoryEnumType._CF_enumeration.addEnumeration(unicode_value='PATCH', tag='PATCH')
vulnerabilityReferenceCategoryEnumType.VENDOR_ADVISORY = vulnerabilityReferenceCategoryEnumType._CF_enumeration.addEnumeration(unicode_value='VENDOR_ADVISORY', tag='VENDOR_ADVISORY')
vulnerabilityReferenceCategoryEnumType.THIRD_PARTY_ADVISORY = vulnerabilityReferenceCategoryEnumType._CF_enumeration.addEnumeration(unicode_value='THIRD_PARTY_ADVISORY', tag='THIRD_PARTY_ADVISORY')
vulnerabilityReferenceCategoryEnumType.SIGNATURE_SOURCE = vulnerabilityReferenceCategoryEnumType._CF_enumeration.addEnumeration(unicode_value='SIGNATURE_SOURCE', tag='SIGNATURE_SOURCE')
vulnerabilityReferenceCategoryEnumType.MITIGATION_PROCEDURE = vulnerabilityReferenceCategoryEnumType._CF_enumeration.addEnumeration(unicode_value='MITIGATION_PROCEDURE', tag='MITIGATION_PROCEDURE')
vulnerabilityReferenceCategoryEnumType.TOOL_CONFIGURATION_DESCRIPTION = vulnerabilityReferenceCategoryEnumType._CF_enumeration.addEnumeration(unicode_value='TOOL_CONFIGURATION_DESCRIPTION', tag='TOOL_CONFIGURATION_DESCRIPTION')
vulnerabilityReferenceCategoryEnumType.UNKNOWN = vulnerabilityReferenceCategoryEnumType._CF_enumeration.addEnumeration(unicode_value='UNKNOWN', tag='UNKNOWN')
vulnerabilityReferenceCategoryEnumType._InitializeFacetMap(vulnerabilityReferenceCategoryEnumType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'vulnerabilityReferenceCategoryEnumType', vulnerabilityReferenceCategoryEnumType)

# Atomic simple type: {http://scap.nist.gov/schema/vulnerability/0.4}securityProtectionType
class securityProtectionType (pyxb.binding.datatypes.token, pyxb.binding.basis.enumeration_mixin):

    """The security protection type"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'securityProtectionType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 79, 2)
    _Documentation = 'The security protection type'
securityProtectionType._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=securityProtectionType)
securityProtectionType.ALLOWS_ADMIN_ACCESS = securityProtectionType._CF_enumeration.addEnumeration(unicode_value='ALLOWS_ADMIN_ACCESS', tag='ALLOWS_ADMIN_ACCESS')
securityProtectionType.ALLOWS_USER_ACCESS = securityProtectionType._CF_enumeration.addEnumeration(unicode_value='ALLOWS_USER_ACCESS', tag='ALLOWS_USER_ACCESS')
securityProtectionType.ALLOWS_OTHER_ACCESS = securityProtectionType._CF_enumeration.addEnumeration(unicode_value='ALLOWS_OTHER_ACCESS', tag='ALLOWS_OTHER_ACCESS')
securityProtectionType._InitializeFacetMap(securityProtectionType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'securityProtectionType', securityProtectionType)

# Atomic simple type: {http://scap.nist.gov/schema/vulnerability/0.4}vulnerabilityIdType
class vulnerabilityIdType (pyxb.binding.datatypes.token):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'vulnerabilityIdType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 257, 2)
    _Documentation = None
vulnerabilityIdType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'vulnerabilityIdType', vulnerabilityIdType)

# Complex type {http://scap.nist.gov/schema/vulnerability/0.4}associatedExploitLocationType with content type ELEMENT_ONLY
class associatedExploitLocationType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://scap.nist.gov/schema/vulnerability/0.4}associatedExploitLocationType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'associatedExploitLocationType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 103, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://scap.nist.gov/schema/vulnerability/0.4}physical-access uses Python identifier physical_access
    __physical_access = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'physical-access'), 'physical_access', '__httpscap_nist_govschemavulnerability0_4_associatedExploitLocationType_httpscap_nist_govschemavulnerability0_4physical_access', False, pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 105, 6), )

    
    physical_access = property(__physical_access.value, __physical_access.set, None, None)

    
    # Element {http://scap.nist.gov/schema/vulnerability/0.4}voluntarily-interact uses Python identifier voluntarily_interact
    __voluntarily_interact = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'voluntarily-interact'), 'voluntarily_interact', '__httpscap_nist_govschemavulnerability0_4_associatedExploitLocationType_httpscap_nist_govschemavulnerability0_4voluntarily_interact', False, pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 106, 6), )

    
    voluntarily_interact = property(__voluntarily_interact.value, __voluntarily_interact.set, None, None)

    
    # Element {http://scap.nist.gov/schema/vulnerability/0.4}dialup uses Python identifier dialup
    __dialup = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'dialup'), 'dialup', '__httpscap_nist_govschemavulnerability0_4_associatedExploitLocationType_httpscap_nist_govschemavulnerability0_4dialup', False, pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 107, 6), )

    
    dialup = property(__dialup.value, __dialup.set, None, None)

    
    # Element {http://scap.nist.gov/schema/vulnerability/0.4}unknown uses Python identifier unknown
    __unknown = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'unknown'), 'unknown', '__httpscap_nist_govschemavulnerability0_4_associatedExploitLocationType_httpscap_nist_govschemavulnerability0_4unknown', False, pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 108, 6), )

    
    unknown = property(__unknown.value, __unknown.set, None, None)

    _ElementMap.update({
        __physical_access.name() : __physical_access,
        __voluntarily_interact.name() : __voluntarily_interact,
        __dialup.name() : __dialup,
        __unknown.name() : __unknown
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'associatedExploitLocationType', associatedExploitLocationType)


# Complex type {http://scap.nist.gov/schema/vulnerability/0.4}osvdbExtensionType with content type ELEMENT_ONLY
class osvdbExtensionType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://scap.nist.gov/schema/vulnerability/0.4}osvdbExtensionType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'osvdbExtensionType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 158, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://scap.nist.gov/schema/vulnerability/0.4}exploit-location uses Python identifier exploit_location
    __exploit_location = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'exploit-location'), 'exploit_location', '__httpscap_nist_govschemavulnerability0_4_osvdbExtensionType_httpscap_nist_govschemavulnerability0_4exploit_location', False, pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 160, 6), )

    
    exploit_location = property(__exploit_location.value, __exploit_location.set, None, None)

    _ElementMap.update({
        __exploit_location.name() : __exploit_location
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'osvdbExtensionType', osvdbExtensionType)


# Complex type {http://scap.nist.gov/schema/vulnerability/0.4}toolConfigurationType with content type ELEMENT_ONLY
class toolConfigurationType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://scap.nist.gov/schema/vulnerability/0.4}toolConfigurationType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'toolConfigurationType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 166, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://scap.nist.gov/schema/vulnerability/0.4}name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'name'), 'name', '__httpscap_nist_govschemavulnerability0_4_toolConfigurationType_httpscap_nist_govschemavulnerability0_4name', False, pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 168, 6), )

    
    name = property(__name.value, __name.set, None, 'The CPE name of the scanning tool.  A value must be supplied for this element.  The CPE name can be used for a CPE from the NVD.  The CPE title attribute can be used for internal naming conventions. (or both, if possible)')

    
    # Element {http://scap.nist.gov/schema/vulnerability/0.4}definition uses Python identifier definition
    __definition = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'definition'), 'definition', '__httpscap_nist_govschemavulnerability0_4_toolConfigurationType_httpscap_nist_govschemavulnerability0_4definition', True, pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 173, 6), )

    
    definition = property(__definition.value, __definition.set, None, 'Defines required signature or policy definition that must be installed on the tool.')

    _ElementMap.update({
        __name.name() : __name,
        __definition.name() : __definition
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'toolConfigurationType', toolConfigurationType)


# Complex type {http://scap.nist.gov/schema/vulnerability/0.4}vulnerableSoftwareType with content type ELEMENT_ONLY
class vulnerableSoftwareType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://scap.nist.gov/schema/vulnerability/0.4}vulnerableSoftwareType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'vulnerableSoftwareType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 189, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://scap.nist.gov/schema/vulnerability/0.4}product uses Python identifier product
    __product = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'product'), 'product', '__httpscap_nist_govschemavulnerability0_4_vulnerableSoftwareType_httpscap_nist_govschemavulnerability0_4product', True, pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 191, 6), )

    
    product = property(__product.value, __product.set, None, None)

    _ElementMap.update({
        __product.name() : __product
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'vulnerableSoftwareType', vulnerableSoftwareType)


# Complex type {http://scap.nist.gov/schema/vulnerability/0.4}fixActionType with content type ELEMENT_ONLY
class fixActionType (pyxb.binding.basis.complexTypeDefinition):
    """A single fix action should only cover a single patch application, software update, configuration change, or external fix.  Dependencies should be documented by using the "next_fix_action" element to point to a recursive list of fix actions."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'fixActionType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 114, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://scap.nist.gov/schema/patch/0.1}patch uses Python identifier patch
    __patch = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_patch, 'patch'), 'patch', '__httpscap_nist_govschemavulnerability0_4_fixActionType_httpscap_nist_govschemapatch0_1patch', False, pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/patch_0.1.xsd', 17, 2), )

    
    patch = property(__patch.value, __patch.set, None, None)

    
    # Element {http://scap.nist.gov/schema/vulnerability/0.4}configuration-remediation uses Python identifier configuration_remediation
    __configuration_remediation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'configuration-remediation'), 'configuration_remediation', '__httpscap_nist_govschemavulnerability0_4_fixActionType_httpscap_nist_govschemavulnerability0_4configuration_remediation', False, pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 120, 6), )

    
    configuration_remediation = property(__configuration_remediation.value, __configuration_remediation.set, None, None)

    
    # Element {http://scap.nist.gov/schema/vulnerability/0.4}software-update uses Python identifier software_update
    __software_update = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'software-update'), 'software_update', '__httpscap_nist_govschemavulnerability0_4_fixActionType_httpscap_nist_govschemavulnerability0_4software_update', True, pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 121, 6), )

    
    software_update = property(__software_update.value, __software_update.set, None, 'CPE name of the software update package.')

    
    # Element {http://scap.nist.gov/schema/vulnerability/0.4}notes uses Python identifier notes
    __notes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'notes'), 'notes', '__httpscap_nist_govschemavulnerability0_4_fixActionType_httpscap_nist_govschemavulnerability0_4notes', True, pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 126, 6), )

    
    notes = property(__notes.value, __notes.set, None, None)

    
    # Element {http://scap.nist.gov/schema/vulnerability/0.4}deprecated-by uses Python identifier deprecated_by
    __deprecated_by = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'deprecated-by'), 'deprecated_by', '__httpscap_nist_govschemavulnerability0_4_fixActionType_httpscap_nist_govschemavulnerability0_4deprecated_by', True, pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 127, 6), )

    
    deprecated_by = property(__deprecated_by.value, __deprecated_by.set, None, None)

    
    # Element {http://scap.nist.gov/schema/vulnerability/0.4}next-fix-action uses Python identifier next_fix_action
    __next_fix_action = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'next-fix-action'), 'next_fix_action', '__httpscap_nist_govschemavulnerability0_4_fixActionType_httpscap_nist_govschemavulnerability0_4next_fix_action', True, pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 128, 6), )

    
    next_fix_action = property(__next_fix_action.value, __next_fix_action.set, None, None)

    
    # Element {http://scap.nist.gov/schema/vulnerability/0.4}fix-action-tool-configuration uses Python identifier fix_action_tool_configuration
    __fix_action_tool_configuration = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'fix-action-tool-configuration'), 'fix_action_tool_configuration', '__httpscap_nist_govschemavulnerability0_4_fixActionType_httpscap_nist_govschemavulnerability0_4fix_action_tool_configuration', True, pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 129, 6), )

    
    fix_action_tool_configuration = property(__fix_action_tool_configuration.value, __fix_action_tool_configuration.set, None, None)

    
    # Element {http://scap.nist.gov/schema/vulnerability/0.4}applicable-configuration uses Python identifier applicable_configuration
    __applicable_configuration = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'applicable-configuration'), 'applicable_configuration', '__httpscap_nist_govschemavulnerability0_4_fixActionType_httpscap_nist_govschemavulnerability0_4applicable_configuration', True, pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 130, 6), )

    
    applicable_configuration = property(__applicable_configuration.value, __applicable_configuration.set, None, None)

    
    # Element {http://scap.nist.gov/schema/vulnerability/0.4}effectiveness uses Python identifier effectiveness
    __effectiveness = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'effectiveness'), 'effectiveness', '__httpscap_nist_govschemavulnerability0_4_fixActionType_httpscap_nist_govschemavulnerability0_4effectiveness', False, pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 131, 6), )

    
    effectiveness = property(__effectiveness.value, __effectiveness.set, None, 'States whether the fix action fully avoids the risk associated with the vulnerability or reduces risk to some extent.')

    
    # Element {http://scap.nist.gov/schema/vulnerability/0.4}applicable-check uses Python identifier applicable_check
    __applicable_check = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'applicable-check'), 'applicable_check', '__httpscap_nist_govschemavulnerability0_4_fixActionType_httpscap_nist_govschemavulnerability0_4applicable_check', True, pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 136, 6), )

    
    applicable_check = property(__applicable_check.value, __applicable_check.set, None, 'Describes or points to the check/test (either OVAL or other) that this particular fix action addresses.  E.G. applying this fix will change the value of this test result.')

    
    # Attribute fix_action_description uses Python identifier fix_action_description
    __fix_action_description = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'fix_action_description'), 'fix_action_description', '__httpscap_nist_govschemavulnerability0_4_fixActionType_fix_action_description', fixActionDescriptionEnumType, required=True)
    __fix_action_description._DeclarationLocation = pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 142, 4)
    __fix_action_description._UseLocation = pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 142, 4)
    
    fix_action_description = property(__fix_action_description.value, __fix_action_description.set, None, None)

    
    # Attribute fix_action_type uses Python identifier fix_action_type
    __fix_action_type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'fix_action_type'), 'fix_action_type', '__httpscap_nist_govschemavulnerability0_4_fixActionType_fix_action_type', fixActionTypeEnumType, required=True)
    __fix_action_type._DeclarationLocation = pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 143, 4)
    __fix_action_type._UseLocation = pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 143, 4)
    
    fix_action_type = property(__fix_action_type.value, __fix_action_type.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__httpscap_nist_govschemavulnerability0_4_fixActionType_id', pyxb.binding.datatypes.token, required=True)
    __id._DeclarationLocation = pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 144, 4)
    __id._UseLocation = pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 144, 4)
    
    id = property(__id.value, __id.set, None, 'Unique value within the source.  Will be used with the source element to serve as a global unique identifier.')

    
    # Attribute source uses Python identifier source
    __source = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'source'), 'source', '__httpscap_nist_govschemavulnerability0_4_fixActionType_source', pyxb.binding.datatypes.anyURI, required=True)
    __source._DeclarationLocation = pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 149, 4)
    __source._UseLocation = pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 149, 4)
    
    source = property(__source.value, __source.set, None, 'Should be a URI-like -- e.g. inverted DNS address e.g mil.jtf-gno')

    _ElementMap.update({
        __patch.name() : __patch,
        __configuration_remediation.name() : __configuration_remediation,
        __software_update.name() : __software_update,
        __notes.name() : __notes,
        __deprecated_by.name() : __deprecated_by,
        __next_fix_action.name() : __next_fix_action,
        __fix_action_tool_configuration.name() : __fix_action_tool_configuration,
        __applicable_configuration.name() : __applicable_configuration,
        __effectiveness.name() : __effectiveness,
        __applicable_check.name() : __applicable_check
    })
    _AttributeMap.update({
        __fix_action_description.name() : __fix_action_description,
        __fix_action_type.name() : __fix_action_type,
        __id.name() : __id,
        __source.name() : __source
    })
Namespace.addCategoryObject('typeBinding', 'fixActionType', fixActionType)


# Complex type {http://scap.nist.gov/schema/vulnerability/0.4}cweReferenceType with content type EMPTY
class cweReferenceType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://scap.nist.gov/schema/vulnerability/0.4}cweReferenceType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'cweReferenceType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 183, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__httpscap_nist_govschemavulnerability0_4_cweReferenceType_id', _ImportedBinding__scap_core.cweNamePatternType, required=True)
    __id._DeclarationLocation = pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 184, 4)
    __id._UseLocation = pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 184, 4)
    
    id = property(__id.value, __id.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __id.name() : __id
    })
Namespace.addCategoryObject('typeBinding', 'cweReferenceType', cweReferenceType)


# Complex type {http://scap.nist.gov/schema/vulnerability/0.4}vulnerabilityType with content type ELEMENT_ONLY
class vulnerabilityType (pyxb.binding.basis.complexTypeDefinition):
    """TODO: Low priority: Add reference to notes type to allow analysts, vendor and other comments.  Add source attribute.  Maybe categorization?"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'vulnerabilityType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 197, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://scap.nist.gov/schema/vulnerability/0.4}osvdb-ext uses Python identifier osvdb_ext
    __osvdb_ext = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'osvdb-ext'), 'osvdb_ext', '__httpscap_nist_govschemavulnerability0_4_vulnerabilityType_httpscap_nist_govschemavulnerability0_4osvdb_ext', False, pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 202, 6), )

    
    osvdb_ext = property(__osvdb_ext.value, __osvdb_ext.set, None, None)

    
    # Element {http://scap.nist.gov/schema/vulnerability/0.4}vulnerable-configuration uses Python identifier vulnerable_configuration
    __vulnerable_configuration = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'vulnerable-configuration'), 'vulnerable_configuration', '__httpscap_nist_govschemavulnerability0_4_vulnerabilityType_httpscap_nist_govschemavulnerability0_4vulnerable_configuration', True, pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 203, 6), )

    
    vulnerable_configuration = property(__vulnerable_configuration.value, __vulnerable_configuration.set, None, None)

    
    # Element {http://scap.nist.gov/schema/vulnerability/0.4}vulnerable-software-list uses Python identifier vulnerable_software_list
    __vulnerable_software_list = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'vulnerable-software-list'), 'vulnerable_software_list', '__httpscap_nist_govschemavulnerability0_4_vulnerabilityType_httpscap_nist_govschemavulnerability0_4vulnerable_software_list', False, pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 204, 6), )

    
    vulnerable_software_list = property(__vulnerable_software_list.value, __vulnerable_software_list.set, None, None)

    
    # Element {http://scap.nist.gov/schema/vulnerability/0.4}cve-id uses Python identifier cve_id
    __cve_id = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'cve-id'), 'cve_id', '__httpscap_nist_govschemavulnerability0_4_vulnerabilityType_httpscap_nist_govschemavulnerability0_4cve_id', False, pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 206, 8), )

    
    cve_id = property(__cve_id.value, __cve_id.set, None, None)

    
    # Element {http://scap.nist.gov/schema/vulnerability/0.4}cce-id uses Python identifier cce_id
    __cce_id = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'cce-id'), 'cce_id', '__httpscap_nist_govschemavulnerability0_4_vulnerabilityType_httpscap_nist_govschemavulnerability0_4cce_id', False, pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 207, 8), )

    
    cce_id = property(__cce_id.value, __cce_id.set, None, None)

    
    # Element {http://scap.nist.gov/schema/vulnerability/0.4}discovered-datetime uses Python identifier discovered_datetime
    __discovered_datetime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'discovered-datetime'), 'discovered_datetime', '__httpscap_nist_govschemavulnerability0_4_vulnerabilityType_httpscap_nist_govschemavulnerability0_4discovered_datetime', False, pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 209, 6), )

    
    discovered_datetime = property(__discovered_datetime.value, __discovered_datetime.set, None, None)

    
    # Element {http://scap.nist.gov/schema/vulnerability/0.4}disclosure-datetime uses Python identifier disclosure_datetime
    __disclosure_datetime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'disclosure-datetime'), 'disclosure_datetime', '__httpscap_nist_govschemavulnerability0_4_vulnerabilityType_httpscap_nist_govschemavulnerability0_4disclosure_datetime', False, pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 210, 6), )

    
    disclosure_datetime = property(__disclosure_datetime.value, __disclosure_datetime.set, None, None)

    
    # Element {http://scap.nist.gov/schema/vulnerability/0.4}exploit-publish-datetime uses Python identifier exploit_publish_datetime
    __exploit_publish_datetime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'exploit-publish-datetime'), 'exploit_publish_datetime', '__httpscap_nist_govschemavulnerability0_4_vulnerabilityType_httpscap_nist_govschemavulnerability0_4exploit_publish_datetime', False, pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 211, 6), )

    
    exploit_publish_datetime = property(__exploit_publish_datetime.value, __exploit_publish_datetime.set, None, None)

    
    # Element {http://scap.nist.gov/schema/vulnerability/0.4}published-datetime uses Python identifier published_datetime
    __published_datetime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'published-datetime'), 'published_datetime', '__httpscap_nist_govschemavulnerability0_4_vulnerabilityType_httpscap_nist_govschemavulnerability0_4published_datetime', False, pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 212, 6), )

    
    published_datetime = property(__published_datetime.value, __published_datetime.set, None, None)

    
    # Element {http://scap.nist.gov/schema/vulnerability/0.4}last-modified-datetime uses Python identifier last_modified_datetime
    __last_modified_datetime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'last-modified-datetime'), 'last_modified_datetime', '__httpscap_nist_govschemavulnerability0_4_vulnerabilityType_httpscap_nist_govschemavulnerability0_4last_modified_datetime', False, pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 213, 6), )

    
    last_modified_datetime = property(__last_modified_datetime.value, __last_modified_datetime.set, None, None)

    
    # Element {http://scap.nist.gov/schema/vulnerability/0.4}cvss uses Python identifier cvss
    __cvss = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'cvss'), 'cvss', '__httpscap_nist_govschemavulnerability0_4_vulnerabilityType_httpscap_nist_govschemavulnerability0_4cvss', False, pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 214, 6), )

    
    cvss = property(__cvss.value, __cvss.set, None, None)

    
    # Element {http://scap.nist.gov/schema/vulnerability/0.4}security-protection uses Python identifier security_protection
    __security_protection = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'security-protection'), 'security_protection', '__httpscap_nist_govschemavulnerability0_4_vulnerabilityType_httpscap_nist_govschemavulnerability0_4security_protection', False, pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 215, 6), )

    
    security_protection = property(__security_protection.value, __security_protection.set, None, None)

    
    # Element {http://scap.nist.gov/schema/vulnerability/0.4}assessment_check uses Python identifier assessment_check
    __assessment_check = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'assessment_check'), 'assessment_check', '__httpscap_nist_govschemavulnerability0_4_vulnerabilityType_httpscap_nist_govschemavulnerability0_4assessment_check', True, pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 216, 6), )

    
    assessment_check = property(__assessment_check.value, __assessment_check.set, None, None)

    
    # Element {http://scap.nist.gov/schema/vulnerability/0.4}cwe uses Python identifier cwe
    __cwe = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'cwe'), 'cwe', '__httpscap_nist_govschemavulnerability0_4_vulnerabilityType_httpscap_nist_govschemavulnerability0_4cwe', True, pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 217, 6), )

    
    cwe = property(__cwe.value, __cwe.set, None, None)

    
    # Element {http://scap.nist.gov/schema/vulnerability/0.4}references uses Python identifier references
    __references = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'references'), 'references', '__httpscap_nist_govschemavulnerability0_4_vulnerabilityType_httpscap_nist_govschemavulnerability0_4references', True, pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 218, 6), )

    
    references = property(__references.value, __references.set, None, None)

    
    # Element {http://scap.nist.gov/schema/vulnerability/0.4}fix_action uses Python identifier fix_action
    __fix_action = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'fix_action'), 'fix_action', '__httpscap_nist_govschemavulnerability0_4_vulnerabilityType_httpscap_nist_govschemavulnerability0_4fix_action', True, pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 219, 6), )

    
    fix_action = property(__fix_action.value, __fix_action.set, None, None)

    
    # Element {http://scap.nist.gov/schema/vulnerability/0.4}scanner uses Python identifier scanner
    __scanner = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'scanner'), 'scanner', '__httpscap_nist_govschemavulnerability0_4_vulnerabilityType_httpscap_nist_govschemavulnerability0_4scanner', True, pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 220, 6), )

    
    scanner = property(__scanner.value, __scanner.set, None, 'Denotes a scanner and required configuration that is capable of detecting the referenced vulnerability.  May also be an OVAL definition and omit scanner name.')

    
    # Element {http://scap.nist.gov/schema/vulnerability/0.4}summary uses Python identifier summary
    __summary = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'summary'), 'summary', '__httpscap_nist_govschemavulnerability0_4_vulnerabilityType_httpscap_nist_govschemavulnerability0_4summary', False, pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 225, 6), )

    
    summary = property(__summary.value, __summary.set, None, None)

    
    # Element {http://scap.nist.gov/schema/vulnerability/0.4}technical_description uses Python identifier technical_description
    __technical_description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'technical_description'), 'technical_description', '__httpscap_nist_govschemavulnerability0_4_vulnerabilityType_httpscap_nist_govschemavulnerability0_4technical_description', True, pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 226, 6), )

    
    technical_description = property(__technical_description.value, __technical_description.set, None, None)

    
    # Element {http://scap.nist.gov/schema/vulnerability/0.4}attack_scenario uses Python identifier attack_scenario
    __attack_scenario = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'attack_scenario'), 'attack_scenario', '__httpscap_nist_govschemavulnerability0_4_vulnerabilityType_httpscap_nist_govschemavulnerability0_4attack_scenario', True, pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 227, 6), )

    
    attack_scenario = property(__attack_scenario.value, __attack_scenario.set, None, 'This element should ultimately be held in a threat model.')

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__httpscap_nist_govschemavulnerability0_4_vulnerabilityType_id', vulnerabilityIdType, required=True)
    __id._DeclarationLocation = pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 233, 4)
    __id._UseLocation = pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 233, 4)
    
    id = property(__id.value, __id.set, None, None)

    _ElementMap.update({
        __osvdb_ext.name() : __osvdb_ext,
        __vulnerable_configuration.name() : __vulnerable_configuration,
        __vulnerable_software_list.name() : __vulnerable_software_list,
        __cve_id.name() : __cve_id,
        __cce_id.name() : __cce_id,
        __discovered_datetime.name() : __discovered_datetime,
        __disclosure_datetime.name() : __disclosure_datetime,
        __exploit_publish_datetime.name() : __exploit_publish_datetime,
        __published_datetime.name() : __published_datetime,
        __last_modified_datetime.name() : __last_modified_datetime,
        __cvss.name() : __cvss,
        __security_protection.name() : __security_protection,
        __assessment_check.name() : __assessment_check,
        __cwe.name() : __cwe,
        __references.name() : __references,
        __fix_action.name() : __fix_action,
        __scanner.name() : __scanner,
        __summary.name() : __summary,
        __technical_description.name() : __technical_description,
        __attack_scenario.name() : __attack_scenario
    })
    _AttributeMap.update({
        __id.name() : __id
    })
Namespace.addCategoryObject('typeBinding', 'vulnerabilityType', vulnerabilityType)


# Complex type {http://scap.nist.gov/schema/vulnerability/0.4}vulnerabilityReferenceType with content type ELEMENT_ONLY
class vulnerabilityReferenceType (pyxb.binding.basis.complexTypeDefinition):
    """TODO: revisit referenceType and textTypeExtends the base "reference" class by adding the ability to specify which kind (within the vulnerability model) of reference it is.  See "Vulnerability_Reference_Category_List" enumeration."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'vulnerabilityReferenceType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 238, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://scap.nist.gov/schema/vulnerability/0.4}source uses Python identifier source
    __source = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'source'), 'source', '__httpscap_nist_govschemavulnerability0_4_vulnerabilityReferenceType_httpscap_nist_govschemavulnerability0_4source', False, pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 244, 10), )

    
    source = property(__source.value, __source.set, None, 'TODO: determine purpose')

    
    # Element {http://scap.nist.gov/schema/vulnerability/0.4}reference uses Python identifier reference
    __reference = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'reference'), 'reference', '__httpscap_nist_govschemavulnerability0_4_vulnerabilityReferenceType_httpscap_nist_govschemavulnerability0_4reference', False, pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 249, 10), )

    
    reference = property(__reference.value, __reference.set, None, None)

    
    # Element {http://scap.nist.gov/schema/vulnerability/0.4}notes uses Python identifier notes
    __notes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'notes'), 'notes', '__httpscap_nist_govschemavulnerability0_4_vulnerabilityReferenceType_httpscap_nist_govschemavulnerability0_4notes', False, pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 250, 10), )

    
    notes = property(__notes.value, __notes.set, None, None)

    
    # Attribute {http://www.w3.org/XML/1998/namespace}lang uses Python identifier lang
    __lang = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'lang'), 'lang', '__httpscap_nist_govschemavulnerability0_4_vulnerabilityReferenceType_httpwww_w3_orgXML1998namespacelang', pyxb.binding.xml_.STD_ANON_lang, unicode_default='en')
    __lang._DeclarationLocation = None
    __lang._UseLocation = pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 252, 8)
    
    lang = property(__lang.value, __lang.set, None, None)

    
    # Attribute reference_type uses Python identifier reference_type
    __reference_type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'reference_type'), 'reference_type', '__httpscap_nist_govschemavulnerability0_4_vulnerabilityReferenceType_reference_type', vulnerabilityReferenceCategoryEnumType, required=True)
    __reference_type._DeclarationLocation = pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 253, 8)
    __reference_type._UseLocation = pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 253, 8)
    
    reference_type = property(__reference_type.value, __reference_type.set, None, None)

    
    # Attribute deprecated uses Python identifier deprecated
    __deprecated = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'deprecated'), 'deprecated', '__httpscap_nist_govschemavulnerability0_4_vulnerabilityReferenceType_deprecated', pyxb.binding.datatypes.boolean)
    __deprecated._DeclarationLocation = pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 254, 8)
    __deprecated._UseLocation = pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 254, 8)
    
    deprecated = property(__deprecated.value, __deprecated.set, None, None)

    _ElementMap.update({
        __source.name() : __source,
        __reference.name() : __reference,
        __notes.name() : __notes
    })
    _AttributeMap.update({
        __lang.name() : __lang,
        __reference_type.name() : __reference_type,
        __deprecated.name() : __deprecated
    })
Namespace.addCategoryObject('typeBinding', 'vulnerabilityReferenceType', vulnerabilityReferenceType)


vulnerability = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'vulnerability'), vulnerabilityType, location=pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 28, 2))
Namespace.addCategoryObject('elementBinding', vulnerability.name().localName(), vulnerability)



associatedExploitLocationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'physical-access'), pyxb.binding.datatypes.boolean, scope=associatedExploitLocationType, location=pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 105, 6), unicode_default='false'))

associatedExploitLocationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'voluntarily-interact'), pyxb.binding.datatypes.boolean, scope=associatedExploitLocationType, location=pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 106, 6), unicode_default='false'))

associatedExploitLocationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'dialup'), pyxb.binding.datatypes.boolean, scope=associatedExploitLocationType, location=pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 107, 6), unicode_default='false'))

associatedExploitLocationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'unknown'), pyxb.binding.datatypes.boolean, scope=associatedExploitLocationType, location=pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 108, 6), unicode_default='false'))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 105, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 106, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 107, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 108, 6))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(associatedExploitLocationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'physical-access')), pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 105, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(associatedExploitLocationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'voluntarily-interact')), pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 106, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(associatedExploitLocationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'dialup')), pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 107, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(associatedExploitLocationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'unknown')), pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 108, 6))
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
associatedExploitLocationType._Automaton = _BuildAutomaton()




osvdbExtensionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'exploit-location'), associatedExploitLocationType, scope=osvdbExtensionType, location=pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 160, 6)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(osvdbExtensionType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'exploit-location')), pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 160, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
osvdbExtensionType._Automaton = _BuildAutomaton_()




toolConfigurationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'name'), _ImportedBinding__scap_core.cpeNamePatternType, scope=toolConfigurationType, documentation='The CPE name of the scanning tool.  A value must be supplied for this element.  The CPE name can be used for a CPE from the NVD.  The CPE title attribute can be used for internal naming conventions. (or both, if possible)', location=pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 168, 6)))

toolConfigurationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'definition'), _ImportedBinding__scap_core.checkReferenceType, scope=toolConfigurationType, documentation='Defines required signature or policy definition that must be installed on the tool.', location=pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 173, 6)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 168, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 173, 6))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(toolConfigurationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'name')), pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 168, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(toolConfigurationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'definition')), pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 173, 6))
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
toolConfigurationType._Automaton = _BuildAutomaton_2()




vulnerableSoftwareType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'product'), _ImportedBinding__cpe_lang.namePattern, scope=vulnerableSoftwareType, location=pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 191, 6)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(vulnerableSoftwareType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'product')), pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 191, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
vulnerableSoftwareType._Automaton = _BuildAutomaton_3()




fixActionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_patch, 'patch'), _ImportedBinding__patch.patchType, scope=fixActionType, location=pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/patch_0.1.xsd', 17, 2)))

fixActionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'configuration-remediation'), vulnerabilityReferenceType, scope=fixActionType, location=pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 120, 6)))

fixActionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'software-update'), _ImportedBinding__scap_core.cpeNamePatternType, scope=fixActionType, documentation='CPE name of the software update package.', location=pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 121, 6)))

fixActionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'notes'), pyxb.binding.datatypes.string, scope=fixActionType, location=pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 126, 6)))

fixActionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'deprecated-by'), _ImportedBinding__scap_core.cpeNamePatternType, scope=fixActionType, location=pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 127, 6)))

fixActionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'next-fix-action'), fixActionType, scope=fixActionType, location=pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 128, 6)))

fixActionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'fix-action-tool-configuration'), toolConfigurationType, scope=fixActionType, location=pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 129, 6)))

fixActionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'applicable-configuration'), _ImportedBinding__cpe_lang.PlatformType, scope=fixActionType, location=pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 130, 6)))

fixActionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'effectiveness'), fixEffectivenessEnumType, scope=fixActionType, documentation='States whether the fix action fully avoids the risk associated with the vulnerability or reduces risk to some extent.', location=pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 131, 6)))

fixActionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'applicable-check'), _ImportedBinding__scap_core.checkReferenceType, scope=fixActionType, documentation='Describes or points to the check/test (either OVAL or other) that this particular fix action addresses.  E.G. applying this fix will change the value of this test result.', location=pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 136, 6)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 119, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 120, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 121, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 126, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 127, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 128, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 129, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 130, 6))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 131, 6))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 136, 6))
    counters.add(cc_9)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(fixActionType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_patch, 'patch')), pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 119, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(fixActionType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'configuration-remediation')), pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 120, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(fixActionType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'software-update')), pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 121, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(fixActionType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'notes')), pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 126, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(fixActionType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'deprecated-by')), pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 127, 6))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(fixActionType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'next-fix-action')), pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 128, 6))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(fixActionType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'fix-action-tool-configuration')), pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 129, 6))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(fixActionType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'applicable-configuration')), pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 130, 6))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(fixActionType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'effectiveness')), pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 131, 6))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(fixActionType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'applicable-check')), pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 136, 6))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
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
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
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
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
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
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_9, True) ]))
    st_9._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
fixActionType._Automaton = _BuildAutomaton_4()




vulnerabilityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'osvdb-ext'), osvdbExtensionType, scope=vulnerabilityType, location=pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 202, 6)))

vulnerabilityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'vulnerable-configuration'), _ImportedBinding__cpe_lang.PlatformType, scope=vulnerabilityType, location=pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 203, 6)))

vulnerabilityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'vulnerable-software-list'), vulnerableSoftwareType, scope=vulnerabilityType, location=pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 204, 6)))

vulnerabilityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'cve-id'), _ImportedBinding__cve.cveNamePatternType, scope=vulnerabilityType, location=pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 206, 8)))

vulnerabilityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'cce-id'), _ImportedBinding__cce.cceNamePatternType, scope=vulnerabilityType, location=pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 207, 8)))

vulnerabilityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'discovered-datetime'), pyxb.binding.datatypes.dateTime, scope=vulnerabilityType, location=pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 209, 6)))

vulnerabilityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'disclosure-datetime'), pyxb.binding.datatypes.dateTime, scope=vulnerabilityType, location=pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 210, 6)))

vulnerabilityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'exploit-publish-datetime'), pyxb.binding.datatypes.dateTime, scope=vulnerabilityType, location=pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 211, 6)))

vulnerabilityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'published-datetime'), pyxb.binding.datatypes.dateTime, scope=vulnerabilityType, location=pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 212, 6)))

vulnerabilityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'last-modified-datetime'), pyxb.binding.datatypes.dateTime, scope=vulnerabilityType, location=pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 213, 6)))

vulnerabilityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'cvss'), _ImportedBinding__cvssv2.cvssImpactType, scope=vulnerabilityType, location=pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 214, 6)))

vulnerabilityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'security-protection'), securityProtectionType, scope=vulnerabilityType, location=pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 215, 6)))

vulnerabilityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'assessment_check'), _ImportedBinding__scap_core.checkReferenceType, scope=vulnerabilityType, location=pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 216, 6)))

vulnerabilityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'cwe'), cweReferenceType, scope=vulnerabilityType, location=pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 217, 6)))

vulnerabilityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'references'), vulnerabilityReferenceType, scope=vulnerabilityType, location=pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 218, 6)))

vulnerabilityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'fix_action'), fixActionType, scope=vulnerabilityType, location=pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 219, 6)))

vulnerabilityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'scanner'), toolConfigurationType, scope=vulnerabilityType, documentation='Denotes a scanner and required configuration that is capable of detecting the referenced vulnerability.  May also be an OVAL definition and omit scanner name.', location=pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 220, 6)))

vulnerabilityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'summary'), pyxb.binding.datatypes.string, scope=vulnerabilityType, location=pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 225, 6)))

vulnerabilityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'technical_description'), _ImportedBinding__scap_core.referenceType, scope=vulnerabilityType, location=pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 226, 6)))

vulnerabilityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'attack_scenario'), _ImportedBinding__scap_core.referenceType, scope=vulnerabilityType, documentation='This element should ultimately be held in a threat model.', location=pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 227, 6)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 202, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 203, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 204, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 205, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 209, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 210, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 211, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 212, 6))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 213, 6))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 214, 6))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 215, 6))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 216, 6))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 217, 6))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 218, 6))
    counters.add(cc_13)
    cc_14 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 219, 6))
    counters.add(cc_14)
    cc_15 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 220, 6))
    counters.add(cc_15)
    cc_16 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 225, 6))
    counters.add(cc_16)
    cc_17 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 226, 6))
    counters.add(cc_17)
    cc_18 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 227, 6))
    counters.add(cc_18)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(vulnerabilityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'osvdb-ext')), pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 202, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(vulnerabilityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'vulnerable-configuration')), pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 203, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(vulnerabilityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'vulnerable-software-list')), pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 204, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(vulnerabilityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'cve-id')), pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 206, 8))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(vulnerabilityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'cce-id')), pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 207, 8))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(vulnerabilityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'discovered-datetime')), pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 209, 6))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(vulnerabilityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'disclosure-datetime')), pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 210, 6))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(vulnerabilityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'exploit-publish-datetime')), pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 211, 6))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(vulnerabilityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'published-datetime')), pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 212, 6))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(vulnerabilityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'last-modified-datetime')), pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 213, 6))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(vulnerabilityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'cvss')), pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 214, 6))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(vulnerabilityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'security-protection')), pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 215, 6))
    st_11 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(vulnerabilityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'assessment_check')), pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 216, 6))
    st_12 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(vulnerabilityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'cwe')), pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 217, 6))
    st_13 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_13, False))
    symbol = pyxb.binding.content.ElementUse(vulnerabilityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'references')), pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 218, 6))
    st_14 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_14, False))
    symbol = pyxb.binding.content.ElementUse(vulnerabilityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'fix_action')), pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 219, 6))
    st_15 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_15, False))
    symbol = pyxb.binding.content.ElementUse(vulnerabilityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'scanner')), pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 220, 6))
    st_16 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_16)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_16, False))
    symbol = pyxb.binding.content.ElementUse(vulnerabilityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'summary')), pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 225, 6))
    st_17 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_17)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_17, False))
    symbol = pyxb.binding.content.ElementUse(vulnerabilityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'technical_description')), pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 226, 6))
    st_18 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_18)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_18, False))
    symbol = pyxb.binding.content.ElementUse(vulnerabilityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'attack_scenario')), pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 227, 6))
    st_19 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_19)
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
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_19, [
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
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_19, [
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
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_11, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_11, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_12, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_12, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_13, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_13, False) ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_14, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_14, False) ]))
    st_15._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_15, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_15, False) ]))
    st_16._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_16, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_16, False) ]))
    st_17._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_17, False) ]))
    st_18._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_18, True) ]))
    st_19._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
vulnerabilityType._Automaton = _BuildAutomaton_5()




vulnerabilityReferenceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'source'), pyxb.binding.datatypes.string, scope=vulnerabilityReferenceType, documentation='TODO: determine purpose', location=pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 244, 10)))

vulnerabilityReferenceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'reference'), _ImportedBinding__scap_core.referenceType, scope=vulnerabilityReferenceType, location=pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 249, 10)))

vulnerabilityReferenceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'notes'), _ImportedBinding__scap_core.notesType, scope=vulnerabilityReferenceType, location=pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 250, 10)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 244, 10))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 250, 10))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(vulnerabilityReferenceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'source')), pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 244, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(vulnerabilityReferenceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'reference')), pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 249, 10))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(vulnerabilityReferenceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'notes')), pyxb.utils.utility.Location('/Users/espen/Sources/nvd/schema/vulnerability_0.4.1.xsd', 250, 10))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
vulnerabilityReferenceType._Automaton = _BuildAutomaton_6()

