from django.db import models


class ResumeAnalysis(models.Model):

    resume_name = models.CharField(max_length=255)

    job_description = models.TextField()

    score = models.IntegerField()

    matched_skills = models.JSONField(default=list)

    missing_skills = models.JSONField(default=list)

    extracted_text = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.resume_name