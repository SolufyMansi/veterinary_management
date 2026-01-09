<p>Hello <strong>{{ doc.pet_owner }}</strong>,</p>

<p>We are pleased to inform you that the laboratory results for <strong>{{ doc.patient_name }}</strong> are now complete.</p>

<h3>Summary of Visit:</h3>

<ul>
    <li><strong>Patient ID:</strong> {{ doc.patient }}</li>
    <li><strong>Test Date:</strong> {{ doc.test_date }}</li>
    <li><strong>Status:</strong> {{ doc.status }}</li>
    <li><strong>Accession No.:</strong> {{ doc.reference_name }}</li>
</ul>

<p>A detailed report, including diagnostic results and clinical conclusions, has been attached to this email as a PDF document.</p>

<p>Please review the attached report, or contact the clinic if you have any questions or wish to schedule a follow-up consultation.</p>

<p>Best regards,</p>

<p><strong>{{ doc.hospital or "The Veterinary Clinic Team" }}</strong></p>
