import os
import subprocess

from subprocess import check_call

check_call(['dot','-Tpng','model.dot','-o','CampusCrimes.png'])