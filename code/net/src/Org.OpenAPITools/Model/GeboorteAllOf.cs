/* 
 * BRP historie bevragen
 *
 * API voor het zoeken en raadplegen van historische verblijfplaatsen, partners, nationaliteiten en verblijfstitels uit de BRP (inclusief de RNI).  Zie de [Functionele documentatie](https://github.com/VNG-Realisatie/Haal-Centraal-BRP-historie-bevragen/tree/v1.0.0/features) voor nadere toelichting. 
 *
 * The version of the OpenAPI document: 0.0.1 (develop)
 * 
 * Generated by: https://github.com/openapitools/openapi-generator.git
 */

using System;
using System.Linq;
using System.IO;
using System.Text;
using System.Text.RegularExpressions;
using System.Collections;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Runtime.Serialization;
using Newtonsoft.Json;
using Newtonsoft.Json.Converters;
using System.ComponentModel.DataAnnotations;
using OpenAPIDateConverter = Org.OpenAPITools.Client.OpenAPIDateConverter;

namespace Org.OpenAPITools.Model
{
    /// <summary>
    /// Gegevens over de geboorte. * **datum** : datum waarop de persoon is geboren. * **land** : land waar de persoon is geboren * **plaats** : plaats waar de persoon is geboren. Voor een plaats buiten Nederland is gemeentecode&#x3D;1999 (RNI) en gemeentenaam de buitenlandse plaatsnaam of aanduiding. 
    /// </summary>
    [DataContract]
    public partial class GeboorteAllOf :  IEquatable<GeboorteAllOf>, IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="GeboorteAllOf" /> class.
        /// </summary>
        /// <param name="land">land.</param>
        /// <param name="plaats">plaats.</param>
        /// <param name="inOnderzoek">inOnderzoek.</param>
        public GeboorteAllOf(Waardetabel land = default(Waardetabel), Waardetabel plaats = default(Waardetabel), GeboorteInOnderzoek inOnderzoek = default(GeboorteInOnderzoek))
        {
            this.Land = land;
            this.Plaats = plaats;
            this.InOnderzoek = inOnderzoek;
        }
        
        /// <summary>
        /// Gets or Sets Land
        /// </summary>
        [DataMember(Name="land", EmitDefaultValue=false)]
        public Waardetabel Land { get; set; }

        /// <summary>
        /// Gets or Sets Plaats
        /// </summary>
        [DataMember(Name="plaats", EmitDefaultValue=false)]
        public Waardetabel Plaats { get; set; }

        /// <summary>
        /// Gets or Sets InOnderzoek
        /// </summary>
        [DataMember(Name="inOnderzoek", EmitDefaultValue=false)]
        public GeboorteInOnderzoek InOnderzoek { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            var sb = new StringBuilder();
            sb.Append("class GeboorteAllOf {\n");
            sb.Append("  Land: ").Append(Land).Append("\n");
            sb.Append("  Plaats: ").Append(Plaats).Append("\n");
            sb.Append("  InOnderzoek: ").Append(InOnderzoek).Append("\n");
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
            return this.Equals(input as GeboorteAllOf);
        }

        /// <summary>
        /// Returns true if GeboorteAllOf instances are equal
        /// </summary>
        /// <param name="input">Instance of GeboorteAllOf to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(GeboorteAllOf input)
        {
            if (input == null)
                return false;

            return 
                (
                    this.Land == input.Land ||
                    (this.Land != null &&
                    this.Land.Equals(input.Land))
                ) && 
                (
                    this.Plaats == input.Plaats ||
                    (this.Plaats != null &&
                    this.Plaats.Equals(input.Plaats))
                ) && 
                (
                    this.InOnderzoek == input.InOnderzoek ||
                    (this.InOnderzoek != null &&
                    this.InOnderzoek.Equals(input.InOnderzoek))
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
                if (this.Land != null)
                    hashCode = hashCode * 59 + this.Land.GetHashCode();
                if (this.Plaats != null)
                    hashCode = hashCode * 59 + this.Plaats.GetHashCode();
                if (this.InOnderzoek != null)
                    hashCode = hashCode * 59 + this.InOnderzoek.GetHashCode();
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
