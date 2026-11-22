# Adding or updating a topic

Use the [migraine page](headache/migraine.md) as a style reference and `includes/topic-template.md` as a starting skeleton. Keep the bedside action easy to find. A reader should know what to do now, what can wait, what defines failure and who needs a call.

## Clinical structure

1. Title, owner-approved review date, one-liner and intended reader. Record the evidence audit separately.
2. Red flags and immediate action; diagnosis/classification with the important exclusions.
3. Rapid approach, workup and a numbered management flow.
4. Dosed adult first-line options, escalation criteria, contraindications and disposition. Label pediatric or off-label regimens explicitly; do not imply that every listed alternative belongs in one combined order set.
5. A short condition-specific military assessment, linked to [retention](military/deployability.md), [deployment/medications](military/deployment-medications.md) and [TRICARE](military/tricare.md).
6. A plain-language evidence brief and matching primary references. State what is uncertain when it changes the decision.

## Evidence and tone

Follow the [evidence and update policy](evidence-review.md). Use current issuing-society guidance, original trials, FDA labeling and official policy. Separate a clinical recommendation from a payer requirement and from deployment eligibility. Record actual form/version dates and distinguish PA, MN, quantity limits and medical-benefit authorization.

Write in your own words. Dry humor is welcome when it makes the point memorable; give the useful action first and keep emergencies, doses and patients out of the punchline. Avoid presenting an AI answer or a review stamp as proof that every claim was independently verified.

Do not publish patient details, Army restricted material or personnel information. Common abbreviations belong in `includes/abbreviations.md`.

## Preview and publication

Add the page to `mkdocs.yml`, preview it, and build with `mkdocs build --strict` into a separate preview directory. Check internal links and mobile readability. Have a clinician review material clinical changes and resolve or visibly bound source gaps.

**Obtain the site owner’s explicit approval before pushing or publishing.** This repository updates a public website. Keep a reviewable change log with the source and reason for each material correction.
