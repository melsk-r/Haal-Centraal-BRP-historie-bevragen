# coding: utf-8

"""
    BRP historie bevragen

    API voor het zoeken en raadplegen van historische verblijfplaatsen, partners, nationaliteiten en verblijfstitels uit de BRP (inclusief de RNI).  Zie de [Functionele documentatie](https://github.com/VNG-Realisatie/Haal-Centraal-BRP-historie-bevragen/tree/v1.0.0/features) voor nadere toelichting.   # noqa: E501

    The version of the OpenAPI document: 0.0.1 (develop)
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class VerblijfplaatsAllOf(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'adresseerbaar_object_identificatie': 'str',
        'aanduiding_bij_huisnummer': 'AanduidingBijHuisnummerEnum',
        'nummeraanduiding_identificatie': 'str',
        'functie_adres': 'SoortAdresEnum',
        'indicatie_vestiging_vanuit_buitenland': 'bool',
        'locatiebeschrijving': 'str',
        'korte_naam': 'str',
        'vanuit_vertrokken_onbekend_waarheen': 'bool',
        'datum_aanvang_adreshouding': 'DatumOnvolledig',
        'datum_ingang_geldigheid': 'DatumOnvolledig',
        'datum_inschrijving_in_gemeente': 'DatumOnvolledig',
        'datum_vestiging_in_nederland': 'DatumOnvolledig',
        'gemeente_van_inschrijving': 'Waardetabel',
        'land_vanwaar_ingeschreven': 'Waardetabel',
        'adresregel1': 'str',
        'adresregel2': 'str',
        'adresregel3': 'str',
        'vertrokken_onbekend_waarheen': 'bool',
        'land': 'Waardetabel',
        'in_onderzoek': 'VerblijfplaatsInOnderzoek'
    }

    attribute_map = {
        'adresseerbaar_object_identificatie': 'adresseerbaarObjectIdentificatie',
        'aanduiding_bij_huisnummer': 'aanduidingBijHuisnummer',
        'nummeraanduiding_identificatie': 'nummeraanduidingIdentificatie',
        'functie_adres': 'functieAdres',
        'indicatie_vestiging_vanuit_buitenland': 'indicatieVestigingVanuitBuitenland',
        'locatiebeschrijving': 'locatiebeschrijving',
        'korte_naam': 'korteNaam',
        'vanuit_vertrokken_onbekend_waarheen': 'vanuitVertrokkenOnbekendWaarheen',
        'datum_aanvang_adreshouding': 'datumAanvangAdreshouding',
        'datum_ingang_geldigheid': 'datumIngangGeldigheid',
        'datum_inschrijving_in_gemeente': 'datumInschrijvingInGemeente',
        'datum_vestiging_in_nederland': 'datumVestigingInNederland',
        'gemeente_van_inschrijving': 'gemeenteVanInschrijving',
        'land_vanwaar_ingeschreven': 'landVanwaarIngeschreven',
        'adresregel1': 'adresregel1',
        'adresregel2': 'adresregel2',
        'adresregel3': 'adresregel3',
        'vertrokken_onbekend_waarheen': 'vertrokkenOnbekendWaarheen',
        'land': 'land',
        'in_onderzoek': 'inOnderzoek'
    }

    def __init__(self, adresseerbaar_object_identificatie=None, aanduiding_bij_huisnummer=None, nummeraanduiding_identificatie=None, functie_adres=None, indicatie_vestiging_vanuit_buitenland=None, locatiebeschrijving=None, korte_naam=None, vanuit_vertrokken_onbekend_waarheen=None, datum_aanvang_adreshouding=None, datum_ingang_geldigheid=None, datum_inschrijving_in_gemeente=None, datum_vestiging_in_nederland=None, gemeente_van_inschrijving=None, land_vanwaar_ingeschreven=None, adresregel1=None, adresregel2=None, adresregel3=None, vertrokken_onbekend_waarheen=None, land=None, in_onderzoek=None, local_vars_configuration=None):  # noqa: E501
        """VerblijfplaatsAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._adresseerbaar_object_identificatie = None
        self._aanduiding_bij_huisnummer = None
        self._nummeraanduiding_identificatie = None
        self._functie_adres = None
        self._indicatie_vestiging_vanuit_buitenland = None
        self._locatiebeschrijving = None
        self._korte_naam = None
        self._vanuit_vertrokken_onbekend_waarheen = None
        self._datum_aanvang_adreshouding = None
        self._datum_ingang_geldigheid = None
        self._datum_inschrijving_in_gemeente = None
        self._datum_vestiging_in_nederland = None
        self._gemeente_van_inschrijving = None
        self._land_vanwaar_ingeschreven = None
        self._adresregel1 = None
        self._adresregel2 = None
        self._adresregel3 = None
        self._vertrokken_onbekend_waarheen = None
        self._land = None
        self._in_onderzoek = None
        self.discriminator = None

        if adresseerbaar_object_identificatie is not None:
            self.adresseerbaar_object_identificatie = adresseerbaar_object_identificatie
        if aanduiding_bij_huisnummer is not None:
            self.aanduiding_bij_huisnummer = aanduiding_bij_huisnummer
        if nummeraanduiding_identificatie is not None:
            self.nummeraanduiding_identificatie = nummeraanduiding_identificatie
        if functie_adres is not None:
            self.functie_adres = functie_adres
        if indicatie_vestiging_vanuit_buitenland is not None:
            self.indicatie_vestiging_vanuit_buitenland = indicatie_vestiging_vanuit_buitenland
        if locatiebeschrijving is not None:
            self.locatiebeschrijving = locatiebeschrijving
        if korte_naam is not None:
            self.korte_naam = korte_naam
        if vanuit_vertrokken_onbekend_waarheen is not None:
            self.vanuit_vertrokken_onbekend_waarheen = vanuit_vertrokken_onbekend_waarheen
        if datum_aanvang_adreshouding is not None:
            self.datum_aanvang_adreshouding = datum_aanvang_adreshouding
        if datum_ingang_geldigheid is not None:
            self.datum_ingang_geldigheid = datum_ingang_geldigheid
        if datum_inschrijving_in_gemeente is not None:
            self.datum_inschrijving_in_gemeente = datum_inschrijving_in_gemeente
        if datum_vestiging_in_nederland is not None:
            self.datum_vestiging_in_nederland = datum_vestiging_in_nederland
        if gemeente_van_inschrijving is not None:
            self.gemeente_van_inschrijving = gemeente_van_inschrijving
        if land_vanwaar_ingeschreven is not None:
            self.land_vanwaar_ingeschreven = land_vanwaar_ingeschreven
        if adresregel1 is not None:
            self.adresregel1 = adresregel1
        if adresregel2 is not None:
            self.adresregel2 = adresregel2
        if adresregel3 is not None:
            self.adresregel3 = adresregel3
        if vertrokken_onbekend_waarheen is not None:
            self.vertrokken_onbekend_waarheen = vertrokken_onbekend_waarheen
        if land is not None:
            self.land = land
        if in_onderzoek is not None:
            self.in_onderzoek = in_onderzoek

    @property
    def adresseerbaar_object_identificatie(self):
        """Gets the adresseerbaar_object_identificatie of this VerblijfplaatsAllOf.  # noqa: E501

        De verblijfplaats van de persoon kan een ligplaats, een standplaats of een verblijfsobject zijn.   # noqa: E501

        :return: The adresseerbaar_object_identificatie of this VerblijfplaatsAllOf.  # noqa: E501
        :rtype: str
        """
        return self._adresseerbaar_object_identificatie

    @adresseerbaar_object_identificatie.setter
    def adresseerbaar_object_identificatie(self, adresseerbaar_object_identificatie):
        """Sets the adresseerbaar_object_identificatie of this VerblijfplaatsAllOf.

        De verblijfplaats van de persoon kan een ligplaats, een standplaats of een verblijfsobject zijn.   # noqa: E501

        :param adresseerbaar_object_identificatie: The adresseerbaar_object_identificatie of this VerblijfplaatsAllOf.  # noqa: E501
        :type: str
        """

        self._adresseerbaar_object_identificatie = adresseerbaar_object_identificatie

    @property
    def aanduiding_bij_huisnummer(self):
        """Gets the aanduiding_bij_huisnummer of this VerblijfplaatsAllOf.  # noqa: E501


        :return: The aanduiding_bij_huisnummer of this VerblijfplaatsAllOf.  # noqa: E501
        :rtype: AanduidingBijHuisnummerEnum
        """
        return self._aanduiding_bij_huisnummer

    @aanduiding_bij_huisnummer.setter
    def aanduiding_bij_huisnummer(self, aanduiding_bij_huisnummer):
        """Sets the aanduiding_bij_huisnummer of this VerblijfplaatsAllOf.


        :param aanduiding_bij_huisnummer: The aanduiding_bij_huisnummer of this VerblijfplaatsAllOf.  # noqa: E501
        :type: AanduidingBijHuisnummerEnum
        """

        self._aanduiding_bij_huisnummer = aanduiding_bij_huisnummer

    @property
    def nummeraanduiding_identificatie(self):
        """Gets the nummeraanduiding_identificatie of this VerblijfplaatsAllOf.  # noqa: E501

        Unieke identificatie van een nummeraanduiding (en het bijbehorende adres) in de BAG.   # noqa: E501

        :return: The nummeraanduiding_identificatie of this VerblijfplaatsAllOf.  # noqa: E501
        :rtype: str
        """
        return self._nummeraanduiding_identificatie

    @nummeraanduiding_identificatie.setter
    def nummeraanduiding_identificatie(self, nummeraanduiding_identificatie):
        """Sets the nummeraanduiding_identificatie of this VerblijfplaatsAllOf.

        Unieke identificatie van een nummeraanduiding (en het bijbehorende adres) in de BAG.   # noqa: E501

        :param nummeraanduiding_identificatie: The nummeraanduiding_identificatie of this VerblijfplaatsAllOf.  # noqa: E501
        :type: str
        """

        self._nummeraanduiding_identificatie = nummeraanduiding_identificatie

    @property
    def functie_adres(self):
        """Gets the functie_adres of this VerblijfplaatsAllOf.  # noqa: E501


        :return: The functie_adres of this VerblijfplaatsAllOf.  # noqa: E501
        :rtype: SoortAdresEnum
        """
        return self._functie_adres

    @functie_adres.setter
    def functie_adres(self, functie_adres):
        """Sets the functie_adres of this VerblijfplaatsAllOf.


        :param functie_adres: The functie_adres of this VerblijfplaatsAllOf.  # noqa: E501
        :type: SoortAdresEnum
        """

        self._functie_adres = functie_adres

    @property
    def indicatie_vestiging_vanuit_buitenland(self):
        """Gets the indicatie_vestiging_vanuit_buitenland of this VerblijfplaatsAllOf.  # noqa: E501

        Geeft aan dat de ingeschreven persoon zich vanuit het buitenland heeft ingeschreven.   # noqa: E501

        :return: The indicatie_vestiging_vanuit_buitenland of this VerblijfplaatsAllOf.  # noqa: E501
        :rtype: bool
        """
        return self._indicatie_vestiging_vanuit_buitenland

    @indicatie_vestiging_vanuit_buitenland.setter
    def indicatie_vestiging_vanuit_buitenland(self, indicatie_vestiging_vanuit_buitenland):
        """Sets the indicatie_vestiging_vanuit_buitenland of this VerblijfplaatsAllOf.

        Geeft aan dat de ingeschreven persoon zich vanuit het buitenland heeft ingeschreven.   # noqa: E501

        :param indicatie_vestiging_vanuit_buitenland: The indicatie_vestiging_vanuit_buitenland of this VerblijfplaatsAllOf.  # noqa: E501
        :type: bool
        """

        self._indicatie_vestiging_vanuit_buitenland = indicatie_vestiging_vanuit_buitenland

    @property
    def locatiebeschrijving(self):
        """Gets the locatiebeschrijving of this VerblijfplaatsAllOf.  # noqa: E501

        Omschrijving van de ligging van een verblijfsobject, standplaats of ligplaats.   # noqa: E501

        :return: The locatiebeschrijving of this VerblijfplaatsAllOf.  # noqa: E501
        :rtype: str
        """
        return self._locatiebeschrijving

    @locatiebeschrijving.setter
    def locatiebeschrijving(self, locatiebeschrijving):
        """Sets the locatiebeschrijving of this VerblijfplaatsAllOf.

        Omschrijving van de ligging van een verblijfsobject, standplaats of ligplaats.   # noqa: E501

        :param locatiebeschrijving: The locatiebeschrijving of this VerblijfplaatsAllOf.  # noqa: E501
        :type: str
        """

        self._locatiebeschrijving = locatiebeschrijving

    @property
    def korte_naam(self):
        """Gets the korte_naam of this VerblijfplaatsAllOf.  # noqa: E501

        De officiële openbareruimtenaam uit de Basisregistratie Gebouwen en Adressen (BAG) of een verkorte versie.   # noqa: E501

        :return: The korte_naam of this VerblijfplaatsAllOf.  # noqa: E501
        :rtype: str
        """
        return self._korte_naam

    @korte_naam.setter
    def korte_naam(self, korte_naam):
        """Sets the korte_naam of this VerblijfplaatsAllOf.

        De officiële openbareruimtenaam uit de Basisregistratie Gebouwen en Adressen (BAG) of een verkorte versie.   # noqa: E501

        :param korte_naam: The korte_naam of this VerblijfplaatsAllOf.  # noqa: E501
        :type: str
        """

        self._korte_naam = korte_naam

    @property
    def vanuit_vertrokken_onbekend_waarheen(self):
        """Gets the vanuit_vertrokken_onbekend_waarheen of this VerblijfplaatsAllOf.  # noqa: E501

        Geeft aan dat de persoon is teruggekeerd uit een situatie van 'vertrokken onbekend waarheen.'   # noqa: E501

        :return: The vanuit_vertrokken_onbekend_waarheen of this VerblijfplaatsAllOf.  # noqa: E501
        :rtype: bool
        """
        return self._vanuit_vertrokken_onbekend_waarheen

    @vanuit_vertrokken_onbekend_waarheen.setter
    def vanuit_vertrokken_onbekend_waarheen(self, vanuit_vertrokken_onbekend_waarheen):
        """Sets the vanuit_vertrokken_onbekend_waarheen of this VerblijfplaatsAllOf.

        Geeft aan dat de persoon is teruggekeerd uit een situatie van 'vertrokken onbekend waarheen.'   # noqa: E501

        :param vanuit_vertrokken_onbekend_waarheen: The vanuit_vertrokken_onbekend_waarheen of this VerblijfplaatsAllOf.  # noqa: E501
        :type: bool
        """

        self._vanuit_vertrokken_onbekend_waarheen = vanuit_vertrokken_onbekend_waarheen

    @property
    def datum_aanvang_adreshouding(self):
        """Gets the datum_aanvang_adreshouding of this VerblijfplaatsAllOf.  # noqa: E501


        :return: The datum_aanvang_adreshouding of this VerblijfplaatsAllOf.  # noqa: E501
        :rtype: DatumOnvolledig
        """
        return self._datum_aanvang_adreshouding

    @datum_aanvang_adreshouding.setter
    def datum_aanvang_adreshouding(self, datum_aanvang_adreshouding):
        """Sets the datum_aanvang_adreshouding of this VerblijfplaatsAllOf.


        :param datum_aanvang_adreshouding: The datum_aanvang_adreshouding of this VerblijfplaatsAllOf.  # noqa: E501
        :type: DatumOnvolledig
        """

        self._datum_aanvang_adreshouding = datum_aanvang_adreshouding

    @property
    def datum_ingang_geldigheid(self):
        """Gets the datum_ingang_geldigheid of this VerblijfplaatsAllOf.  # noqa: E501


        :return: The datum_ingang_geldigheid of this VerblijfplaatsAllOf.  # noqa: E501
        :rtype: DatumOnvolledig
        """
        return self._datum_ingang_geldigheid

    @datum_ingang_geldigheid.setter
    def datum_ingang_geldigheid(self, datum_ingang_geldigheid):
        """Sets the datum_ingang_geldigheid of this VerblijfplaatsAllOf.


        :param datum_ingang_geldigheid: The datum_ingang_geldigheid of this VerblijfplaatsAllOf.  # noqa: E501
        :type: DatumOnvolledig
        """

        self._datum_ingang_geldigheid = datum_ingang_geldigheid

    @property
    def datum_inschrijving_in_gemeente(self):
        """Gets the datum_inschrijving_in_gemeente of this VerblijfplaatsAllOf.  # noqa: E501


        :return: The datum_inschrijving_in_gemeente of this VerblijfplaatsAllOf.  # noqa: E501
        :rtype: DatumOnvolledig
        """
        return self._datum_inschrijving_in_gemeente

    @datum_inschrijving_in_gemeente.setter
    def datum_inschrijving_in_gemeente(self, datum_inschrijving_in_gemeente):
        """Sets the datum_inschrijving_in_gemeente of this VerblijfplaatsAllOf.


        :param datum_inschrijving_in_gemeente: The datum_inschrijving_in_gemeente of this VerblijfplaatsAllOf.  # noqa: E501
        :type: DatumOnvolledig
        """

        self._datum_inschrijving_in_gemeente = datum_inschrijving_in_gemeente

    @property
    def datum_vestiging_in_nederland(self):
        """Gets the datum_vestiging_in_nederland of this VerblijfplaatsAllOf.  # noqa: E501


        :return: The datum_vestiging_in_nederland of this VerblijfplaatsAllOf.  # noqa: E501
        :rtype: DatumOnvolledig
        """
        return self._datum_vestiging_in_nederland

    @datum_vestiging_in_nederland.setter
    def datum_vestiging_in_nederland(self, datum_vestiging_in_nederland):
        """Sets the datum_vestiging_in_nederland of this VerblijfplaatsAllOf.


        :param datum_vestiging_in_nederland: The datum_vestiging_in_nederland of this VerblijfplaatsAllOf.  # noqa: E501
        :type: DatumOnvolledig
        """

        self._datum_vestiging_in_nederland = datum_vestiging_in_nederland

    @property
    def gemeente_van_inschrijving(self):
        """Gets the gemeente_van_inschrijving of this VerblijfplaatsAllOf.  # noqa: E501


        :return: The gemeente_van_inschrijving of this VerblijfplaatsAllOf.  # noqa: E501
        :rtype: Waardetabel
        """
        return self._gemeente_van_inschrijving

    @gemeente_van_inschrijving.setter
    def gemeente_van_inschrijving(self, gemeente_van_inschrijving):
        """Sets the gemeente_van_inschrijving of this VerblijfplaatsAllOf.


        :param gemeente_van_inschrijving: The gemeente_van_inschrijving of this VerblijfplaatsAllOf.  # noqa: E501
        :type: Waardetabel
        """

        self._gemeente_van_inschrijving = gemeente_van_inschrijving

    @property
    def land_vanwaar_ingeschreven(self):
        """Gets the land_vanwaar_ingeschreven of this VerblijfplaatsAllOf.  # noqa: E501


        :return: The land_vanwaar_ingeschreven of this VerblijfplaatsAllOf.  # noqa: E501
        :rtype: Waardetabel
        """
        return self._land_vanwaar_ingeschreven

    @land_vanwaar_ingeschreven.setter
    def land_vanwaar_ingeschreven(self, land_vanwaar_ingeschreven):
        """Sets the land_vanwaar_ingeschreven of this VerblijfplaatsAllOf.


        :param land_vanwaar_ingeschreven: The land_vanwaar_ingeschreven of this VerblijfplaatsAllOf.  # noqa: E501
        :type: Waardetabel
        """

        self._land_vanwaar_ingeschreven = land_vanwaar_ingeschreven

    @property
    def adresregel1(self):
        """Gets the adresregel1 of this VerblijfplaatsAllOf.  # noqa: E501

        Het eerste deel van een adres is een combinatie van de straat en huisnummer.   # noqa: E501

        :return: The adresregel1 of this VerblijfplaatsAllOf.  # noqa: E501
        :rtype: str
        """
        return self._adresregel1

    @adresregel1.setter
    def adresregel1(self, adresregel1):
        """Sets the adresregel1 of this VerblijfplaatsAllOf.

        Het eerste deel van een adres is een combinatie van de straat en huisnummer.   # noqa: E501

        :param adresregel1: The adresregel1 of this VerblijfplaatsAllOf.  # noqa: E501
        :type: str
        """

        self._adresregel1 = adresregel1

    @property
    def adresregel2(self):
        """Gets the adresregel2 of this VerblijfplaatsAllOf.  # noqa: E501

        Het tweede deel van een adres is een combinatie van woonplaats eventueel in combinatie met de postcode.   # noqa: E501

        :return: The adresregel2 of this VerblijfplaatsAllOf.  # noqa: E501
        :rtype: str
        """
        return self._adresregel2

    @adresregel2.setter
    def adresregel2(self, adresregel2):
        """Sets the adresregel2 of this VerblijfplaatsAllOf.

        Het tweede deel van een adres is een combinatie van woonplaats eventueel in combinatie met de postcode.   # noqa: E501

        :param adresregel2: The adresregel2 of this VerblijfplaatsAllOf.  # noqa: E501
        :type: str
        """

        self._adresregel2 = adresregel2

    @property
    def adresregel3(self):
        """Gets the adresregel3 of this VerblijfplaatsAllOf.  # noqa: E501

        Het derde deel van een adres is optioneel. Het gaat om een of meer geografische gebieden van het adres in het buitenland.   # noqa: E501

        :return: The adresregel3 of this VerblijfplaatsAllOf.  # noqa: E501
        :rtype: str
        """
        return self._adresregel3

    @adresregel3.setter
    def adresregel3(self, adresregel3):
        """Sets the adresregel3 of this VerblijfplaatsAllOf.

        Het derde deel van een adres is optioneel. Het gaat om een of meer geografische gebieden van het adres in het buitenland.   # noqa: E501

        :param adresregel3: The adresregel3 of this VerblijfplaatsAllOf.  # noqa: E501
        :type: str
        """

        self._adresregel3 = adresregel3

    @property
    def vertrokken_onbekend_waarheen(self):
        """Gets the vertrokken_onbekend_waarheen of this VerblijfplaatsAllOf.  # noqa: E501

        Indicatie dat de ingeschreven persoon is vertrokken naar het buitenland, maar dat niet bekend is waar naar toe.   # noqa: E501

        :return: The vertrokken_onbekend_waarheen of this VerblijfplaatsAllOf.  # noqa: E501
        :rtype: bool
        """
        return self._vertrokken_onbekend_waarheen

    @vertrokken_onbekend_waarheen.setter
    def vertrokken_onbekend_waarheen(self, vertrokken_onbekend_waarheen):
        """Sets the vertrokken_onbekend_waarheen of this VerblijfplaatsAllOf.

        Indicatie dat de ingeschreven persoon is vertrokken naar het buitenland, maar dat niet bekend is waar naar toe.   # noqa: E501

        :param vertrokken_onbekend_waarheen: The vertrokken_onbekend_waarheen of this VerblijfplaatsAllOf.  # noqa: E501
        :type: bool
        """

        self._vertrokken_onbekend_waarheen = vertrokken_onbekend_waarheen

    @property
    def land(self):
        """Gets the land of this VerblijfplaatsAllOf.  # noqa: E501


        :return: The land of this VerblijfplaatsAllOf.  # noqa: E501
        :rtype: Waardetabel
        """
        return self._land

    @land.setter
    def land(self, land):
        """Sets the land of this VerblijfplaatsAllOf.


        :param land: The land of this VerblijfplaatsAllOf.  # noqa: E501
        :type: Waardetabel
        """

        self._land = land

    @property
    def in_onderzoek(self):
        """Gets the in_onderzoek of this VerblijfplaatsAllOf.  # noqa: E501


        :return: The in_onderzoek of this VerblijfplaatsAllOf.  # noqa: E501
        :rtype: VerblijfplaatsInOnderzoek
        """
        return self._in_onderzoek

    @in_onderzoek.setter
    def in_onderzoek(self, in_onderzoek):
        """Sets the in_onderzoek of this VerblijfplaatsAllOf.


        :param in_onderzoek: The in_onderzoek of this VerblijfplaatsAllOf.  # noqa: E501
        :type: VerblijfplaatsInOnderzoek
        """

        self._in_onderzoek = in_onderzoek

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, VerblijfplaatsAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VerblijfplaatsAllOf):
            return True

        return self.to_dict() != other.to_dict()
