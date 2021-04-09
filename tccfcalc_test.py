"""
    test tccfcalc.dll calculation
"""

import shutil
import os

det_list = ["hpge", "scintil"]
geom_list = ["point", "cylinder", "marinelli"]
nuclide_list = ["co-60", "eu-152"]

def form_infile_name(det, geom, nuclide):
    if len(nuclide) == 0:
        return f"in_files{os.sep}tccfcalc_{det}_{geom}.in"
    else:
        return f"in_files{os.sep}tccfcalc_{det}_{geom}_{nuclide}.in"

def form_outfile_name(det, geom, nuclide):
    if len(nuclide) == 0:
        return f"out_files{os.sep}tccfcalc_{det}_{geom}.out"
    else:
        return f"out_files{os.sep}tccfcalc_{det}_{geom}_{nuclide}.out"
    
def form_resfile_name(det, geom, nuclide):
    if len(nuclide) == 0:
        return f"results{os.sep}tccfcalc_{det}_{geom}.out"
    else:
        return f"results{os.sep}tccfcalc_{det}_{geom}_{nuclide}.out"
        
def form_res_spectrum_name(det, geom, nuclide):
    return f"results{os.sep}spectrum_{det}_{geom}_{nuclide}.spe"
    
def form_res_coincspectrum_name(det, geom, nuclide):
    return f"results{os.sep}spectrum_coinc_{det}_{geom}_{nuclide}.spe"
    
calc_params = {
    'seed': '-s 42', 
    'co-60': '-n Co-60', 
    'eu-152': '-n Eu-152',
    'N10000': '-N 10000',
    }

if __name__ == "__main__":
    # create results directory and copy analyzer.ain
    if not os.path.exists('results'):
        os.mkdir('results')        
    if not os.path.exists('analyzer.ain'):
        shutil.copy("in_files/analyzer_ppd_8k_3MeV.ain", 'analyzer.ain')

    # calculation cycle
    for det in det_list:
        nuclide = ""
        for geom in geom_list:
            tccfcalc_name = form_infile_name(det, geom, nuclide)
            outfname = form_outfile_name(det, geom, nuclide)
            print("calc with:", tccfcalc_name)
            shutil.copy(tccfcalc_name, "tccfcalc.in")
            os.system(' '.join(["effcalc.exe -q", calc_params['seed']]))
            os.system(f"out_cmp.exe tccfcalc.out {outfname}")
            shutil.copy("tccfcalc.out", form_resfile_name(det, geom, nuclide))
            
        geom = "point"
        for nuclide in nuclide_list:
            tccfcalc_name = form_infile_name(det, geom, nuclide)
            outfname = form_outfile_name(det, geom, nuclide)
            print("calc with:", tccfcalc_name)
            shutil.copy(tccfcalc_name, "tccfcalc.in")
            os.system(' '.join(["effcalc.exe -q", calc_params['seed'], calc_params[nuclide]]))
            os.system(f"out_cmp.exe tccfcalc.out {outfname}")
            shutil.copy("tccfcalc.out", form_resfile_name(det, geom, nuclide))
            shutil.copy("test_spectr.spe", form_res_spectrum_name(det, geom, nuclide))
            shutil.copy("test_spectr_coi.spe", form_res_coincspectrum_name(det, geom, nuclide))
            
            
            
            