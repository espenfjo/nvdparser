# ./_cvssv2.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:681ba95213d1b7ed04eefeca5c3475c23b31f301
# Generated 2014-10-11 12:09:17.506061 by PyXB version 1.2.3
# Namespace http://scap.nist.gov/schema/cvss-v2/0.2 [xmlns:cvssv2]

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
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI(u'http://scap.nist.gov/schema/cvss-v2/0.2', create_if_missing=True)
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


# Atomic simple type: {http://scap.nist.gov/schema/cvss-v2/0.2}zeroToTenDecimalType
class zeroToTenDecimalType (pyxb.binding.datatypes.decimal):

    """Value restriction to single decimal values from 0.0 to 10.0, as used in CVSS scores"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'zeroToTenDecimalType')
    _XSDLocation = pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 16, 1)
    _Documentation = u'Value restriction to single decimal values from 0.0 to 10.0, as used in CVSS scores'
zeroToTenDecimalType._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=zeroToTenDecimalType, value=pyxb.binding.datatypes.decimal(10.0))
zeroToTenDecimalType._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=zeroToTenDecimalType, value=pyxb.binding.datatypes.decimal(0.0))
zeroToTenDecimalType._CF_fractionDigits = pyxb.binding.facets.CF_fractionDigits(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
zeroToTenDecimalType._InitializeFacetMap(zeroToTenDecimalType._CF_maxInclusive,
   zeroToTenDecimalType._CF_minInclusive,
   zeroToTenDecimalType._CF_fractionDigits)
Namespace.addCategoryObject('typeBinding', u'zeroToTenDecimalType', zeroToTenDecimalType)

# Atomic simple type: {http://scap.nist.gov/schema/cvss-v2/0.2}accessComplexityEnumType
class accessComplexityEnumType (pyxb.binding.datatypes.token, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'accessComplexityEnumType')
    _XSDLocation = pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 96, 1)
    _Documentation = None
accessComplexityEnumType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=accessComplexityEnumType, enum_prefix=None)
accessComplexityEnumType.HIGH = accessComplexityEnumType._CF_enumeration.addEnumeration(unicode_value=u'HIGH', tag=u'HIGH')
accessComplexityEnumType.MEDIUM = accessComplexityEnumType._CF_enumeration.addEnumeration(unicode_value=u'MEDIUM', tag=u'MEDIUM')
accessComplexityEnumType.LOW = accessComplexityEnumType._CF_enumeration.addEnumeration(unicode_value=u'LOW', tag=u'LOW')
accessComplexityEnumType._InitializeFacetMap(accessComplexityEnumType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'accessComplexityEnumType', accessComplexityEnumType)

# Atomic simple type: {http://scap.nist.gov/schema/cvss-v2/0.2}accessVectorEnumType
class accessVectorEnumType (pyxb.binding.datatypes.token, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'accessVectorEnumType')
    _XSDLocation = pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 113, 1)
    _Documentation = None
accessVectorEnumType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=accessVectorEnumType, enum_prefix=None)
accessVectorEnumType.LOCAL = accessVectorEnumType._CF_enumeration.addEnumeration(unicode_value=u'LOCAL', tag=u'LOCAL')
accessVectorEnumType.ADJACENT_NETWORK = accessVectorEnumType._CF_enumeration.addEnumeration(unicode_value=u'ADJACENT_NETWORK', tag=u'ADJACENT_NETWORK')
accessVectorEnumType.NETWORK = accessVectorEnumType._CF_enumeration.addEnumeration(unicode_value=u'NETWORK', tag=u'NETWORK')
accessVectorEnumType._InitializeFacetMap(accessVectorEnumType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'accessVectorEnumType', accessVectorEnumType)

# Atomic simple type: {http://scap.nist.gov/schema/cvss-v2/0.2}ciaRequirementEnumType
class ciaRequirementEnumType (pyxb.binding.datatypes.token, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ciaRequirementEnumType')
    _XSDLocation = pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 130, 1)
    _Documentation = None
ciaRequirementEnumType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ciaRequirementEnumType, enum_prefix=None)
ciaRequirementEnumType.LOW = ciaRequirementEnumType._CF_enumeration.addEnumeration(unicode_value=u'LOW', tag=u'LOW')
ciaRequirementEnumType.MEDIUM = ciaRequirementEnumType._CF_enumeration.addEnumeration(unicode_value=u'MEDIUM', tag=u'MEDIUM')
ciaRequirementEnumType.HIGH = ciaRequirementEnumType._CF_enumeration.addEnumeration(unicode_value=u'HIGH', tag=u'HIGH')
ciaRequirementEnumType.NOT_DEFINED = ciaRequirementEnumType._CF_enumeration.addEnumeration(unicode_value=u'NOT_DEFINED', tag=u'NOT_DEFINED')
ciaRequirementEnumType._InitializeFacetMap(ciaRequirementEnumType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'ciaRequirementEnumType', ciaRequirementEnumType)

# Atomic simple type: {http://scap.nist.gov/schema/cvss-v2/0.2}collateralDamagePotentialEnumType
class collateralDamagePotentialEnumType (pyxb.binding.datatypes.token, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'collateralDamagePotentialEnumType')
    _XSDLocation = pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 148, 1)
    _Documentation = None
collateralDamagePotentialEnumType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=collateralDamagePotentialEnumType, enum_prefix=None)
collateralDamagePotentialEnumType.NONE = collateralDamagePotentialEnumType._CF_enumeration.addEnumeration(unicode_value=u'NONE', tag=u'NONE')
collateralDamagePotentialEnumType.LOW = collateralDamagePotentialEnumType._CF_enumeration.addEnumeration(unicode_value=u'LOW', tag=u'LOW')
collateralDamagePotentialEnumType.LOW_MEDIUM = collateralDamagePotentialEnumType._CF_enumeration.addEnumeration(unicode_value=u'LOW_MEDIUM', tag=u'LOW_MEDIUM')
collateralDamagePotentialEnumType.MEDIUM_HIGH = collateralDamagePotentialEnumType._CF_enumeration.addEnumeration(unicode_value=u'MEDIUM_HIGH', tag=u'MEDIUM_HIGH')
collateralDamagePotentialEnumType.HIGH = collateralDamagePotentialEnumType._CF_enumeration.addEnumeration(unicode_value=u'HIGH', tag=u'HIGH')
collateralDamagePotentialEnumType.NOT_DEFINED = collateralDamagePotentialEnumType._CF_enumeration.addEnumeration(unicode_value=u'NOT_DEFINED', tag=u'NOT_DEFINED')
collateralDamagePotentialEnumType._InitializeFacetMap(collateralDamagePotentialEnumType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'collateralDamagePotentialEnumType', collateralDamagePotentialEnumType)

# Atomic simple type: {http://scap.nist.gov/schema/cvss-v2/0.2}targetDistributionEnumType
class targetDistributionEnumType (pyxb.binding.datatypes.token, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'targetDistributionEnumType')
    _XSDLocation = pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 168, 1)
    _Documentation = None
targetDistributionEnumType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=targetDistributionEnumType, enum_prefix=None)
targetDistributionEnumType.NONE = targetDistributionEnumType._CF_enumeration.addEnumeration(unicode_value=u'NONE', tag=u'NONE')
targetDistributionEnumType.LOW = targetDistributionEnumType._CF_enumeration.addEnumeration(unicode_value=u'LOW', tag=u'LOW')
targetDistributionEnumType.MEDIUM = targetDistributionEnumType._CF_enumeration.addEnumeration(unicode_value=u'MEDIUM', tag=u'MEDIUM')
targetDistributionEnumType.HIGH = targetDistributionEnumType._CF_enumeration.addEnumeration(unicode_value=u'HIGH', tag=u'HIGH')
targetDistributionEnumType.NOT_DEFINED = targetDistributionEnumType._CF_enumeration.addEnumeration(unicode_value=u'NOT_DEFINED', tag=u'NOT_DEFINED')
targetDistributionEnumType._InitializeFacetMap(targetDistributionEnumType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'targetDistributionEnumType', targetDistributionEnumType)

# Atomic simple type: {http://scap.nist.gov/schema/cvss-v2/0.2}ciaEnumType
class ciaEnumType (pyxb.binding.datatypes.token, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ciaEnumType')
    _XSDLocation = pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 187, 1)
    _Documentation = None
ciaEnumType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ciaEnumType, enum_prefix=None)
ciaEnumType.NONE = ciaEnumType._CF_enumeration.addEnumeration(unicode_value=u'NONE', tag=u'NONE')
ciaEnumType.PARTIAL = ciaEnumType._CF_enumeration.addEnumeration(unicode_value=u'PARTIAL', tag=u'PARTIAL')
ciaEnumType.COMPLETE = ciaEnumType._CF_enumeration.addEnumeration(unicode_value=u'COMPLETE', tag=u'COMPLETE')
ciaEnumType._InitializeFacetMap(ciaEnumType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'ciaEnumType', ciaEnumType)

# Atomic simple type: {http://scap.nist.gov/schema/cvss-v2/0.2}authenticationEnumType
class authenticationEnumType (pyxb.binding.datatypes.token, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'authenticationEnumType')
    _XSDLocation = pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 204, 1)
    _Documentation = None
authenticationEnumType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=authenticationEnumType, enum_prefix=None)
authenticationEnumType.MULTIPLE_INSTANCES = authenticationEnumType._CF_enumeration.addEnumeration(unicode_value=u'MULTIPLE_INSTANCES', tag=u'MULTIPLE_INSTANCES')
authenticationEnumType.SINGLE_INSTANCE = authenticationEnumType._CF_enumeration.addEnumeration(unicode_value=u'SINGLE_INSTANCE', tag=u'SINGLE_INSTANCE')
authenticationEnumType.NONE = authenticationEnumType._CF_enumeration.addEnumeration(unicode_value=u'NONE', tag=u'NONE')
authenticationEnumType._InitializeFacetMap(authenticationEnumType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'authenticationEnumType', authenticationEnumType)

# Atomic simple type: {http://scap.nist.gov/schema/cvss-v2/0.2}remediationLevelEnumType
class remediationLevelEnumType (pyxb.binding.datatypes.token, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'remediationLevelEnumType')
    _XSDLocation = pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 221, 1)
    _Documentation = None
remediationLevelEnumType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=remediationLevelEnumType, enum_prefix=None)
remediationLevelEnumType.OFFICIAL_FIX = remediationLevelEnumType._CF_enumeration.addEnumeration(unicode_value=u'OFFICIAL_FIX', tag=u'OFFICIAL_FIX')
remediationLevelEnumType.TEMPORARY_FIX = remediationLevelEnumType._CF_enumeration.addEnumeration(unicode_value=u'TEMPORARY_FIX', tag=u'TEMPORARY_FIX')
remediationLevelEnumType.WORKAROUND = remediationLevelEnumType._CF_enumeration.addEnumeration(unicode_value=u'WORKAROUND', tag=u'WORKAROUND')
remediationLevelEnumType.UNAVAILABLE = remediationLevelEnumType._CF_enumeration.addEnumeration(unicode_value=u'UNAVAILABLE', tag=u'UNAVAILABLE')
remediationLevelEnumType.NOT_DEFINED = remediationLevelEnumType._CF_enumeration.addEnumeration(unicode_value=u'NOT_DEFINED', tag=u'NOT_DEFINED')
remediationLevelEnumType._InitializeFacetMap(remediationLevelEnumType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'remediationLevelEnumType', remediationLevelEnumType)

# Atomic simple type: {http://scap.nist.gov/schema/cvss-v2/0.2}confidenceEnumType
class confidenceEnumType (pyxb.binding.datatypes.token, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'confidenceEnumType')
    _XSDLocation = pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 240, 1)
    _Documentation = None
confidenceEnumType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=confidenceEnumType, enum_prefix=None)
confidenceEnumType.UNCONFIRMED = confidenceEnumType._CF_enumeration.addEnumeration(unicode_value=u'UNCONFIRMED', tag=u'UNCONFIRMED')
confidenceEnumType.UNCORROBORATED = confidenceEnumType._CF_enumeration.addEnumeration(unicode_value=u'UNCORROBORATED', tag=u'UNCORROBORATED')
confidenceEnumType.CONFIRMED = confidenceEnumType._CF_enumeration.addEnumeration(unicode_value=u'CONFIRMED', tag=u'CONFIRMED')
confidenceEnumType.NOT_DEFINED = confidenceEnumType._CF_enumeration.addEnumeration(unicode_value=u'NOT_DEFINED', tag=u'NOT_DEFINED')
confidenceEnumType._InitializeFacetMap(confidenceEnumType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'confidenceEnumType', confidenceEnumType)

# Atomic simple type: {http://scap.nist.gov/schema/cvss-v2/0.2}exploitabilityEnumType
class exploitabilityEnumType (pyxb.binding.datatypes.token, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'exploitabilityEnumType')
    _XSDLocation = pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 258, 1)
    _Documentation = None
exploitabilityEnumType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=exploitabilityEnumType, enum_prefix=None)
exploitabilityEnumType.UNPROVEN = exploitabilityEnumType._CF_enumeration.addEnumeration(unicode_value=u'UNPROVEN', tag=u'UNPROVEN')
exploitabilityEnumType.PROOF_OF_CONCEPT = exploitabilityEnumType._CF_enumeration.addEnumeration(unicode_value=u'PROOF_OF_CONCEPT', tag=u'PROOF_OF_CONCEPT')
exploitabilityEnumType.FUNCTIONAL = exploitabilityEnumType._CF_enumeration.addEnumeration(unicode_value=u'FUNCTIONAL', tag=u'FUNCTIONAL')
exploitabilityEnumType.HIGH = exploitabilityEnumType._CF_enumeration.addEnumeration(unicode_value=u'HIGH', tag=u'HIGH')
exploitabilityEnumType.NOT_DEFINED = exploitabilityEnumType._CF_enumeration.addEnumeration(unicode_value=u'NOT_DEFINED', tag=u'NOT_DEFINED')
exploitabilityEnumType._InitializeFacetMap(exploitabilityEnumType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'exploitabilityEnumType', exploitabilityEnumType)

# Complex type {http://scap.nist.gov/schema/cvss-v2/0.2}metricsType with content type EMPTY
class metricsType (pyxb.binding.basis.complexTypeDefinition):
    """Base type for metrics that defines common attributes of all metrics."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'metricsType')
    _XSDLocation = pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 275, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute upgraded-from-version uses Python identifier upgraded_from_version
    __upgraded_from_version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'upgraded-from-version'), 'upgraded_from_version', '__httpscap_nist_govschemacvss_v20_2_metricsType_upgraded_from_version', pyxb.binding.datatypes.decimal)
    __upgraded_from_version._DeclarationLocation = pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 279, 2)
    __upgraded_from_version._UseLocation = pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 279, 2)
    
    upgraded_from_version = property(__upgraded_from_version.value, __upgraded_from_version.set, None, u"Indicates if the metrics have been upgraded from a previous version of CVSS.  If fields that were approximated will have an approximated attribute set to 'true'.")

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __upgraded_from_version.name() : __upgraded_from_version
    })
