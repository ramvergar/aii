#encoding:utf-8
from django import forms
   
class UsuarioBusquedaForm(forms.Form):
    idUsuario = forms.CharField(label="Id de Usuario", widget=forms.TextInput, required=True)
    
class PeliculaBusquedaForm(forms.Form):
    idPelicula = forms.CharField(label="Id de Pelicula", widget=forms.TextInput, required=True)

class AnimeRecomendacionForm(forms.Form):
    usuario_id = forms.IntegerField(label="ID del Usuario")
    formato_emision = forms.ChoiceField(
        choices=[('TV', 'TV'), ('OVA', 'OVA'), ('Movie', 'Movie'), ('Special', 'Special')],
        label="Formato de Emisión"
    )

class UsuarioBusquedaForm(forms.Form):
    idUsuario = forms.IntegerField(label="ID Usuario", min_value=1)
    formato = forms.ChoiceField(label="Formato de Emisión", choices= [
    ('TV', 'TV'),
    ('Movie', 'Movie'),
    ('OVA', 'OVA'),
    ('Special', 'Special'),
])