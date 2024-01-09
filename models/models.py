<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="keyboards" content="HTML 5, CSS3, JavaScript, JQuery, AngularJs"/>
  <meta name="description" content="Dynamic web development">
  <meta name="author" content="edmond">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  </head>
<body>    
<header>
  <h1>Chlamydia & Gonorrhea case reporting form</h1>
</header>
<h2>Clinic Information</h2>
<form method="post">
    <div class="form-group">
    <label for="date">Date:</label>
    <input type="date" id="date" name="date" ><span id="dateerr"></span>
    <label for="person_completing">Person Completing Form:</label>
    <input type="text" id="person_completing" name="person_completing"><span id="pcomerr"></span>
    <label for="health_provider">Health Provider:</label>
    <input type="text" id="health-provider" name="health_provider"><span id="healtherr"></span>
    <label for="contact_info">Contact phone number/fax:</label>
    <input type="text" id="contact-info" name="contact_info"><span id="contacterr"></span>
    </div>
    <p>Your lab reported a communicable disease on the patient shown below and listed you as the provider.
      The Oregon Department of Human Services and Washington County require additional information.
      The fax cover sheet you have received references Oregon Law (ORS 433) that requires you to report this information.
      Please complete the form within 24 hours, or by the end of the next working day, and fax it back to our office at 503-846-3644.
      If you prefer, you may call to report the required information. We appreciate your cooperation and prompt handling of this confidential report.</p>
    <h2>Patient Information — Please complete all information requested below</h2>


        <table>
          <tr>
            <th>1. NAME:</th>
            <td><input type="text" id="name" name="name"><span id="nameerr"></span></td>
            <th>DATE OF BIRTH:</th>
            <td><input type="date" id="date-of-birth" name="date-of-birth"><span id="doberr"></span></td>
            <th>GENDER:</th>
            <td>
              <input type="checkbox" id="gender-male" name="gender" value="Male">
              <label for="gender-male">Male</label>
              <input type="checkbox" id="gender-female" name="gender" value="Female">
              <label for="gender-female">Female</label>
              <input type="checkbox" id="gender-other" name="gender" value="Other">
              <label for="gender-other">Other</label><span id="gendererr"></span>
            </td>
          </tr>
          <tr>
            <th>2. HOME ADDRESS:</th>
            <td colspan="5">
              <input type="text" id="street" name="street" placeholder="Street">
              <input type="text" id="city-state" name="city-state" placeholder="City/State">
              <input type="text" id="zip" name="zip" placeholder="Zip">
            </td>
          </tr>
          <tr>
            <th>PHONE NUMBER:</th>
            <td><input type="text" id="phone-number" name="phone-number"></td>
            <th>ALTERNATIVE # :</th>
            <td><input type="text" id="alternative-number" name="alternative-number"></td>
          </tr>
          <tr>
    <th>3. PREGNANCY TEST RESULTS:</th>
    <td colspan="5">
      <input type="checkbox" id="test-results-na" name="test-results" value="N/A">
      <label for="test-results-na">N/A</label>
      <input type="checkbox" id="test-results-negative" name="test-results" value="Negative">
      <label for="test-results-negative">Negative</label>
      <input type="checkbox" id="test-results-unknown" name="test-results" value="Unknown">
      <label for="test-results-unknown">Unknown</label>
      <input type="checkbox" id="test-results-positive" name="test-results" value="Positive">
      <label for="test-results-positive">Positive:</label>
      If positive, how many weeks?
      <input type="text" id="weeks-pregnant" name="weeks-pregnant"><span id="pregnancytesterr"></span>
    </td>
  </tr>
  <tr>
  <th>4. ETHNICITY:</th>
  <td colspan="5">
    <input type="checkbox" id="ethnicity-hispanic" name="ethnicity" value="Hispanic">
    <label for="ethnicity-hispanic">Hispanic</label>
    <input type="checkbox" id="ethnicity-non-hispanic" name="ethnicity" value="Non-Hispanic">
    <label for="ethnicity-non-hispanic">Non-Hispanic</label>
    <input type="checkbox" id="ethnicity-unknown" name="ethnicity" value="Unknown">
    <label for="ethnicity-unknown">Unknown</label><span id="ethnicityerr"></span>
  </td>
</tr>
<tr>
  <th>RACE:</th>
  <td colspan="5">
    <input type="checkbox" id="race-white" name="race" value="White">
    <label for="race-white">White</label>
    <input type="checkbox" id="race-american-indian" name="race" value="American Indian">
    <label for="race-american-indian">American Indian</label>
    <input type="checkbox" id="race-unknown" name="race" value="Unknown">
    <label for="race-unknown">Unknown</label>
    <input type="checkbox" id="race-black" name="race" value="Black">
    <label for="race-black">Black</label>
    <input type="checkbox" id="race-alaskan" name="race" value="Alaskan">
    <label for="race-alaskan">Alaskan</label>
    <input type="checkbox" id="race-asian" name="race" value="Asian">
    <label for="race-asian">Asian</label>
    <input type="checkbox" id="race-pacific-islander" name="race" value="Pacific Islander">
    <label for="race-pacific-islander">Pacific Islander</label>
    <input type="checkbox" id="race-other" name="race" value="Other">
    <label for="race-other">Other:</label>
    <input type="text" id="race-other-text" name="race-other-text"><span id="raceerr"></span>
  </td>