Namespace.addCategoryObject('typeBinding', u'metricsType', metricsType)


# Complex type {http://scap.nist.gov/schema/cvss-v2/0.2}cvssType with content type ELEMENT_ONLY
class cvssType (pyxb.binding.basis.complexTypeDefinition):
    """ "This schema was intentionally designed to avoid mixing classes and attributes between CVSS version 1, CVSS version 2, and future versions. Scores in the CVSS system are interdependent.  The temporal score is a multiplier of the base score.  The environmental score, in turn, is a multiplier of the temporal score.  The ability to transfer these scores independently is provided on the assumption that the user understands the business logic. For any given metric, it is preferred that the score, as a minimum is provided, however the score can be re-created from the metrics or the multiplier and any scores they are dependent on." """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'cvssType')
    _XSDLocation = pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 288, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://scap.nist.gov/schema/cvss-v2/0.2}base_metrics uses Python identifier base_metrics
    __base_metrics = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'base_metrics'), 'base_metrics', '__httpscap_nist_govschemacvss_v20_2_cvssType_httpscap_nist_govschemacvss_v20_2base_metrics', True, pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 293, 3), )

    
    base_metrics = property(__base_metrics.value, __base_metrics.set, None, None)

    
    # Element {http://scap.nist.gov/schema/cvss-v2/0.2}environmental_metrics uses Python identifier environmental_metrics
    __environmental_metrics = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'environmental_metrics'), 'environmental_metrics', '__httpscap_nist_govschemacvss_v20_2_cvssType_httpscap_nist_govschemacvss_v20_2environmental_metrics', True, pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 294, 3), )

    
    environmental_metrics = property(__environmental_metrics.value, __environmental_metrics.set, None, None)

    
    # Element {http://scap.nist.gov/schema/cvss-v2/0.2}temporal_metrics uses Python identifier temporal_metrics
    __temporal_metrics = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'temporal_metrics'), 'temporal_metrics', '__httpscap_nist_govschemacvss_v20_2_cvssType_httpscap_nist_govschemacvss_v20_2temporal_metrics', True, pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 295, 3), )

    
    temporal_metrics = property(__temporal_metrics.value, __temporal_metrics.set, None, None)

    _ElementMap.update({
        __base_metrics.name() : __base_metrics,
        __environmental_metrics.name() : __environmental_metrics,
        __temporal_metrics.name() : __temporal_metrics
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'cvssType', cvssType)


# Complex type {http://scap.nist.gov/schema/cvss-v2/0.2}accessComplexityType with content type SIMPLE
class accessComplexityType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://scap.nist.gov/schema/cvss-v2/0.2}accessComplexityType with content type SIMPLE"""
    _TypeDefinition = accessComplexityEnumType
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'accessComplexityType')
    _XSDLocation = pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 103, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is accessComplexityEnumType
    
    # Attribute approximated uses Python identifier approximated
    __approximated = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'approximated'), 'approximated', '__httpscap_nist_govschemacvss_v20_2_accessComplexityType_approximated', pyxb.binding.datatypes.boolean, unicode_default=u'false')
    __approximated._DeclarationLocation = pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 87, 2)
    __approximated._UseLocation = pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 87, 2)
    
    approximated = property(__approximated.value, __approximated.set, None, u'Indicates if the vector has been approximated as the result of an upgrade from a previous CVSS version')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __approximated.name() : __approximated
    })
