#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SLiCAP module with symbolic math functions executed by maxima CAS.

Imported by the module **SLiCAPplots.py**.
"""
from SLiCAP.SLiCAPmatrices import *
from mpmath import polyroots

MAXIMAFUNCTIONS = 'load("' + ini.installPath + 'SLiCAPmaxima/SLiCAP.mac");\n'

def python2maxima(expr):
    """
    Converts a sympy expression into a Maxima expression.

    :param expr: sympy expression
    :type expr: sympy.Ex

    :return: maxima expression
    :rtype: str
    """
    expr = str(expr) + ' ' # Add a space for expressions ending with pi, e, E or I
    # Remove extra brackets in matrix
    expr = re.sub(r'Matrix\(\[\[(.*)\]\]\)', r'matrix([\1])', expr)
    # Replace exp(1): e or E with %e
    expr = re.sub(r'([+-/\*^\(])[eE]([\s\)+-/\*^])', r'\1%e\2', expr)
    # Replace pi with %pi
    expr = re.sub(r'([+-/\*^\(])pi([\s\)+-/\*^])', r'\1%pi\2', expr)
    # Replace 1j or I with %i
    expr = re.sub(r'([0-9])j', r'\1*%i', expr)
    expr = re.sub(r'([+-/\*^\(\s])I([\s\)+-/\*^])', r'\1%i\2', expr)
    # Replace the sign() function with the signum() function
    expr = re.sub(r'sign(\(.*\))', r'signum\1', expr)
    return expr

def maxima2python(expr):
    """
    Converts a maxima expression into string that can be converted into a sympy expression.

    :param expr: maxima expression
    :type expr: str

    :return: sympy compatible expression
    :rtype: str
    """
    # Convert big float notation '12345b+123' to float notation '12345e+123':
    expr = re.sub(r'(([+-]?)(\d+)(\.?)(\d*))b(([+-]?)(\d+))', r'\1e\6', expr)
    # Convert complex number notation:
    expr = re.sub(r'%i','1j', expr)
    # Convert 'e' notation:
    expr = re.sub(r'%e','exp(1)', expr)
    # Convert 'pi' notation:
    expr = re.sub(r'%pi','pi', expr)
    # Convert Maxima matrix to sympy matrix:
    expr = re.sub(r'matrix\(\[(.*)\]\)', r'Matrix([[\1]])', expr)
    # Replace the signum() function with the sign() function
    expr = re.sub(r'signum(\(.*\))', r'sign\1', expr)
    return expr

def maxEval(maxExpr):
    """
    Evaluates the expression 'maxExpr' with Maxima CAS and returns the result.

    Starts a subprocess that evaluates maxExpr with Maxima CAS and returns the
    resulting expression in text format. The variable that needs to be output
    must be named: 'result'.

    In some cases Maxima CAS will ask for extra input.
    This will be ignored and a time out will kill the subprocess.

    :param maxExpr: Expression in Maxima format to be evaluated.
    :type maxExpr: str

    :return: String that can be converted into a sympy expression.
    :rtype: str

    Example:

    >>> maxEval("result:ilt(1/(s^2 + a^2), s, t);")
    'sin(a*t)/a'
    """
    #maxAssume = "assume_pos:true$assume_pos_pred:symbolp$ratprint:false$"
    maxStringConv = "stringdisp:true$string(result);"
    maxInput = maxExpr + maxStringConv
    maxInput=maxInput.replace('\n',' ') # Windows cannot handle \n in input!
    # Read the output
    try:
        output = subprocess.run([ini.maxima, '--very-quiet', '-batch-string', maxInput], capture_output=True, timeout=ini.MaximaTimeOut, text=True)
        result = output.stdout.split('"')[-2] # The quoted string is the result of the calculation
        result = result.replace('\\\n', '')   # Remove the maxima newline characters from this result
        result = maxima2python(result)        # Convert the maxima output into a string that can be 'sympified' by python
    except:
        print("""\nMaxima calculation failed or timed out. A time-out occurs if maxima requires additional input, or if maxima requires more time. 
