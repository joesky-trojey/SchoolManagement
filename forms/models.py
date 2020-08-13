from django.db import models

# Create your models here.
class Forms(models.Model):
    form_id=models.IntegerField(primary_key=True)
    form_name=models.TextField(max_length=10, verbose_name='Form name')

    """
    Model field 	Form field
AutoField 	Not represented in the form
BigAutoField 	Not represented in the form
BigIntegerField 	IntegerField with min_value set to -9223372036854775808 and max_value set to 9223372036854775807.
BinaryField 	CharField, if editable is set to True on the model field, otherwise not represented in the form.
BooleanField 	BooleanField, or NullBooleanField if null=True.
CharField 	CharField with max_length set to the model field’s max_length and empty_value set to None if null=True.
DateField 	DateField
DateTimeField 	DateTimeField
DecimalField 	DecimalField
DurationField 	DurationField
EmailField 	EmailField
FileField 	FileField
FilePathField 	FilePathField
FloatField 	FloatField
ForeignKey 	ModelChoiceField (see below)
ImageField 	ImageField
IntegerField 	IntegerField
IPAddressField 	IPAddressField
GenericIPAddressField 	GenericIPAddressField
ManyToManyField 	ModelMultipleChoiceField (see below)
NullBooleanField 	NullBooleanField
PositiveIntegerField 	IntegerField
PositiveSmallIntegerField 	IntegerField
SlugField 	SlugField
SmallAutoField 	Not represented in the form
SmallIntegerField 	IntegerField
TextField 	CharField with widget=forms.Textarea
TimeField 	TimeField
URLField 	URLField
UUIDField 	UUIDField
    """