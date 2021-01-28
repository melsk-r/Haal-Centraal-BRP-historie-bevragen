/*
 * BRP historie bevragen
 *
 * API voor het zoeken en raadplegen van historische verblijfplaatsen, partners, nationaliteiten en verblijfstitels uit de BRP (inclusief de RNI).  Zie de [Functionele documentatie](https://github.com/VNG-Realisatie/Haal-Centraal-BRP-historie-bevragen/tree/v1.0.0/features) voor nadere toelichting. 
 *
 * The version of the OpenAPI document: 0.0.1 (develop)
 * Generated by: https://github.com/openapitools/openapi-generator.git
 */


using System;
using System.Collections;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Linq;
using System.IO;
using System.Runtime.Serialization;
using System.Text;
using System.Text.RegularExpressions;
using Newtonsoft.Json;
using Newtonsoft.Json.Converters;
using Newtonsoft.Json.Linq;
using System.ComponentModel.DataAnnotations;
using OpenAPIDateConverter = Org.OpenAPITools.Client.OpenAPIDateConverter;

namespace Org.OpenAPITools.Model
{
    /// <summary>
    /// Nationaliteithistorie
    /// </summary>
    [DataContract(Name = "Nationaliteithistorie")]
    public partial class Nationaliteithistorie : IEquatable<Nationaliteithistorie>, IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="Nationaliteithistorie" /> class.
        /// </summary>
        /// <param name="aanduidingBijzonderNederlanderschap">aanduidingBijzonderNederlanderschap.</param>
        /// <param name="datumIngangGeldigheid">datumIngangGeldigheid.</param>
        /// <param name="nationaliteit">nationaliteit.</param>
        /// <param name="redenOpname">redenOpname.</param>
        /// <param name="inOnderzoek">inOnderzoek.</param>
        /// <param name="geheimhoudingPersoonsgegevens">Gegevens mogen niet worden verstrekt aan derden / maatschappelijke instellingen. .</param>
        /// <param name="datumTot">datumTot.</param>
        /// <param name="redenBeeindigen">redenBeeindigen.</param>
        /// <param name="indicatieNationaliteitBeeindigd">Geeft aan dat de nationaliteit beëindigd is. .</param>
        public Nationaliteithistorie(AanduidingBijzonderNederlanderschapEnum aanduidingBijzonderNederlanderschap = default(AanduidingBijzonderNederlanderschapEnum), DatumOnvolledig datumIngangGeldigheid = default(DatumOnvolledig), Waardetabel nationaliteit = default(Waardetabel), Waardetabel redenOpname = default(Waardetabel), NationaliteitInOnderzoek inOnderzoek = default(NationaliteitInOnderzoek), bool geheimhoudingPersoonsgegevens = default(bool), DatumOnvolledig datumTot = default(DatumOnvolledig), Waardetabel redenBeeindigen = default(Waardetabel), bool indicatieNationaliteitBeeindigd = default(bool))
        {
            this.AanduidingBijzonderNederlanderschap = aanduidingBijzonderNederlanderschap;
            this.DatumIngangGeldigheid = datumIngangGeldigheid;
            this.Nationaliteit = nationaliteit;
            this.RedenOpname = redenOpname;
            this.InOnderzoek = inOnderzoek;
            this.GeheimhoudingPersoonsgegevens = geheimhoudingPersoonsgegevens;
            this.DatumTot = datumTot;
            this.RedenBeeindigen = redenBeeindigen;
            this.IndicatieNationaliteitBeeindigd = indicatieNationaliteitBeeindigd;
        }

        /// <summary>
        /// Gets or Sets AanduidingBijzonderNederlanderschap
        /// </summary>
        [DataMember(Name = "aanduidingBijzonderNederlanderschap", EmitDefaultValue = false)]
        public AanduidingBijzonderNederlanderschapEnum AanduidingBijzonderNederlanderschap { get; set; }

