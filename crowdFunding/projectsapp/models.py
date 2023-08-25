from django.db import models
from datetime import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import Avg


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=200, unique=True)
    details = models.TextField()
    rate = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    total_target = models.IntegerField(null=False, blank=False)
    current_donation = models.IntegerField(default=0)
    start_campaign = models.DateField(default=datetime.now, blank=True)
    end_campaign = models.DateField(null=False, blank=False)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    selected_at_by_admin = models.BooleanField(default=False)
    category_id = models.ForeignKey(to="Category", on_delete=models.CASCADE)
    main_Image = models.ImageField(upload_to='media/Projects/%y/%m/%d', null=False, blank=False)
    owner_id = models.ForeignKey(to="users.CustomUser", on_delete=models.CASCADE)

    def average_rating(self) -> int:
        return ProjectRating.objects.filter(ProjectId=self).aggregate(Avg("rating"))["rating__avg"] or 0

    def goal_percentage(self):
        percentage = (self.current_donation / self.total_target) * 100
        return f"{int(percentage)}"

    def delete(self):
        total_percentage = self.total_target * 0.25
        if self.current_donation >= total_percentage:
            return 0
        return 1

    def __str__(self):
        return self.title


class Projects_pictures(models.Model):
    image = models.ImageField(upload_to='media/Projects/%y/%m/%d', null=False, blank=False)
    ProjectId = models.ForeignKey(to="Project", on_delete=models.PROTECT)

    def __str__(self):
        return self.ProjectId.title


class Tags(models.Model):
    name_tag = models.CharField(max_length=20)
    ProjectId = models.ForeignKey(to="Project", on_delete=models.PROTECT)
    
    def __str__(self):
        return self.name_tag


class ProjectReport(models.Model):
    reason = models.TextField(null=False, blank=False)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    ProjectId = models.ForeignKey(to="Project", on_delete=models.CASCADE)
    owner_id = models.ForeignKey(to="users.CustomUser", on_delete=models.CASCADE)

    def __str__(self):
        return f"report {self.id} on comment {self.ProjectId} from {self.owner_id}"


class Comment(models.Model):
    commentValue = models.TextField(null=False, blank=False)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    ProjectId = models.ForeignKey(to="Project", on_delete=models.PROTECT)
    owner_id = models.ForeignKey(to="users.CustomUser", on_delete=models.CASCADE)

    def __str__(self):
        return f"comment {self.id} on {self.ProjectId.title} from {self.owner_id}"


class CommentReport(models.Model):
    reason = models.TextField(null=False, blank=False)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    commentId = models.ForeignKey(to="Comment", on_delete=models.CASCADE)
    owner_id = models.ForeignKey(to="users.CustomUser", on_delete=models.CASCADE)

    def __str__(self):
        return f"report {self.id} on comment {self.commentId.id} on {self.commentId.ProjectId.title} from {self.owner_id}"


class Replay(models.Model):
    replayValue = models.TextField(null=False, blank=False)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    commentId = models.ForeignKey(to="Comment", on_delete=models.CASCADE)
    owner_id = models.ForeignKey(to="users.CustomUser", on_delete=models.CASCADE)

    def __str__(self):
        return f"replay {self.id} comment {self.commentId.id} on {self.commentId.ProjectId.title} from {self.owner_id}"


class ReplayReport(models.Model):
    reason = models.TextField(null=False, blank=False)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    replayId = models.ForeignKey(to="Replay", on_delete=models.CASCADE)
    owner_id = models.ForeignKey(to="users.CustomUser", on_delete=models.CASCADE)

    def __str__(self):
        return f"report {self.id} on replay {self.replayId.id} on comment {self.replayId.commentId.id} on {self.replayId.commentId.ProjectId.title}"


class Test2(models.Model):
    reason = models.TextField(null=False, blank=False)
    replayId = models.ForeignKey(to="Replay", on_delete=models.CASCADE)
    owner_id = models.ForeignKey(to="users.CustomUser", on_delete=models.CASCADE)

    def __str__(self):
        return f"report {self.id} on replay {self.replayId.id} on comment {self.replayId.commentId.id} on {self.replayId.commentId.ProjectId.title}"



class Test4(models.Model):
    reason = models.TextField(null=False, blank=False)
    replayId = models.ForeignKey(to="Replay", on_delete=models.CASCADE)
    owner_id = models.ForeignKey(to="users.CustomUser", on_delete=models.CASCADE)

    def __str__(self):
        return f"report {self.id} on replay {self.replayId.id} on comment {self.replayId.commentId.id} on {self.replayId.commentId.ProjectId.title}"


class ProjectRating(models.Model):
    owner_id = models.ForeignKey(to="users.CustomUser", on_delete=models.CASCADE)
    ProjectId = models.ForeignKey(to="Project", on_delete=models.CASCADE)
    rating = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])

    def __str__(self):
        return f"rating {self.rating} on {self.ProjectId.title} by {self.owner_id} "


class sample(models.Model):
    name = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name