Namespace.addCategoryObject('typeBinding', u'accessComplexityType', accessComplexityType)


# Complex type {http://scap.nist.gov/schema/cvss-v2/0.2}accessVectorType with content type SIMPLE
class accessVectorType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://scap.nist.gov/schema/cvss-v2/0.2}accessVectorType with content type SIMPLE"""
    _TypeDefinition = accessVectorEnumType
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'accessVectorType')
    _XSDLocation = pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 120, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is accessVectorEnumType
    
    # Attribute approximated uses Python identifier approximated
    __approximated = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'approximated'), 'approximated', '__httpscap_nist_govschemacvss_v20_2_accessVectorType_approximated', pyxb.binding.datatypes.boolean, unicode_default=u'false')
    __approximated._DeclarationLocation = pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 87, 2)
    __approximated._UseLocation = pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 87, 2)
    
    approximated = property(__approximated.value, __approximated.set, None, u'Indicates if the vector has been approximated as the result of an upgrade from a previous CVSS version')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __approximated.name() : __approximated
    })
Namespace.addCategoryObject('typeBinding', u'accessVectorType', accessVectorType)


# Complex type {http://scap.nist.gov/schema/cvss-v2/0.2}ciaRequirementType with content type SIMPLE
class ciaRequirementType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://scap.nist.gov/schema/cvss-v2/0.2}ciaRequirementType with content type SIMPLE"""
    _TypeDefinition = ciaRequirementEnumType
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ciaRequirementType')
    _XSDLocation = pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 138, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is ciaRequirementEnumType
    
    # Attribute approximated uses Python identifier approximated
    __approximated = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'approximated'), 'approximated', '__httpscap_nist_govschemacvss_v20_2_ciaRequirementType_approximated', pyxb.binding.datatypes.boolean, unicode_default=u'false')
    __approximated._DeclarationLocation = pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 87, 2)
    __approximated._UseLocation = pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 87, 2)
    
    approximated = property(__approximated.value, __approximated.set, None, u'Indicates if the vector has been approximated as the result of an upgrade from a previous CVSS version')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __approximated.name() : __approximated
    })