        /// <summary>
        /// Gets or Sets DatumIngangGeldigheid
        /// </summary>
        [DataMember(Name = "datumIngangGeldigheid", EmitDefaultValue = false)]
        public DatumOnvolledig DatumIngangGeldigheid { get; set; }

        /// <summary>
        /// Gets or Sets Nationaliteit
        /// </summary>
        [DataMember(Name = "nationaliteit", EmitDefaultValue = false)]
        public Waardetabel Nationaliteit { get; set; }

        /// <summary>
        /// Gets or Sets RedenOpname
        /// </summary>
        [DataMember(Name = "redenOpname", EmitDefaultValue = false)]
        public Waardetabel RedenOpname { get; set; }

        /// <summary>
        /// Gets or Sets InOnderzoek
        /// </summary>
        [DataMember(Name = "inOnderzoek", EmitDefaultValue = false)]
        public NationaliteitInOnderzoek InOnderzoek { get; set; }

        /// <summary>
        /// Gegevens mogen niet worden verstrekt aan derden / maatschappelijke instellingen. 
        /// </summary>
        /// <value>Gegevens mogen niet worden verstrekt aan derden / maatschappelijke instellingen. </value>
        [DataMember(Name = "geheimhoudingPersoonsgegevens", EmitDefaultValue = false)]
        public bool GeheimhoudingPersoonsgegevens { get; set; }

        /// <summary>
        /// Gets or Sets DatumTot
        /// </summary>
        [DataMember(Name = "datumTot", EmitDefaultValue = false)]
        public DatumOnvolledig DatumTot { get; set; }

        /// <summary>
        /// Gets or Sets RedenBeeindigen
        /// </summary>
        [DataMember(Name = "redenBeeindigen", EmitDefaultValue = false)]
        public Waardetabel RedenBeeindigen { get; set; }

        /// <summary>
        /// Geeft aan dat de nationaliteit beëindigd is. 
        /// </summary>
        /// <value>Geeft aan dat de nationaliteit beëindigd is. </value>
        [DataMember(Name = "indicatieNationaliteitBeeindigd", EmitDefaultValue = false)]
        public bool IndicatieNationaliteitBeeindigd { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            var sb = new StringBuilder();
            sb.Append("class Nationaliteithistorie {\n");
            sb.Append("  AanduidingBijzonderNederlanderschap: ").Append(AanduidingBijzonderNederlanderschap).Append("\n");
            sb.Append("  DatumIngangGeldigheid: ").Append(DatumIngangGeldigheid).Append("\n");
            sb.Append("  Nationaliteit: ").Append(Nationaliteit).Append("\n");
            sb.Append("  RedenOpname: ").Append(RedenOpname).Append("\n");
            sb.Append("  InOnderzoek: ").Append(InOnderzoek).Append("\n");
            sb.Append("  GeheimhoudingPersoonsgegevens: ").Append(GeheimhoudingPersoonsgegevens).Append("\n");
            sb.Append("  DatumTot: ").Append(DatumTot).Append("\n");
            sb.Append("  RedenBeeindigen: ").Append(RedenBeeindigen).Append("\n");
            sb.Append("  IndicatieNationaliteitBeeindigd: ").Append(IndicatieNationaliteitBeeindigd).Append("\n");
            sb.Append("}\n");
            return sb.ToString();
        }

        /// <summary>
        /// Returns the JSON string presentation of the object
        /// </summary>
        /// <returns>JSON string presentation of the object</returns>
        public virtual string ToJson()
        {
            return Newtonsoft.Json.JsonConvert.SerializeObject(this, Newtonsoft.Json.Formatting.Indented);
        }

        /// <summary>
        /// Returns true if objects are equal
        /// </summary>
        /// <param name="input">Object to be compared</param>
        /// <returns>Boolean</returns>
        public override bool Equals(object input)
        {
            return this.Equals(input as Nationaliteithistorie);
        }

