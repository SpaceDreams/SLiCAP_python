v 20130925 2
C 44100 44300 1 0 0 Comparator.sym
{
T 44600 45000 5 10 1 1 0 0 1
refdes=X5
}
C 41400 40100 0 0 0 Noqsi-title-B.sym
{
T 51400 40600 15 10 1 1 0 0 1
date=20161208
T 55300 40600 15 10 1 1 0 0 1
rev=1.1
T 56800 40300 15 10 1 1 0 0 1
auth=jpd@noqsi.com
T 51600 40900 15 8 1 1 0 0 1
fname=DISCRI.sch
T 54600 41300 15 14 1 1 0 4 1
title=Two level pulse height discriminator
}
C 46000 44100 1 0 0 RSFF1-1.sym
{
T 47300 45000 5 10 1 1 0 6 1
refdes=X6
T 46300 46000 5 10 0 0 0 0 1
symversion=1.0
}
C 50200 43800 1 0 0 EDFFP-1.sym
{
T 51500 45400 5 10 1 1 0 6 1
refdes=X7
T 50500 46500 5 10 0 0 0 0 1
symversion=1.0
}
C 45900 48800 1 0 0 INV1P-1.sym
{
T 46300 49400 5 10 1 1 0 0 1
refdes=X9
T 46700 49500 5 10 0 0 0 0 1
symversion=1.0
}
C 44000 47500 1 0 0 Comparator.sym
{
T 44500 48200 5 10 1 1 0 0 1
refdes=X1
}
C 45900 47300 1 0 0 RSFF1-1.sym
{
T 46200 49200 5 10 0 0 0 0 1
symversion=1.0
T 47200 48200 5 10 1 1 0 6 1
refdes=X2
}
C 50100 47000 1 0 0 EDFFP-1.sym
{
T 50400 49700 5 10 0 0 0 0 1
symversion=1.0
T 51400 48600 5 10 1 1 0 6 1
refdes=X3
}
N 45000 47900 45900 47900 4
{
T 45300 48000 5 10 1 1 0 0 1
netname=LLC
}
N 45900 47900 45900 49100 4
N 45100 44700 46000 44700 4
{
T 45900 44800 5 10 1 1 0 0 1
netname=HLC
}
N 47600 44700 50200 44700 4
N 47000 49100 49600 49100 4
N 49600 49100 49600 45100 4
N 49600 45100 50200 45100 4
N 50100 48300 49600 48300 4
C 43900 43400 1 180 1 BIAS1-1.sym
{
T 44300 42600 5 10 1 1 180 6 1
refdes=X10
T 44200 41800 5 10 0 0 180 6 1
symversion=1.0
}
N 45300 43200 45300 47500 4
N 45300 47500 44500 47500 4
N 44600 44300 45300 44300 4
C 43000 43100 1 0 0 resistor-1.sym
{
T 43200 43400 5 10 1 1 0 0 1
refdes=R1
T 43300 42900 5 10 1 1 0 0 1
value=15k
}
C 42800 43400 1 0 0 Vdd.sym
N 43000 43200 43000 43400 4
C 51100 43600 1 0 0 Vdd1.sym
N 51300 43600 51000 43600 4
N 51000 43600 51000 43800 4
C 51000 46700 1 0 0 Vdd1.sym
N 51200 46700 50900 46700 4
N 50900 46700 50900 47000 4
C 45500 41400 1 0 0 INV1P-1.sym
{
T 45900 42000 5 10 1 1 0 0 1
refdes=X11
T 46300 42100 5 10 0 0 0 0 1
symversion=1.0
}
C 46600 41400 1 0 0 INV1P-1.sym
{
T 47000 42000 5 10 1 1 0 0 1
refdes=X12
T 47400 42100 5 10 0 0 0 0 1
symversion=1.0
}
N 47700 41700 49900 41700 4
N 49900 41700 49900 47500 4
N 49900 47500 50100 47500 4
C 52600 47200 1 0 0 INV1P-1.sym
{
T 53000 47800 5 10 1 1 0 0 1
refdes=X4
T 53400 47900 5 10 0 0 0 0 1
symversion=1.0
}
N 52600 47500 51700 47500 4
C 52700 44000 1 0 0 INV1P-1.sym
{
T 53100 44600 5 10 1 1 0 0 1
refdes=X8
T 53500 44700 5 10 0 0 0 0 1
symversion=1.0
}
N 52700 44300 51800 44300 4
N 50200 44300 49900 44300 4
C 53900 47200 1 0 0 spice-subcircuit-IO-1.sym
{
T 54750 47450 5 10 1 1 0 0 1
refdes=P4
}
C 54000 44000 1 0 0 spice-subcircuit-IO-1.sym
{
T 54850 44250 5 10 1 1 0 0 1
refdes=P5
}
C 44000 41400 1 0 1 spice-subcircuit-IO-1.sym
{
T 43150 41650 5 10 1 1 0 6 1
refdes=P6
}
N 43800 41700 45500 41700 4
{
T 44400 41800 5 10 1 1 0 0 1
netname=CLK
}
C 43700 47800 1 0 1 spice-subcircuit-IO-1.sym
{
T 42850 48050 5 10 1 1 0 6 1
refdes=P1
}
N 44000 48100 43500 48100 4
{
T 43600 48200 5 10 1 1 0 0 1
netname=IN
}
N 44100 44900 43700 44900 4
N 43700 44900 43700 48100 4
C 43700 47400 1 0 1 spice-subcircuit-IO-1.sym
{
T 42850 47650 5 10 1 1 0 6 1
refdes=P2
}
N 44000 47700 43500 47700 4
{
T 43900 47400 5 10 1 1 0 0 1
netname=LL
}
C 43800 44200 1 0 1 spice-subcircuit-IO-1.sym
{
T 42950 44450 5 10 1 1 0 6 1
refdes=P3
}
N 44100 44500 43600 44500 4
{
T 43800 44200 5 10 1 1 0 0 1
netname=HL
}
C 47800 47000 1 0 0 NORP-1.sym
{
T 48300 47700 5 10 1 1 0 0 1
refdes=X13
T 48900 48600 5 10 0 0 0 0 1
symversion=1.0
}
C 47000 45800 1 0 1 NANDP-1.sym
{
T 46600 46600 5 10 1 1 0 6 1
refdes=X14
T 46000 47500 5 10 0 0 0 6 1
symversion=1.0
}
N 47900 47100 47900 44700 4
N 47900 47500 47500 47500 4
N 45900 47500 45700 47500 4
N 45700 44300 45700 47500 4
N 45700 44300 46000 44300 4
N 47000 46400 51900 46400 4
N 51900 46400 51900 47500 4
N 49200 47300 49200 47900 4
N 49200 47900 50100 47900 4
N 47000 46000 52100 46000 4
N 52100 46000 52100 44300 4
C 46600 50200 1 0 0 spice-subcircuit-LL-1.sym
{
T 46700 50600 5 10 1 1 0 0 1
refdes=A1
T 46700 50300 5 10 1 1 0 0 1
model-name=DISCRI
}
C 42300 49000 1 0 0 DISCRI.sym
{
T 43600 50600 5 10 1 1 0 6 1
refdes=X?
T 42600 51700 5 10 0 0 0 0 1
symversion=1.0
T 42300 49000 5 10 0 0 0 0 1
graphical=1
}
N 54100 47500 53700 47500 4
{
T 53800 47600 5 10 1 1 0 0 1
netname=LLP
}
N 54200 44300 53800 44300 4
{
T 53800 44400 5 10 1 1 0 0 1
netname=HLP
}
