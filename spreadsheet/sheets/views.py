from rest_framework import viewsets
from .models import Spreadsheet, Cell
from .serializers import SpreadsheetSerializer, CellSerializer
from django.shortcuts import render
from django.http import JsonResponse

class SpreadsheetViewSet(viewsets.ModelViewSet):
    queryset = Spreadsheet.objects.all()
    serializer_class = SpreadsheetSerializer

def spreadsheet_data(request):
    data = list(Spreadsheet.objects.values())  # Convert QuerySet to list of dicts
    print("Spreadsheet API Data:", data)  # Debugging line
    return JsonResponse({"data": data}, safe=False)

class CellViewSet(viewsets.ModelViewSet):
    queryset = Cell.objects.all()
    serializer_class = CellSerializer

    def perform_create(self, serializer):
        """Ensure cell uniqueness in a spreadsheet."""
        spreadsheet = serializer.validated_data.get("spreadsheet")
        row = serializer.validated_data.get("row")
        column = serializer.validated_data.get("column")

        existing_cell = Cell.objects.filter(spreadsheet=spreadsheet, row=row, column=column).first()
        if existing_cell:
            existing_cell.value = serializer.validated_data.get("value", existing_cell.value)
            existing_cell.formula = serializer.validated_data.get("formula", existing_cell.formula)
            existing_cell.save()
            return existing_cell
        else:
            return serializer.save()

def index(request):
    return render(request, "spreadsheet/index.html")