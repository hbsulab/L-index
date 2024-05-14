# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 13:57:30 2022

@author: Hasan (In Collaboration with MenQi)
"""
import warnings
warnings.filterwarnings('ignore')
import pandas as pd
import numpy as np
from scipy.linalg import svd
import sys
sys.path.insert(1, "D:/Research/2_CRISPR/Codes/Delemus(L-index)/OldFiles/For2024CSBJSubmission/")
import ImportantFunc as Imp
import time
from datetime import datetime
start_time = time.process_time()
print('Start =', datetime.now().strftime('%H:%M:%S'))

def SAPfunc(MutList,oriAA):
    MutEle = [ele for Mut in MutList for ele in Mut.split(";")]
    M = Imp.count_dups(sorted(MutEle))
    df = pd.DataFrame({'Mutation': M[0],'Count': M[1]})
    df['Ori'] = [x[0] for x in df['Mutation']]
    df['Pos'] = df['Mutation'].astype(str).str.extractall('(\d+)').unstack().fillna('').sum(axis=1).astype(int)
    df['Sites'] = df['Ori'].astype(str) + df['Pos'].astype(str)
    df.sort_values(['Pos'],inplace = True, ascending=True)
    df = df.reset_index(drop=True)
    N_AA = Imp.count_dups( df["Sites"].tolist() )
    dfN_AA = pd.DataFrame({'Sites': N_AA[0],'SAP': N_AA[1]})
    df = pd.merge(pd.DataFrame({'Sites': oriAA}),dfN_AA,on="Sites",how="left").fillna(0)
    df.drop('Sites', inplace=True, axis=1)
    return df

def SVDfunc(A,kk):
    U, s, VT = svd(A)
    r = A.shape[0]
    rs = s.shape[0]
    Au=0.0*A
    
    Sum_s = 0.0
    for i in range(len(s)): Sum_s += s[i]**2
    for j in range(len(s)): s[j] = s[j]**2
    s = s[:6]/Sum_s
    
    for b in range(rs):
        Auu = 0.0
        for k in range(r):
            Auu = Auu + U[k,b]*A[k,:]
        Au[b,:] = Auu
    
    Au = Au[:kk,:]
    r,c = Au.shape
    
    SVDScore = []
    for y in range(c):#loop over columns
        c = 0.0
        for x in range(r):#loop over rows
            c += (Au[x,y]**2)
        SVDScore.append(c**0.5)
    return SVDScore,s
###############################################################################################
dfInput = pd.read_excel('SampleInput.xlsx').dropna().reset_index(drop=True)
print("Current time =", datetime.now().strftime("%H:%M:%S"))
print('TIME TAKEN: ' + str(time.process_time() - start_time) + 's\n')

ref0 = 'MFVFLVLLPLVSSQCVNLTTRTQLPPAYTNSFTRGVYYPDKVFRSSVLHSTQDLFLPFFSNVTWFHAIHVSGTNGTKRFDNPVLPFNDGVYFASTEKSNIIRGWIFGTTLDSKTQSLLIVNNATNVVIKVCEFQFCNDPFLGVYYHKNNKSWMESEFRVYSSANNCTFEYVSQPFLMDLEGKQGNFKNLREFVFKNIDGYFKIYSKHTPINLVRDLPQGFSALEPLVDLPIGINITRFQTLLALHRSYLTPGDSSSGWTAGAAAYYVGYLQPRTFLLKYNENGTITDAVDCALDPLSETKCTLKSFTVEKGIYQTSNFRVQPTESIVRFPNITNLCPFGEVFNATRFASVYAWNRKRISNCVADYSVLYNSASFSTFKCYGVSPTKLNDLCFTNVYADSFVIRGDEVRQIAPGQTGKIADYNYKLPDDFTGCVIAWNSNNLDSKVGGNYNYLYRLFRKSNLKPFERDISTEIYQAGSTPCNGVEGFNCYFPLQSYGFQPTNGVGYQPYRVVVLSFELLHAPATVCGPKKSTNLVKNKCVNFNFNGLTGTGVLTESNKKFLPFQQFGRDIADTTDAVRDPQTLEILDITPCSFGGVSVITPGTNTSNQVAVLYQDVNCTEVPVAIHADQLTPTWRVYSTGSNVFQTRAGCLIGAEHVNNSYECDIPIGAGICASYQTQTNSPRRARSVASQSIIAYTMSLGAENSVAYSNNSIAIPTNFTISVTTEILPVSMTKTSVDCTMYICGDSTECSNLLLQYGSFCTQLNRALTGIAVEQDKNTQEVFAQVKQIYKTPPIKDFGGFNFSQILPDPSKPSKRSFIEDLLFNKVTLADAGFIKQYGDCLGDIAARDLICAQKFNGLTVLPPLLTDEMIAQYTSALLAGTITSGWTFGAGAALQIPFAMQMAYRFNGIGVTQNVLYENQKLIANQFNSAIGKIQDSLSSTASALGKLQDVVNQNAQALNTLVKQLSSNFGAISSVLNDILSRLDKVEAEVQIDRLITGRLQSLQTYVTQQLIRAAEIRASANLAATKMSECVLGQSKRVDFCGKGYHLMSFPQSAPHGVVFLHVTYVPAQEKNFTTAPAICHDGKAHFPREGVFVSNGTHWFVTQRNFYEPQIITTDNTFVSGNCDVVIGIVNNTVYDPLQPELDSFKEELDKYFKNHTSPDVDLGDISGINASVVNIQKEIDRLNEVAKNLNESLIDLQELGKYEQYIKWPWYIWLGFIAGLIAIVMVTIMLCCMTSCCSCLKGCCSCGSCCKFDEDDSEPVLKGVKLHYT'
oriAA = [str(ref0[m]+str(m+1)) for m in range(len(ref0))]
dfSites = pd.DataFrame({'Sites': oriAA})
dfDelemus = dfSites.copy(deep=True)
###############################################################################################
kk = 3 # Number of eigen values
SeqFrame = [0]*1273
Eigen = []
star_month, end_month = 40, 42
for z in range(star_month, end_month+1):
    dfInpMon = dfInput.loc[(dfInput['MonthIndex'] == z)].reset_index(drop=True)
    MutList = dfInpMon['mutation info'].tolist()
    print('iteration -{0} Total Seq = {1}'.format(z,len(MutList)) )
    print("Current time =", datetime.now().strftime("%H:%M:%S"))
    print('TIME TAKEN: ' + str(time.process_time() - start_time) + 's\n')
    """Creating Input SAP"""
    dfSAP = SAPfunc(MutList,oriAA).rename(columns={'SAP':z})
    """Creating Input Matrix"""
    SeqArray = []
    for Seq in MutList:
        SeqInput = list(SeqFrame)
        MutPos = [ ''.join(filter(lambda i: i.isdigit(), Mut)) for Mut in Seq.split(";") ]
        for Pos in MutPos:
            SeqInput[int(Pos)-1] = 1
        SeqArray.append(SeqInput)
    """SVD & deLemus Calculation """
    A = np.nan_to_num(np.array(SeqArray).astype(float))
    SVDScore,s = SVDfunc(A,kk)
    Eigen.append(s)
    dfSVD = pd.DataFrame({z: SVDScore})
    dfDelemus[z] = np.log10( (dfSAP[z]*dfSVD[z]) +1)
###############################################################################################
dfEigen = pd.DataFrame(np.array(Eigen))
dfEigen = dfEigen.rename(columns={old_column_name: i+1 for i, old_column_name in enumerate(dfEigen.columns)})
df = dfEigen.reset_index(drop=True)
dfEigen.index = range(star_month, end_month + 1)
FileProcessing = f'deLemus_Month-{star_month}-{end_month}.xlsx'
with pd.ExcelWriter(FileProcessing) as writer:
    dfDelemus.to_excel(writer, sheet_name='deLemus', index=None)
    dfEigen.to_excel(writer, sheet_name='Top6Eigen')
print("Current time =", datetime.now().strftime("%H:%M:%S"))
print('TIME TAKEN: ' + str(time.process_time() - start_time) + 's\n')