from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'stock', 'imagen']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'pastel-input'}),
            'descripcion': forms.Textarea(attrs={'class': 'pastel-input', 'rows': 3}),
            'precio': forms.NumberInput(attrs={'class': 'pastel-input'}),
            'stock': forms.NumberInput(attrs={'class': 'pastel-input'}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'pastel-input'}),
        }