The latter case can be solved by increasing the time limit using the command: 'ini.MaximaTimeOut=nnn', where nnn is the number of seconds.\n""")
        result = output
    return result

def maxLimit(expr, var, val, pm, numeric = True):
    """
    Calculates the limit of an expression for 'var' approaches 'val' from 'pm'.

    :param expr: Expression of which the limit must be evaluated.
    :type expr: sympy.Expr, str
    :param var: Variable that should approach the limit value.
    :type var: sympy.Symbol, str
    :param val: Limit value of the variable.
    :type val:  sympy.Symbol, str, sp.Expr, int, float
    :param pm: Direction: 'plus' or 'minus'
    :type pm: str
    :param numeric: True will force Maxima to use (big) floats for numeric
                    values.
    :type numeric: bool

    :return: Calculated limit
    :rtype: sympy.Expr
    """
    if numeric:
        numeric = 'bfloat'
    else:
        numeric = ''
    maxExpr = 'result:%s(limit(' + str(expr) + ',' + str(var) + ',' + str(val) + ',' + pm +' ));'%(numeric)
    result = maxEval(maxExpr)
    try:
        return sp.sympify(result)
    except:
        print('Maxima error:', result)

def maxIntegrate(expr, var, start = None, stop = None, numeric = True):
    """
    Calculates definite or indefinite integral of 'expr'.

    :param expr: Integrand
    :type expr: sympy.Expr

    :param var: Integration variable
    :type var: sympy.Symbol, str

    :param start: Lower limit of the integral.
    :type start: Bool, int float, sympy.Expr

    :param stop: Upper limit of the integral.
    :type stop: Bool, int float, sympy.Expr

    :param numeric: True will force Maxima to use (big) floats for numeric
                    values.
    :type numeric: bool

    :return: Integral
    :rtype: sympy.Expr
    """
    if numeric:
        numeric = 'bfloat'
        expr=sp.N(expr)
    else:
        numeric = ''
    
    if start != None and stop != None:
        maxExpr = 'result:%s(integrate(%s, %s, %s, %s));'%(numeric, str(expr), str(var), str(start), str(stop))
    else:
        maxExpr = 'result:%s(integrate(%s, %s));'%(numeric, str(expr), str(var))
    result = maxEval(maxExpr)
    try:
        result = sp.sympify(result)
    except:
        print("Error: could not integrate expression: '{0}'.".format(str(expr)))
        result = sp.sympify('Error')
    return result

def rmsNoise(noiseResult, noise, fmin, fmax, source = None):
    """
    Calculates the RMS source-referred noise or detector-referred noise,
    or the contribution of a specific noise source to it.

    :param noiseResult: Results of the execution of an instruction with data type 'noise'.
    :type noiseResult: SLiCAPprotos.allResults

    :param noise: 'inoise' or 'onoise' for source-referred noise or detector-
                  referred noise, respectively.
    :type noise': str

    :param fmin: Lower limit of the frequency range in Hz.
    :type fmin: str, int, float, sp.Symbol

    :param fmax: Upper limit of the frequency range in Hz.
    :type fmax: str, int, float, sp.Symbol

    :param source: 'all' or refDes (ID) of a noise source of which the
                   contribution to the RMS noise needs to be evaluated. Only
                   IDs of current of voltage sources with a nonzero value
                   for 'noise' are accepted.
    :return: RMS noise over the frequency interval.

             - An expression or value if parameter stepping of the instruction is disabled.
             - A list with expressions or values if parameter stepping of the instruction is enabled.
    :rtype: int, float, sympy.Expr, list
    """
    errors = 0
    if fmin == None or fmax == None:
        print("Error in frequency range specification.")
        errors += 1
    fMi = checkNumber(fmin)
    fMa = checkNumber(fmax)
    if fMi != None:
        # Numeric value for fmin
        fmin = fMi
    if fMa != None: 
        # Numeric value for fmax
        fmax = fMa
    if fMi != None and  fMa != None and fmin >= fmax:
        # Numeric values for fmin and fmax but fmin >= fmax
        print("Error in frequency range specification.")
        errors += 1
    elif noiseResult.dataType != 'noise':
        print("Error: expected dataType noise, got: '{0}'.".format(noiseResult.dataType))
        errors += 1
    if errors == 0:
        keys = list(noiseResult.onoiseTerms.keys())
        if noise == 'inoise':
            if source == None:
                noiseData = noiseResult.inoise
            elif source in keys:
                noiseData = noiseResult.inoiseTerms[source]
            else:
                print("Error: unknown noise source: '{0}'.".format(source))
                errors += 1
        elif noise == 'onoise':
            if source == None:
                noiseData = noiseResult.onoise
            elif source in keys:
                noiseData = noiseResult.onoiseTerms[source]
            else:
                print("Error: unknown noise source: '{0}'.".format(source))
                errors += 1
        else:
            print("Error: unknown noise type: '{0}'.".format(noise))
            errors += 1
        if errors == 0:
            if type(noiseData) != list:
                noiseData = [noiseData]
            rms =  np.array([sp.N(sp.sqrt(maxIntegrate(noiseData[i], ini.frequency, start=fmin, stop=fmax, numeric=noiseResult.simType))) for i in range(len(noiseData))])
            if len(rms) == 1:
                rms = rms[0]
            return rms

if __name__ == '__main__':
    x = sp.Symbol('x')
    y = (1+2*x+3*x**2)/(x*sp.exp(10)+2/sp.pi)
    print(maxIntegrate(y,x, numeric=False))