Namespace.addCategoryObject('typeBinding', u'ciaRequirementType', ciaRequirementType)


# Complex type {http://scap.nist.gov/schema/cvss-v2/0.2}collateralDamagePotentialType with content type SIMPLE
class collateralDamagePotentialType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://scap.nist.gov/schema/cvss-v2/0.2}collateralDamagePotentialType with content type SIMPLE"""
    _TypeDefinition = collateralDamagePotentialEnumType
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'collateralDamagePotentialType')
    _XSDLocation = pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 158, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is collateralDamagePotentialEnumType
    
    # Attribute approximated uses Python identifier approximated
    __approximated = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'approximated'), 'approximated', '__httpscap_nist_govschemacvss_v20_2_collateralDamagePotentialType_approximated', pyxb.binding.datatypes.boolean, unicode_default=u'false')
    __approximated._DeclarationLocation = pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 87, 2)
    __approximated._UseLocation = pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 87, 2)
    
    approximated = property(__approximated.value, __approximated.set, None, u'Indicates if the vector has been approximated as the result of an upgrade from a previous CVSS version')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __approximated.name() : __approximated
    })
Namespace.addCategoryObject('typeBinding', u'collateralDamagePotentialType', collateralDamagePotentialType)


# Complex type {http://scap.nist.gov/schema/cvss-v2/0.2}targetDistributionType with content type SIMPLE
class targetDistributionType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://scap.nist.gov/schema/cvss-v2/0.2}targetDistributionType with content type SIMPLE"""
    _TypeDefinition = targetDistributionEnumType
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'targetDistributionType')
    _XSDLocation = pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 177, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is targetDistributionEnumType
    
    # Attribute approximated uses Python identifier approximated
    __approximated = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'approximated'), 'approximated', '__httpscap_nist_govschemacvss_v20_2_targetDistributionType_approximated', pyxb.binding.datatypes.boolean, unicode_default=u'false')
    __approximated._DeclarationLocation = pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 87, 2)
    __approximated._UseLocation = pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 87, 2)
    
    approximated = property(__approximated.value, __approximated.set, None, u'Indicates if the vector has been approximated as the result of an upgrade from a previous CVSS version')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __approximated.name() : __approximated
    })
Namespace.addCategoryObject('typeBinding', u'targetDistributionType', targetDistributionType)


# Complex type {http://scap.nist.gov/schema/cvss-v2/0.2}ciaType with content type SIMPLE
class ciaType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://scap.nist.gov/schema/cvss-v2/0.2}ciaType with content type SIMPLE"""
    _TypeDefinition = ciaEnumType
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ciaType')
    _XSDLocation = pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 194, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is ciaEnumType
    
    # Attribute approximated uses Python identifier approximated
    __approximated = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'approximated'), 'approximated', '__httpscap_nist_govschemacvss_v20_2_ciaType_approximated', pyxb.binding.datatypes.boolean, unicode_default=u'false')
    __approximated._DeclarationLocation = pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 87, 2)
    __approximated._UseLocation = pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 87, 2)
    
    approximated = property(__approximated.value, __approximated.set, None, u'Indicates if the vector has been approximated as the result of an upgrade from a previous CVSS version')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __approximated.name() : __approximated
    })
Namespace.addCategoryObject('typeBinding', u'ciaType', ciaType)


# Complex type {http://scap.nist.gov/schema/cvss-v2/0.2}authenticationType with content type SIMPLE
class authenticationType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://scap.nist.gov/schema/cvss-v2/0.2}authenticationType with content type SIMPLE"""
    _TypeDefinition = authenticationEnumType
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'authenticationType')
    _XSDLocation = pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 211, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is authenticationEnumType
    
    # Attribute approximated uses Python identifier approximated
    __approximated = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'approximated'), 'approximated', '__httpscap_nist_govschemacvss_v20_2_authenticationType_approximated', pyxb.binding.datatypes.boolean, unicode_default=u'false')
    __approximated._DeclarationLocation = pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 87, 2)
    __approximated._UseLocation = pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 87, 2)
    
    approximated = property(__approximated.value, __approximated.set, None, u'Indicates if the vector has been approximated as the result of an upgrade from a previous CVSS version')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __approximated.name() : __approximated
    })
Namespace.addCategoryObject('typeBinding', u'authenticationType', authenticationType)


# Complex type {http://scap.nist.gov/schema/cvss-v2/0.2}remediationLevelType with content type SIMPLE
class remediationLevelType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://scap.nist.gov/schema/cvss-v2/0.2}remediationLevelType with content type SIMPLE"""
    _TypeDefinition = remediationLevelEnumType
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'remediationLevelType')
    _XSDLocation = pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 230, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is remediationLevelEnumType
    
    # Attribute approximated uses Python identifier approximated
    __approximated = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'approximated'), 'approximated', '__httpscap_nist_govschemacvss_v20_2_remediationLevelType_approximated', pyxb.binding.datatypes.boolean, unicode_default=u'false')
    __approximated._DeclarationLocation = pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 87, 2)
    __approximated._UseLocation = pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 87, 2)
    
    approximated = property(__approximated.value, __approximated.set, None, u'Indicates if the vector has been approximated as the result of an upgrade from a previous CVSS version')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __approximated.name() : __approximated
    })