        /// <summary>
        /// Returns true if Nationaliteithistorie instances are equal
        /// </summary>
        /// <param name="input">Instance of Nationaliteithistorie to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(Nationaliteithistorie input)
        {
            if (input == null)
                return false;

            return 
                (
                    this.AanduidingBijzonderNederlanderschap == input.AanduidingBijzonderNederlanderschap ||
                    (this.AanduidingBijzonderNederlanderschap != null &&
                    this.AanduidingBijzonderNederlanderschap.Equals(input.AanduidingBijzonderNederlanderschap))
                ) && 
                (
                    this.DatumIngangGeldigheid == input.DatumIngangGeldigheid ||
                    (this.DatumIngangGeldigheid != null &&
                    this.DatumIngangGeldigheid.Equals(input.DatumIngangGeldigheid))
                ) && 
                (
                    this.Nationaliteit == input.Nationaliteit ||
                    (this.Nationaliteit != null &&
                    this.Nationaliteit.Equals(input.Nationaliteit))
                ) && 
                (
                    this.RedenOpname == input.RedenOpname ||
                    (this.RedenOpname != null &&
                    this.RedenOpname.Equals(input.RedenOpname))
                ) && 
                (
                    this.InOnderzoek == input.InOnderzoek ||
                    (this.InOnderzoek != null &&
                    this.InOnderzoek.Equals(input.InOnderzoek))
                ) && 
                (
                    this.GeheimhoudingPersoonsgegevens == input.GeheimhoudingPersoonsgegevens ||
                    this.GeheimhoudingPersoonsgegevens.Equals(input.GeheimhoudingPersoonsgegevens)
                ) && 
                (
                    this.DatumTot == input.DatumTot ||
                    (this.DatumTot != null &&
                    this.DatumTot.Equals(input.DatumTot))
                ) && 
                (
                    this.RedenBeeindigen == input.RedenBeeindigen ||
                    (this.RedenBeeindigen != null &&
                    this.RedenBeeindigen.Equals(input.RedenBeeindigen))
                ) && 
                (
                    this.IndicatieNationaliteitBeeindigd == input.IndicatieNationaliteitBeeindigd ||
                    this.IndicatieNationaliteitBeeindigd.Equals(input.IndicatieNationaliteitBeeindigd)
                );
        }

        /// <summary>
        /// Gets the hash code
        /// </summary>
        /// <returns>Hash code</returns>
        public override int GetHashCode()
        {
            unchecked // Overflow is fine, just wrap
            {
                int hashCode = 41;
                if (this.AanduidingBijzonderNederlanderschap != null)
                    hashCode = hashCode * 59 + this.AanduidingBijzonderNederlanderschap.GetHashCode();
                if (this.DatumIngangGeldigheid != null)
                    hashCode = hashCode * 59 + this.DatumIngangGeldigheid.GetHashCode();
                if (this.Nationaliteit != null)
                    hashCode = hashCode * 59 + this.Nationaliteit.GetHashCode();
                if (this.RedenOpname != null)
                    hashCode = hashCode * 59 + this.RedenOpname.GetHashCode();
                if (this.InOnderzoek != null)
                    hashCode = hashCode * 59 + this.InOnderzoek.GetHashCode();
                hashCode = hashCode * 59 + this.GeheimhoudingPersoonsgegevens.GetHashCode();
                if (this.DatumTot != null)
                    hashCode = hashCode * 59 + this.DatumTot.GetHashCode();
                if (this.RedenBeeindigen != null)
                    hashCode = hashCode * 59 + this.RedenBeeindigen.GetHashCode();
                hashCode = hashCode * 59 + this.IndicatieNationaliteitBeeindigd.GetHashCode();
                return hashCode;
            }
        }

        /// <summary>
        /// To validate all properties of the instance
        /// </summary>
        /// <param name="validationContext">Validation context</param>
        /// <returns>Validation Result</returns>
        IEnumerable<System.ComponentModel.DataAnnotations.ValidationResult> IValidatableObject.Validate(ValidationContext validationContext)
        {
            yield break;
        }
    }

}
