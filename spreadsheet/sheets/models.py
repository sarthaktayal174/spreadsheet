from django.db import models

class Spreadsheet(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Cell(models.Model):
    spreadsheet = models.ForeignKey(Spreadsheet, on_delete=models.CASCADE, related_name="cells", null=True)  # Temporarily allow null
    row = models.IntegerField()
    column = models.IntegerField()
    value = models.TextField(blank=True, null=True)
    formula = models.TextField(blank=True, null=True)

    class Meta:
        unique_together = ('spreadsheet', 'row', 'column')  # Ensure uniqueness for each cell

    def __str__(self):
        return f"Sheet: {self.spreadsheet.name}, Cell: ({self.row}, {self.column})"

