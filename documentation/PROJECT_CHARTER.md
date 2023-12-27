# Project Charter 

## Executive Summary
We will be using a synthetic patient database simulating California inpatient discharge data to do a proof of concept study in support of Dr. Jen Franks’ research interests.  Specifically, we’ll be looking at the utilization of immediate postpartum LARC (long-acting reversible contraceptives) at California hospitals to determine if Kern Medical Center in Bakersfield was an outlier for not offering these procedures before residents did advocacy work in recent years.  The goal is to support the preparation of a data request for HCAI, and to create an analytic program that can be repeated when that real-world data is obtained.

## Project Goals
- Create a tool to analyze data from the synthetic patient database
- Generate a report with this tool detailing various health metrics as specified by the client

## Deliverables
* A report of the synthetic data with the following parameters/features:
   - Data should be stratified based on location
   - Report should highlight places that are not supplying LARC
   - Report should highlight insurance companies that are not covering LARC
   - Report should highlight the change in LARC placement rates at Kern Medical Center over time from 2018 to 2023.
   - Data should include the following points and be limited to hospitals that supply obstetrics care:
     1. \# of L&D stays in CA
        - Include procedure codes, how many of those stays had the procedures done during those stays
     2. What insurances the patients have
     3. Post-partum hemorrhaging (diagnosis code, control for confounding variables)
     5. Infection
        - Intra-amniotic infection
        - Chorioamnionitis
        - Endometritis
     4. Demographics (representative of people who have had L&D stays across California)
        - Age, ethnicity, socioeconomic status (optional) (medicaid status), parity
        - Comparison between people who got LARC and who haven’t
        - Disability (Mental illness in particular) (Intellectual disability)
* A code repository for the program 

## Business Case / Background

**Why are we doing this?**
- We experienced difficulty at Kern Medical Center in Bakersfield instituting a program to support immediate postpartum LARC because of concerns for reimbursement.  Given the strong benefits in the literature including minimizing barriers to care and promoting patient autonomy, a study looking at overall utilization of this resource by hospitals would be beneficial for better contextualizing the contraceptive environment, particularly for patient populations whose only interaction with the healthcare system is during the immediate postpartum period.  We suspect the option of immediate postpartum LARC is standard of care in other hospitals and that patient's readily utilize this service, but we need the data to back that up.
- During early 2023 IPP (Immediate Post-partum) placement of Nexplanon increased as insurance reimbursement improved, however placement of IUDs still lagged behind, per Dr. Franks assertion likely secondary to provider culture and lack of advocacy. There is evidence to support that IPP IUD placement is preferrable to interval post-partum IUD placement at greater than 6 weeks postpartum because of the decreased risk of uterine perforation/embedment. (Note: we may be able to add to this evidence with a future study using administrative healthcare data.)
- This data source is new to Dr. Franks, so the hope is that we can use synthetic data to demonstrate the use case before jumping through the hoops required to get access to real data.
- The hope is that the analysis will be repeated on real-world data obtained from HCAI and used to bolster the argument that these procedures should both be offered by the medical centers in the Central Valley and should be covered by the health insurance providers most commonly associated with those patients.

## Benefits, Costs, and Budget

**Benefits:**
- **Project**
  - Paves the way for data-driven research on IPP LARC procedures in California, empowering clinicians to do advocacy, policymakers to allocate resources in a targeted way, and resident physicians to measure the impact of their QI projects.
- **People** 
  - Adds to Rhonda’s public coding portfolio
  - Develops Iris’s project management skills and experience
  - Supports Dr. Franks in her research and advocacy interests
- **Organization:**
  - Provides a first use case for the synthetic patient database
  - Helps strengthen the relationship between Orchid and Dr. Franks 

**Costs:**
- Our time
- $4 per month for server use

# Scope and Exclusion

**In-Scope:**
- Create the report
- Write the code

**Out-of-Scope:**
- Obtaining the real data
- Writing the grant
- Presenting to Kern Hospital
- Publication of any papers
- Data outside of California 
  
# Project Team
Project Sponsor: TBD

Product Owner: TBD

Project Lead: Iris F. 

Project Development Team: TBD

Additional Stakeholders: TBD


# Measuring Success
**What is acceptable:**
1. Final report has been delivered to the client before July 2024
2. Client is satisfied with the extent of data in the report
3. Rhonda is satisfied with the project as an addition to her public coding portfolio.