Namespace.addCategoryObject('typeBinding', u'remediationLevelType', remediationLevelType)


# Complex type {http://scap.nist.gov/schema/cvss-v2/0.2}confidenceType with content type SIMPLE
class confidenceType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://scap.nist.gov/schema/cvss-v2/0.2}confidenceType with content type SIMPLE"""
    _TypeDefinition = confidenceEnumType
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'confidenceType')
    _XSDLocation = pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 248, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is confidenceEnumType
    
    # Attribute approximated uses Python identifier approximated
    __approximated = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'approximated'), 'approximated', '__httpscap_nist_govschemacvss_v20_2_confidenceType_approximated', pyxb.binding.datatypes.boolean, unicode_default=u'false')
    __approximated._DeclarationLocation = pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 87, 2)
    __approximated._UseLocation = pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 87, 2)
    
    approximated = property(__approximated.value, __approximated.set, None, u'Indicates if the vector has been approximated as the result of an upgrade from a previous CVSS version')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __approximated.name() : __approximated
    })
Namespace.addCategoryObject('typeBinding', u'confidenceType', confidenceType)


# Complex type {http://scap.nist.gov/schema/cvss-v2/0.2}exploitabilityType with content type SIMPLE
class exploitabilityType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://scap.nist.gov/schema/cvss-v2/0.2}exploitabilityType with content type SIMPLE"""
    _TypeDefinition = exploitabilityEnumType
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'exploitabilityType')
    _XSDLocation = pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 267, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is exploitabilityEnumType
    
    # Attribute approximated uses Python identifier approximated
    __approximated = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'approximated'), 'approximated', '__httpscap_nist_govschemacvss_v20_2_exploitabilityType_approximated', pyxb.binding.datatypes.boolean, unicode_default=u'false')
    __approximated._DeclarationLocation = pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 87, 2)
    __approximated._UseLocation = pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 87, 2)
    
    approximated = property(__approximated.value, __approximated.set, None, u'Indicates if the vector has been approximated as the result of an upgrade from a previous CVSS version')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __approximated.name() : __approximated
    })
Namespace.addCategoryObject('typeBinding', u'exploitabilityType', exploitabilityType)


