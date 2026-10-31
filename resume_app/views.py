from django.shortcuts import render
from pypdf import PdfReader
from .models import ResumeAnalysis


def home(request):

    if request.method == "POST":

        resume = request.FILES.get('resume')

        job_description = request.POST.get(
            'job_description', ''
        ).strip()

        # Validate resume
        if not resume:
            return render(request, 'resume_app/index.html', {
                'error': 'Please upload your resume.'
            })

        # Validate job description
        if not job_description:
            return render(request, 'resume_app/index.html', {
                'error': 'Please enter a job description.'
            })

        # Validate PDF extension
        if not resume.name.lower().endswith('.pdf'):
            return render(request, 'resume_app/index.html', {
                'error': 'Only PDF files are allowed.'
            })

        try:

            # Extract PDF text
            reader = PdfReader(resume)

            text = ""

            for page in reader.pages:
                text += page.extract_text() or ""

            if not text.strip():
                return render(request, 'resume_app/index.html', {
                    'error': 'No readable text found in this PDF.'
                })

            # Available skills
            skills = [
                "Python",
                "Java",
                "SQL",
                "Django",
                "HTML",
                "CSS",
                "JavaScript",
                "Machine Learning",
                "Communication",
                "Projects"
            ]

            # Find required skills
            required_skills = []

            for skill in skills:
                if skill.lower() in job_description.lower():
                    required_skills.append(skill)

            # Find matched skills
            matched_skills = []

            for skill in required_skills:
                if skill.lower() in text.lower():
                    matched_skills.append(skill)

            # Find missing skills
            missing_skills = [
                skill for skill in required_skills
                if skill not in matched_skills
            ]

            # Calculate score
            if required_skills:
                score = (
                    len(matched_skills) / len(required_skills)
                ) * 100
            else:
                score = 0

            final_score = round(score)

            # Save analysis in database
            ResumeAnalysis.objects.create(
                resume_name=resume.name,
                job_description=job_description,
                score=final_score,
                matched_skills=matched_skills,
                missing_skills=missing_skills,
                extracted_text=text
            )

            # Display result
            return render(request, 'resume_app/result.html', {
                'score': final_score,
                'found': matched_skills,
                'missing': missing_skills,
                'text': text,
            })

        except Exception as error:

            return render(request, 'resume_app/index.html', {
                'error': f'Unable to process resume: {error}'
            })

    return render(request, 'resume_app/index.html')