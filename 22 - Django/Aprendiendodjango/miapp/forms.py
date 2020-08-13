from django import forms
from django.core import validators

class FormArticle (forms.Form):
    title = forms.CharField(label="Titulo",
                            max_length=40, #40 caracteres de largo
                            required=True, #No es rquesitio llenarlo
                            widget=forms.TextInput(
                                attrs={
                                    'placeholder':'Mete el titulo',
                                    'class':'titulo_form_article'
                                } 
                                ), #Permite cambios a nivel visual
                            validators = [validators.MinLengthValidator(4,'El titulo es muy corto'),
                                        #Valores permitidos, mensaje de error, tipo de  error
                                        validators.RegexValidator('^[A-Za-z0-9 ñ]*$','El titulo esta mal formado','invalid title')
                                        ]   # A-Z , a-z , 0-9 y espacios '' 
                            )
    content = forms.CharField(label="Contenido", 
                                widget=forms.Textarea, #Permite cambios a nivel visual
                               validators= [validators.MaxLengthValidator(50,'Has puesto mucho texto')] )  
                                
    content.widget.attrs.update({'placeholder':'Mete el contenido',
                                    'class':'content_form_article',
                                    'id':'contenido_form'
                                })

    public_options=[(1,'SI'),(0,'NO')]  #Opciones del slector
    public = forms.TypedChoiceField(label = "Publico", choices=public_options)