# Complex type {http://scap.nist.gov/schema/cvss-v2/0.2}cvssImpactType with content type ELEMENT_ONLY
class cvssImpactType (cvssType):
    """Complex type {http://scap.nist.gov/schema/cvss-v2/0.2}cvssImpactType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'cvssImpactType')
    _XSDLocation = pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 299, 1)
    _ElementMap = cvssType._ElementMap.copy()
    _AttributeMap = cvssType._AttributeMap.copy()
    # Base type is cvssType
    
    # Element base_metrics ({http://scap.nist.gov/schema/cvss-v2/0.2}base_metrics) inherited from {http://scap.nist.gov/schema/cvss-v2/0.2}cvssType
    
    # Element environmental_metrics ({http://scap.nist.gov/schema/cvss-v2/0.2}environmental_metrics) inherited from {http://scap.nist.gov/schema/cvss-v2/0.2}cvssType
    
    # Element temporal_metrics ({http://scap.nist.gov/schema/cvss-v2/0.2}temporal_metrics) inherited from {http://scap.nist.gov/schema/cvss-v2/0.2}cvssType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'cvssImpactType', cvssImpactType)


# Complex type {http://scap.nist.gov/schema/cvss-v2/0.2}baseMetricsType with content type ELEMENT_ONLY
class baseMetricsType (metricsType):
    """Complex type {http://scap.nist.gov/schema/cvss-v2/0.2}baseMetricsType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'baseMetricsType')
    _XSDLocation = pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 313, 1)
    _ElementMap = metricsType._ElementMap.copy()
    _AttributeMap = metricsType._AttributeMap.copy()
    # Base type is metricsType
    
    # Element {http://scap.nist.gov/schema/cvss-v2/0.2}access-vector uses Python identifier access_vector
    __access_vector = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'access-vector'), 'access_vector', '__httpscap_nist_govschemacvss_v20_2_baseMetricsType_httpscap_nist_govschemacvss_v20_2access_vector', False, pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 32, 3), )

    
    access_vector = property(__access_vector.value, __access_vector.set, None, None)

    
    # Element {http://scap.nist.gov/schema/cvss-v2/0.2}access-complexity uses Python identifier access_complexity
    __access_complexity = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'access-complexity'), 'access_complexity', '__httpscap_nist_govschemacvss_v20_2_baseMetricsType_httpscap_nist_govschemacvss_v20_2access_complexity', False, pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 33, 3), )

    
    access_complexity = property(__access_complexity.value, __access_complexity.set, None, None)

    
    # Element {http://scap.nist.gov/schema/cvss-v2/0.2}authentication uses Python identifier authentication
    __authentication = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'authentication'), 'authentication', '__httpscap_nist_govschemacvss_v20_2_baseMetricsType_httpscap_nist_govschemacvss_v20_2authentication', False, pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 34, 3), )

    
    authentication = property(__authentication.value, __authentication.set, None, None)

    
    # Element {http://scap.nist.gov/schema/cvss-v2/0.2}confidentiality-impact uses Python identifier confidentiality_impact
    __confidentiality_impact = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'confidentiality-impact'), 'confidentiality_impact', '__httpscap_nist_govschemacvss_v20_2_baseMetricsType_httpscap_nist_govschemacvss_v20_2confidentiality_impact', False, pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 35, 3), )

    
    confidentiality_impact = property(__confidentiality_impact.value, __confidentiality_impact.set, None, None)

    
    # Element {http://scap.nist.gov/schema/cvss-v2/0.2}integrity-impact uses Python identifier integrity_impact
    __integrity_impact = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'integrity-impact'), 'integrity_impact', '__httpscap_nist_govschemacvss_v20_2_baseMetricsType_httpscap_nist_govschemacvss_v20_2integrity_impact', False, pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 36, 3), )

    
    integrity_impact = property(__integrity_impact.value, __integrity_impact.set, None, None)

    
    # Element {http://scap.nist.gov/schema/cvss-v2/0.2}availability-impact uses Python identifier availability_impact
    __availability_impact = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'availability-impact'), 'availability_impact', '__httpscap_nist_govschemacvss_v20_2_baseMetricsType_httpscap_nist_govschemacvss_v20_2availability_impact', False, pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 37, 3), )

    
    availability_impact = property(__availability_impact.value, __availability_impact.set, None, None)

    
    # Element {http://scap.nist.gov/schema/cvss-v2/0.2}score uses Python identifier score
    __score = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'score'), 'score', '__httpscap_nist_govschemacvss_v20_2_baseMetricsType_httpscap_nist_govschemacvss_v20_2score', False, pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 317, 5), )

    
    score = property(__score.value, __score.set, None, u'Base severity score assigned to a vulnerability by a source')

    
    # Element {http://scap.nist.gov/schema/cvss-v2/0.2}exploit-subscore uses Python identifier exploit_subscore
    __exploit_subscore = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'exploit-subscore'), 'exploit_subscore', '__httpscap_nist_govschemacvss_v20_2_baseMetricsType_httpscap_nist_govschemacvss_v20_2exploit_subscore', False, pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 322, 5), )

    
    exploit_subscore = property(__exploit_subscore.value, __exploit_subscore.set, None, u'Base exploit sub-score assigned to a vulnerability by a source')

    
    # Element {http://scap.nist.gov/schema/cvss-v2/0.2}impact-subscore uses Python identifier impact_subscore
    __impact_subscore = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'impact-subscore'), 'impact_subscore', '__httpscap_nist_govschemacvss_v20_2_baseMetricsType_httpscap_nist_govschemacvss_v20_2impact_subscore', False, pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 327, 5), )

    
    impact_subscore = property(__impact_subscore.value, __impact_subscore.set, None, u'Base impact sub-score assigned to a vulnerability by a source')

    
    # Element {http://scap.nist.gov/schema/cvss-v2/0.2}source uses Python identifier source
    __source = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'source'), 'source', '__httpscap_nist_govschemacvss_v20_2_baseMetricsType_httpscap_nist_govschemacvss_v20_2source', False, pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 333, 5), )

    
    source = property(__source.value, __source.set, None, u'Data source the vector was obtained from.  Example:  http://nvd.nist.gov or com.symantec.deepsight')

    
    # Element {http://scap.nist.gov/schema/cvss-v2/0.2}generated-on-datetime uses Python identifier generated_on_datetime
    __generated_on_datetime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'generated-on-datetime'), 'generated_on_datetime', '__httpscap_nist_govschemacvss_v20_2_baseMetricsType_httpscap_nist_govschemacvss_v20_2generated_on_datetime', False, pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 338, 5), )

    
    generated_on_datetime = property(__generated_on_datetime.value, __generated_on_datetime.set, None, None)

    
    # Attribute upgraded_from_version inherited from {http://scap.nist.gov/schema/cvss-v2/0.2}metricsType
    _ElementMap.update({
        __access_vector.name() : __access_vector,
        __access_complexity.name() : __access_complexity,
        __authentication.name() : __authentication,
        __confidentiality_impact.name() : __confidentiality_impact,
        __integrity_impact.name() : __integrity_impact,
        __availability_impact.name() : __availability_impact,
        __score.name() : __score,
        __exploit_subscore.name() : __exploit_subscore,
        __impact_subscore.name() : __impact_subscore,
        __source.name() : __source,
        __generated_on_datetime.name() : __generated_on_datetime
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'baseMetricsType', baseMetricsType)


# Complex type {http://scap.nist.gov/schema/cvss-v2/0.2}environmentalMetricsType with content type ELEMENT_ONLY
class environmentalMetricsType (metricsType):
    """Complex type {http://scap.nist.gov/schema/cvss-v2/0.2}environmentalMetricsType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'environmentalMetricsType')
    _XSDLocation = pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 346, 1)
    _ElementMap = metricsType._ElementMap.copy()
    _AttributeMap = metricsType._AttributeMap.copy()
    # Base type is metricsType
    
    # Element {http://scap.nist.gov/schema/cvss-v2/0.2}collateral-damage-potential uses Python identifier collateral_damage_potential
    __collateral_damage_potential = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'collateral-damage-potential'), 'collateral_damage_potential', '__httpscap_nist_govschemacvss_v20_2_environmentalMetricsType_httpscap_nist_govschemacvss_v20_2collateral_damage_potential', False, pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 42, 3), )

    
    collateral_damage_potential = property(__collateral_damage_potential.value, __collateral_damage_potential.set, None, None)

    
    # Element {http://scap.nist.gov/schema/cvss-v2/0.2}target-distribution uses Python identifier target_distribution
    __target_distribution = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'target-distribution'), 'target_distribution', '__httpscap_nist_govschemacvss_v20_2_environmentalMetricsType_httpscap_nist_govschemacvss_v20_2target_distribution', False, pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 43, 3), )

    
    target_distribution = property(__target_distribution.value, __target_distribution.set, None, None)

    
    # Element {http://scap.nist.gov/schema/cvss-v2/0.2}confidentiality-requirement uses Python identifier confidentiality_requirement
    __confidentiality_requirement = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'confidentiality-requirement'), 'confidentiality_requirement', '__httpscap_nist_govschemacvss_v20_2_environmentalMetricsType_httpscap_nist_govschemacvss_v20_2confidentiality_requirement', False, pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 44, 3), )

    
    confidentiality_requirement = property(__confidentiality_requirement.value, __confidentiality_requirement.set, None, None)

    
    # Element {http://scap.nist.gov/schema/cvss-v2/0.2}integrity-requirement uses Python identifier integrity_requirement
    __integrity_requirement = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'integrity-requirement'), 'integrity_requirement', '__httpscap_nist_govschemacvss_v20_2_environmentalMetricsType_httpscap_nist_govschemacvss_v20_2integrity_requirement', False, pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 45, 3), )

    
    integrity_requirement = property(__integrity_requirement.value, __integrity_requirement.set, None, None)

    
    # Element {http://scap.nist.gov/schema/cvss-v2/0.2}availability-requirement uses Python identifier availability_requirement
    __availability_requirement = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'availability-requirement'), 'availability_requirement', '__httpscap_nist_govschemacvss_v20_2_environmentalMetricsType_httpscap_nist_govschemacvss_v20_2availability_requirement', False, pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 46, 3), )

    
    availability_requirement = property(__availability_requirement.value, __availability_requirement.set, None, None)

    
    # Element {http://scap.nist.gov/schema/cvss-v2/0.2}score uses Python identifier score
    __score = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'score'), 'score', '__httpscap_nist_govschemacvss_v20_2_environmentalMetricsType_httpscap_nist_govschemacvss_v20_2score', False, pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 350, 5), )

    
    score = property(__score.value, __score.set, None, None)

    
    # Element {http://scap.nist.gov/schema/cvss-v2/0.2}source uses Python identifier source
    __source = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'source'), 'source', '__httpscap_nist_govschemacvss_v20_2_environmentalMetricsType_httpscap_nist_govschemacvss_v20_2source', False, pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 352, 5), )

    
    source = property(__source.value, __source.set, None, u'Data source the vector was obtained from.  Example:  gov.nist.nvd or com.symantec.deepsight')

    
    # Element {http://scap.nist.gov/schema/cvss-v2/0.2}generated-on-datetime uses Python identifier generated_on_datetime
    __generated_on_datetime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'generated-on-datetime'), 'generated_on_datetime', '__httpscap_nist_govschemacvss_v20_2_environmentalMetricsType_httpscap_nist_govschemacvss_v20_2generated_on_datetime', False, pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 357, 5), )

    
    generated_on_datetime = property(__generated_on_datetime.value, __generated_on_datetime.set, None, None)

    
    # Attribute upgraded_from_version inherited from {http://scap.nist.gov/schema/cvss-v2/0.2}metricsType
    _ElementMap.update({
        __collateral_damage_potential.name() : __collateral_damage_potential,
        __target_distribution.name() : __target_distribution,
        __confidentiality_requirement.name() : __confidentiality_requirement,
        __integrity_requirement.name() : __integrity_requirement,
        __availability_requirement.name() : __availability_requirement,
        __score.name() : __score,
        __source.name() : __source,
        __generated_on_datetime.name() : __generated_on_datetime
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'environmentalMetricsType', environmentalMetricsType)


# Complex type {http://scap.nist.gov/schema/cvss-v2/0.2}temporalMetricsType with content type ELEMENT_ONLY
class temporalMetricsType (metricsType):
    """Complex type {http://scap.nist.gov/schema/cvss-v2/0.2}temporalMetricsType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'temporalMetricsType')
    _XSDLocation = pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 365, 1)
    _ElementMap = metricsType._ElementMap.copy()
    _AttributeMap = metricsType._AttributeMap.copy()
    # Base type is metricsType
    
    # Element {http://scap.nist.gov/schema/cvss-v2/0.2}exploitability uses Python identifier exploitability
    __exploitability = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'exploitability'), 'exploitability', '__httpscap_nist_govschemacvss_v20_2_temporalMetricsType_httpscap_nist_govschemacvss_v20_2exploitability', False, pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 51, 3), )

    
    exploitability = property(__exploitability.value, __exploitability.set, None, None)

    
    # Element {http://scap.nist.gov/schema/cvss-v2/0.2}remediation-level uses Python identifier remediation_level
    __remediation_level = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'remediation-level'), 'remediation_level', '__httpscap_nist_govschemacvss_v20_2_temporalMetricsType_httpscap_nist_govschemacvss_v20_2remediation_level', False, pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 52, 3), )

    
    remediation_level = property(__remediation_level.value, __remediation_level.set, None, None)

    
    # Element {http://scap.nist.gov/schema/cvss-v2/0.2}report-confidence uses Python identifier report_confidence
    __report_confidence = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'report-confidence'), 'report_confidence', '__httpscap_nist_govschemacvss_v20_2_temporalMetricsType_httpscap_nist_govschemacvss_v20_2report_confidence', False, pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 53, 3), )

    
    report_confidence = property(__report_confidence.value, __report_confidence.set, None, None)

    
    # Element {http://scap.nist.gov/schema/cvss-v2/0.2}score uses Python identifier score
    __score = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'score'), 'score', '__httpscap_nist_govschemacvss_v20_2_temporalMetricsType_httpscap_nist_govschemacvss_v20_2score', False, pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 369, 5), )

    
    score = property(__score.value, __score.set, None, u'The temporal score is the temporal multiplier times the base score.')

    
    # Element {http://scap.nist.gov/schema/cvss-v2/0.2}temporal-multiplier uses Python identifier temporal_multiplier
    __temporal_multiplier = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'temporal-multiplier'), 'temporal_multiplier', '__httpscap_nist_govschemacvss_v20_2_temporalMetricsType_httpscap_nist_govschemacvss_v20_2temporal_multiplier', False, pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 374, 5), )

    
    temporal_multiplier = property(__temporal_multiplier.value, __temporal_multiplier.set, None, u'The temporal multiplier is a number between zero and one.  Reference the CVSS standard for computation.')

    
    # Element {http://scap.nist.gov/schema/cvss-v2/0.2}source uses Python identifier source
    __source = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'source'), 'source', '__httpscap_nist_govschemacvss_v20_2_temporalMetricsType_httpscap_nist_govschemacvss_v20_2source', False, pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 380, 5), )

    
    source = property(__source.value, __source.set, None, None)

    
    # Element {http://scap.nist.gov/schema/cvss-v2/0.2}generated-on-datetime uses Python identifier generated_on_datetime
    __generated_on_datetime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'generated-on-datetime'), 'generated_on_datetime', '__httpscap_nist_govschemacvss_v20_2_temporalMetricsType_httpscap_nist_govschemacvss_v20_2generated_on_datetime', False, pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 381, 5), )

    
    generated_on_datetime = property(__generated_on_datetime.value, __generated_on_datetime.set, None, None)

    
    # Attribute upgraded_from_version inherited from {http://scap.nist.gov/schema/cvss-v2/0.2}metricsType
    _ElementMap.update({
        __exploitability.name() : __exploitability,
        __remediation_level.name() : __remediation_level,
        __report_confidence.name() : __report_confidence,
        __score.name() : __score,
        __temporal_multiplier.name() : __temporal_multiplier,
        __source.name() : __source,
        __generated_on_datetime.name() : __generated_on_datetime
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'temporalMetricsType', temporalMetricsType)




cvssType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'base_metrics'), baseMetricsType, scope=cvssType, location=pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 293, 3)))

