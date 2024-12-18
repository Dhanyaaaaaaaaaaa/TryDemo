package org.openapitools.model;

import java.net.URI;
import java.util.Objects;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonCreator;
import org.openapitools.jackson.nullable.JsonNullable;
import java.time.OffsetDateTime;
import javax.validation.Valid;
import javax.validation.constraints.*;
import io.swagger.v3.oas.annotations.media.Schema;


import java.util.*;
import javax.annotation.Generated;

/**
 * CustomerUpdate
 */

@Generated(value = "org.openapitools.codegen.languages.SpringCodegen", date = "2024-12-18T13:32:23.431172+05:30[Asia/Calcutta]", comments = "Generator version: 7.9.0")
public class CustomerUpdate {

  private String name;

  private String email;

  private String phone;

  public CustomerUpdate name(String name) {
    this.name = name;
    return this;
  }

  /**
   * Full name of the customer
   * @return name
   */
  
  @Schema(name = "name", description = "Full name of the customer", requiredMode = Schema.RequiredMode.NOT_REQUIRED)
  @JsonProperty("name")
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }

  public CustomerUpdate email(String email) {
    this.email = email;
    return this;
  }

  /**
   * Email address of the customer
   * @return email
   */
  
  @Schema(name = "email", description = "Email address of the customer", requiredMode = Schema.RequiredMode.NOT_REQUIRED)
  @JsonProperty("email")
  public String getEmail() {
    return email;
  }

  public void setEmail(String email) {
    this.email = email;
  }

  public CustomerUpdate phone(String phone) {
    this.phone = phone;
    return this;
  }

  /**
   * Phone number of the customer
   * @return phone
   */
  
  @Schema(name = "phone", description = "Phone number of the customer", requiredMode = Schema.RequiredMode.NOT_REQUIRED)
  @JsonProperty("phone")
  public String getPhone() {
    return phone;
  }

  public void setPhone(String phone) {
    this.phone = phone;
  }

  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    CustomerUpdate customerUpdate = (CustomerUpdate) o;
    return Objects.equals(this.name, customerUpdate.name) &&
        Objects.equals(this.email, customerUpdate.email) &&
        Objects.equals(this.phone, customerUpdate.phone);
  }

  @Override
  public int hashCode() {
    return Objects.hash(name, email, phone);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class CustomerUpdate {\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    email: ").append(toIndentedString(email)).append("\n");
    sb.append("    phone: ").append(toIndentedString(phone)).append("\n");
    sb.append("}");
    return sb.toString();
  }

  /**
   * Convert the given object to string with each line indented by 4 spaces
   * (except the first line).
   */
  private String toIndentedString(Object o) {
    if (o == null) {
      return "null";
    }
    return o.toString().replace("\n", "\n    ");
  }
}

