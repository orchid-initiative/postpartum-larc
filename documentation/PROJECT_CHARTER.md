# Project Charter 

## Executive Summary
We will be using a synthetic patient database simulating California inpatient discharge data to do a proof of concept study in support of Dr. Jen Franks’ research interests.  Specifically, we’ll be looking at the utilization of immediate postpartum LARC (long-acting reversible contraceptives) at California hospitals to determine if Kern Medical Center in Bakersfield is an outlier for not offering these procedures.  The goal is to support the preparation of a data request for HCAI, and to create an analytic program that can be repeated when that real-world data is obtained.

## Project Goals

## Deliverables
* A report of the synthetic data with the following parameters/features:
   - Data should be stratified based on location
   - Report should highlight places that are not supplying LARC
   - Report should highlight insurance companies that are not covering LARC
   - Data should include the following points and be limited to hospitals that supply obstetrics care:
     1. \# of L&D stays in CA
        - Include procedure codes, how many of those stays had the procedures done during those stays
     2. What insurances the patients have
     3. Post-partum hemorrhaging (diagnosis code, control for confounding variables)
     4. Demographics (representative of women who have had L&D stays across California)
        - Age, ethnicity, socioeconomic status (optional) (medicaid status), parity
        - Comparison between people who got LARC and who haven’t
        - Disability (Mental illness in particular) (Intellectual disability)
     5. Infection
        - Intra-amniotic infection
        - Chorioamnionitis
        - Endometritis

## Business Case / Background

**Why are we doing this?**
- Kern Medical Center in Bakersfield is hesitant to place immediate postpartum LARC because of concerns for reimbursement.  Given the strong benefits in the literature, a study looking at overall utilization of this resource by hospitals would be beneficial for better contextualizing the contraceptive environment, particularly for patient populations whose only interaction with the healthcare system is during the immediate postpartum period.  We think it is standard of care in other hospitals, but we need the data to back that up.
- This data source is new to Dr. Franks, so the hope is that we can use synthetic data to demonstrate the use case before jumping through the hoops required to get access to real data.
- The hope is that the analysis will be repeated on real-world data obtained from HCAI and used to bolster the argument that these procedures should both be offered by the medical centers in the Central Valley and should be covered by the health insurance providers most commonly associated with those patients.

## Benefits, Costs, and Budget

**Benefits:**
- **Project**
  - Getting best practices to be followed in the Kern Hospital in Bakersfield

- **People** 
  - Adds to Rhonda’s public coding portfolio
  - Develops Iris’s project management skills and experience
  - Teaches Dr. Franks how to do research with this data source

- **Organization:**
  - Provides a use case for the synthetic patient database
  - Helps strengthen the relationship between Orchid and Dr. Franks 

**Costs:**
- Our time
- $4 per month for server use

**Budget needed:**
- N/A (For now)

# Scope and Exclusion

**In-Scope:**
- Create the report
- Write the code
- Other in-scope items (optional):

**Out-of-Scope:**
- Obtaining the real data
- Writing the grant
- Presenting to Kern Hospital
- Publication of any papers
- Data outside of California 
- Other out-of-scope items (optional):
  
# Project Team
Project Sponsor: TBD

Product Owner: TBD

Project Lead: TBD

Project Development Team: TBD

Additional Stakeholders: TBD


# Measuring Success
**What is acceptable:**
1. Final report has been delivered to the client
1. Client is satisfied with the extent of data in the report
1. Rhonda is satisfied with the project as an addition to her public coding portfolio.