cvssType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'environmental_metrics'), environmentalMetricsType, scope=cvssType, location=pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 294, 3)))

cvssType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'temporal_metrics'), temporalMetricsType, scope=cvssType, location=pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 295, 3)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 293, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 294, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 295, 3))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(cvssType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'base_metrics')), pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 293, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(cvssType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'environmental_metrics')), pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 294, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(cvssType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'temporal_metrics')), pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 295, 3))
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
cvssType._Automaton = _BuildAutomaton()




def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 304, 5))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 305, 5))
    counters.add(cc_1)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(cvssImpactType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'base_metrics')), pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 303, 5))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(cvssImpactType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'environmental_metrics')), pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 304, 5))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(cvssImpactType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'temporal_metrics')), pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 305, 5))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
cvssImpactType._Automaton = _BuildAutomaton_()




baseMetricsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'access-vector'), accessVectorType, scope=baseMetricsType, location=pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 32, 3)))

baseMetricsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'access-complexity'), accessComplexityType, scope=baseMetricsType, location=pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 33, 3)))

baseMetricsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'authentication'), authenticationType, scope=baseMetricsType, location=pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 34, 3)))

baseMetricsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'confidentiality-impact'), ciaType, scope=baseMetricsType, location=pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 35, 3)))

baseMetricsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'integrity-impact'), ciaType, scope=baseMetricsType, location=pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 36, 3)))

baseMetricsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'availability-impact'), ciaType, scope=baseMetricsType, location=pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 37, 3)))

baseMetricsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'score'), zeroToTenDecimalType, scope=baseMetricsType, documentation=u'Base severity score assigned to a vulnerability by a source', location=pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 317, 5)))

baseMetricsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'exploit-subscore'), zeroToTenDecimalType, scope=baseMetricsType, documentation=u'Base exploit sub-score assigned to a vulnerability by a source', location=pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 322, 5)))

baseMetricsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'impact-subscore'), zeroToTenDecimalType, scope=baseMetricsType, documentation=u'Base impact sub-score assigned to a vulnerability by a source', location=pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 327, 5)))

baseMetricsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'source'), pyxb.binding.datatypes.anyURI, scope=baseMetricsType, documentation=u'Data source the vector was obtained from.  Example:  http://nvd.nist.gov or com.symantec.deepsight', location=pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 333, 5)))

baseMetricsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'generated-on-datetime'), pyxb.binding.datatypes.dateTime, scope=baseMetricsType, location=pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 338, 5)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 317, 5))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 322, 5))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 327, 5))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 32, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 33, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 34, 3))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 35, 3))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 36, 3))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 37, 3))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 338, 5))
    counters.add(cc_9)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(baseMetricsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'score')), pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 317, 5))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(baseMetricsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'exploit-subscore')), pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 322, 5))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(baseMetricsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'impact-subscore')), pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 327, 5))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(baseMetricsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'access-vector')), pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 32, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(baseMetricsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'access-complexity')), pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 33, 3))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(baseMetricsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'authentication')), pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 34, 3))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(baseMetricsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'confidentiality-impact')), pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 35, 3))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(baseMetricsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'integrity-impact')), pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 36, 3))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(baseMetricsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'availability-impact')), pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 37, 3))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(baseMetricsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'source')), pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 333, 5))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(baseMetricsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'generated-on-datetime')), pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 338, 5))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
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
    transitions.append(fac.Transition(st_10, [
         ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, True) ]))
    st_10._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
baseMetricsType._Automaton = _BuildAutomaton_2()




environmentalMetricsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'collateral-damage-potential'), collateralDamagePotentialType, scope=environmentalMetricsType, location=pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 42, 3)))

environmentalMetricsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'target-distribution'), targetDistributionType, scope=environmentalMetricsType, location=pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 43, 3)))

environmentalMetricsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'confidentiality-requirement'), ciaRequirementType, scope=environmentalMetricsType, location=pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 44, 3)))

environmentalMetricsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'integrity-requirement'), ciaRequirementType, scope=environmentalMetricsType, location=pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 45, 3)))

environmentalMetricsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'availability-requirement'), ciaRequirementType, scope=environmentalMetricsType, location=pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 46, 3)))

environmentalMetricsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'score'), zeroToTenDecimalType, scope=environmentalMetricsType, location=pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 350, 5)))

environmentalMetricsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'source'), pyxb.binding.datatypes.anyURI, scope=environmentalMetricsType, documentation=u'Data source the vector was obtained from.  Example:  gov.nist.nvd or com.symantec.deepsight', location=pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 352, 5)))

environmentalMetricsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'generated-on-datetime'), pyxb.binding.datatypes.dateTime, scope=environmentalMetricsType, location=pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 357, 5)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 350, 5))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 42, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 43, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 44, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 45, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 46, 3))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 357, 5))
    counters.add(cc_6)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(environmentalMetricsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'score')), pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 350, 5))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(environmentalMetricsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'collateral-damage-potential')), pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 42, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(environmentalMetricsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'target-distribution')), pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 43, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(environmentalMetricsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'confidentiality-requirement')), pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 44, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(environmentalMetricsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'integrity-requirement')), pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 45, 3))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(environmentalMetricsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'availability-requirement')), pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 46, 3))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(environmentalMetricsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'source')), pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 352, 5))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(environmentalMetricsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'generated-on-datetime')), pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 357, 5))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
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
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, True) ]))
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
environmentalMetricsType._Automaton = _BuildAutomaton_3()




temporalMetricsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'exploitability'), exploitabilityType, scope=temporalMetricsType, location=pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 51, 3)))

temporalMetricsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'remediation-level'), remediationLevelType, scope=temporalMetricsType, location=pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 52, 3)))

temporalMetricsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'report-confidence'), confidenceType, scope=temporalMetricsType, location=pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 53, 3)))

temporalMetricsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'score'), zeroToTenDecimalType, scope=temporalMetricsType, documentation=u'The temporal score is the temporal multiplier times the base score.', location=pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 369, 5)))

temporalMetricsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'temporal-multiplier'), pyxb.binding.datatypes.decimal, scope=temporalMetricsType, documentation=u'The temporal multiplier is a number between zero and one.  Reference the CVSS standard for computation.', location=pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 374, 5)))

temporalMetricsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'source'), pyxb.binding.datatypes.anyURI, scope=temporalMetricsType, location=pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 380, 5)))

temporalMetricsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'generated-on-datetime'), pyxb.binding.datatypes.dateTime, scope=temporalMetricsType, location=pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 381, 5)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 369, 5))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 374, 5))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 51, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 52, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 53, 3))
    counters.add(cc_4)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(temporalMetricsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'score')), pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 369, 5))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(temporalMetricsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'temporal-multiplier')), pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 374, 5))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(temporalMetricsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'exploitability')), pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 51, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(temporalMetricsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'remediation-level')), pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 52, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(temporalMetricsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'report-confidence')), pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 53, 3))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(temporalMetricsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'source')), pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 380, 5))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(temporalMetricsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'generated-on-datetime')), pyxb.utils.utility.Location(u'/Users/espen/Sources/nvd/schema/cvss-v2_0.2.xsd', 381, 5))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
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
    transitions.append(fac.Transition(st_6, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
temporalMetricsType._Automaton = _BuildAutomaton_4()