</tr>
<tr>
  <th>GENDER OF SEX PARTNER(S):</th>
  <td colspan="5">
    <input type="checkbox" id="partner-gender-male" name="partner-gender" value="Male">
    <label for="partner-gender-male">Male</label>
    <input type="checkbox" id="partner-gender-female" name="partner-gender" value="Female">
    <label for="partner-gender-female">Female</label>
    <input type="checkbox" id="partner-gender-both" name="partner-gender" value="Both">
    <label for="partner-gender-both">Both</label>
    <input type="checkbox" id="partner-gender-unknown" name="partner-gender" value="Unknown">
    <label for="partner-gender-unknown">Unknown</label><span id="partnergendererr"></span>
  </td>
</tr>

<tr>
  <th>5. PREVIOUS HIV TESTING:</th>
  <td colspan="5">
    <input type="checkbox" id="previous-hiv-yes" name="previous-hiv" value="Yes">
    <label for="previous-hiv-yes">Yes</label>
    <input type="checkbox" id="previous-hiv-no" name="previous-hiv" value="No">
    <label for="previous-hiv-no">No</label>
    <input type="checkbox" id="previous-hiv-unknown" name="previous-hiv" value="Unknown">
    <label for="previous-hiv-unknown">Unknown</label>
    <br>
    If yes, last result was?
    <input type="checkbox" id="previous-hiv-result-pos" name="previous-hiv-result" value="POS">
    <label for="previous-hiv-result-pos">POS</label>
    <input type="checkbox" id="previous-hiv-result-neg" name="previous-hiv-result" value="NEG">
    <label for="previous-hiv-result-neg">NEG</label>
    <input type="checkbox" id="previous-hiv-result-unknown" name="previous-hiv-result" value="Unknown">
    <label for="previous-hiv-result-unknown">Unknown</label><span id="prevhiverr"></span>
    <br>
    Month of last test:
    <input type="text" id="last-test-month" name="last-test-month">
    Year of last test:
    <input type="text" id="last-test-year" name="last-test-year">
  </td>
</tr>

<tr>
  <th>6. REASON FOR EXAM:</th>
  <td colspan="5">
    <input type="checkbox" id="reason-symptomatic" name="reason" value="Symptomatic">
    <label for="reason-symptomatic">Symptomatic</label>
    <input type="checkbox" id="reason-routine" name="reason" value="Routine Exam">
    <label for="reason-routine">Routine Exam</label>
    <input type="checkbox" id="reason-test-for-cure" name="reason" value="Test for Cure">
    <label for="reason-test-for-cure">Test for Cure</label>
    <input type="checkbox" id="reason-exposed-to-infection" name="reason" value="Exposed to Infection">
    <label for="reason-exposed-to-infection">Exposed to Infection</label>
    <input type="checkbox" id="reason-pregnant" name="reason" value="Pregnant">
    <label for="reason-pregnant">Pregnant</label><span id="reasonerr"></span>
  </td>
</tr>
<tr>
  <th>DIAGNOSIS:</th>
  <td colspan="5">
    <input type="checkbox" id="diagnosis-asymptomatic" name="diagnosis" value="Asymptomatic">
    <label for="diagnosis-asymptomatic">Asymptomatic</label>
    <input type="checkbox" id="diagnosis-symptomatic-uncomplicated" name="diagnosis" value="Symptomatic-Uncomplicated">
    <label for="diagnosis-symptomatic-uncomplicated">Symptomatic-Uncomplicated</label>
    <input type="checkbox" id="diagnosis-pid" name="diagnosis" value="Pelvic Inflammatory Disease (PID)">
    <label for="diagnosis-pid">Pelvic Inflammatory Disease (PID)</label>
    <input type="checkbox" id="diagnosis-ophthalmia" name="diagnosis" value="Ophthalmia / Conjunctivitis">
    <label for="diagnosis-ophthalmia">Ophthalmia / Conjunctivitis</label>
    <input type="checkbox" id="diagnosis-disseminated" name="diagnosis" value="Disseminated">
    <label for="diagnosis-disseminated">Disseminated</label><span id="diagnosiserrr"></span>
  </td>
</tr>
<tr>
  <th>SITE(S):</th>
  <td colspan="5">
    <input type="checkbox" id="site-cervix" name="site" value="Cervix">
    <label for="site-cervix">Cervix</label>
    <input type="checkbox" id="site-ocular" name="site" value="Ocular">
    <label for="site-ocular">Ocular</label>
    <input type="checkbox" id="site-vaginal" name="site" value="Vaginal">
    <label for="site-vaginal">Vaginal</label>
    <input type="checkbox" id="site-urine" name="site" value="Urine">
    <label for="site-urine">Urine</label>
    <input type="checkbox" id="site-urethra" name="site" value="Urethra">
    <label for="site-urethra">Urethra</label>
    <input type="checkbox" id="site-pharynx" name="site" value="Pharynx">
    <label for="site-pharynx">Pharynx</label>
    <input type="checkbox" id="site-rectum" name="site" value="Rectum">
    <label for="site-rectum">Rectum</label>
    <input type="checkbox" id="site-other" name="site" value="Other">
    <label for="site-other">Other</label><span id="siteerr"></span>
  </td>
</tr>
    </table>
    <input type="submit" value="Submit">

  </form>

  </article>

</body>


</html>