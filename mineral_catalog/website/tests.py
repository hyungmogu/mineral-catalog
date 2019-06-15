from django.core.urlresolvers import reverse
from django.test import TestCase
from django.utils import timezone

# Create your tests here.
from .models import Mineral


# MODEL TEST
class MineralModelTest(TestCase):
    def test_mineral_creation(self):
        mineral = Mineral.objects.create(
            category="Organic",
            streak="Pink",
            optical_properties="Biaxial",
            group="Organic Minerals",
            name="Abelsonite",
            diaphaneity="Semitransparent",
            color="Pink-purple, dark greyish purple, pale purplish red, reddish brown",
            unit_cell="a = 8.508 \u00c5, b = 11.185 \u00c5c=7.299 \u00c5, \u03b1 = 90.85\u00b0\u03b2 = 114.1\u00b0, \u03b3 = 79.99\u00b0Z = 1",
            strunz_classification="10.CA.20",
            mohs_scale_hardness="2\u20133",
            crystal_symmetry="Space group: P1 or P1Point group: 1 or 1",
            cleavage="Probable on {111}",
            formula="C<sub>31</sub>H<sub>32</sub>N<sub>4</sub>Ni",
            luster="Adamantine, sub-metallic",
            crystal_system="Triclinic",
            image_caption="Abelsonite from the Green River Formation, Uintah County, Utah, US",
            image_filename="Abelsonite.jpg"
        )

        # query all objects in database
        query = Mineral.objects.get(pk=1)

        # the number of items in database must be 1
        self.assertEqual(Mineral.objects.count(), 1)

        # the pk of the item must be 1
        self.assertEqual(query.pk, 1)

        # the title of stored item must be the same
        self.assertEqual(query.name, 'Abelsonite')


# VIEW TEST