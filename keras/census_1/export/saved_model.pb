Г
м Г 
9
Add
x"T
y"T
z"T"
Ttype:
2	
S
AddN
inputs"T*N
sum"T"
Nint(0"
Ttype:
2	

ArgMax

input"T
	dimension"Tidx
output"output_type"
Ttype:
2	"
Tidxtype0:
2	"
output_typetype0	:
2	
x
Assign
ref"T

value"T

output_ref"T"	
Ttype"
validate_shapebool("
use_lockingbool(
p
	AssignAdd
ref"T

value"T

output_ref"T"
Ttype:
2	"
use_lockingbool( 
{
BiasAdd

value"T	
bias"T
output"T"
Ttype:
2	"-
data_formatstringNHWC:
NHWCNCHW
{
BiasAddGrad
out_backprop"T
output"T"
Ttype:
2	"-
data_formatstringNHWC:
NHWCNCHW
R
BroadcastGradientArgs
s0"T
s1"T
r0"T
r1"T"
Ttype0:
2	
8
Cast	
x"SrcT	
y"DstT"
SrcTtype"
DstTtype
8
Const
output"dtype"
valuetensor"
dtypetype
S
DynamicStitch
indices*N
data"T*N
merged"T"
Nint(0"	
Ttype
A
Equal
x"T
y"T
z
"
Ttype:
2	

4
Fill
dims

value"T
output"T"	
Ttype
>
FloorDiv
x"T
y"T
z"T"
Ttype:
2	
7
FloorMod
x"T
y"T
z"T"
Ttype:
2	
?
GreaterEqual
x"T
y"T
z
"
Ttype:
2		
.
Identity

input"T
output"T"	
Ttype
<
	LessEqual
x"T
y"T
z
"
Ttype:
2		
+
Log
x"T
y"T"
Ttype:	
2


LogicalNot
x

y

o
MatMul
a"T
b"T
product"T"
transpose_abool( "
transpose_bbool( "
Ttype:

2
:
Maximum
x"T
y"T
z"T"
Ttype:	
2	

Mean

input"T
reduction_indices"Tidx
output"T"
	keep_dimsbool( "
Ttype:
2	"
Tidxtype0:
2	
e
MergeV2Checkpoints
checkpoint_prefixes
destination_prefix"
delete_old_dirsbool(
:
Minimum
x"T
y"T
z"T"
Ttype:	
2	
<
Mul
x"T
y"T
z"T"
Ttype:
2	
-
Neg
x"T
y"T"
Ttype:
	2	

NoOp
D
NotEqual
x"T
y"T
z
"
Ttype:
2	

M
Pack
values"T*N
output"T"
Nint(0"	
Ttype"
axisint 
C
Placeholder
output"dtype"
dtypetype"
shapeshape:

Prod

input"T
reduction_indices"Tidx
output"T"
	keep_dimsbool( "
Ttype:
2	"
Tidxtype0:
2	
}
RandomUniform

shape"T
output"dtype"
seedint "
seed2int "
dtypetype:
2"
Ttype:
2	
`
Range
start"Tidx
limit"Tidx
delta"Tidx
output"Tidx"
Tidxtype0:
2	
=
RealDiv
x"T
y"T
z"T"
Ttype:
2	
4

Reciprocal
x"T
y"T"
Ttype:
	2	
A
Relu
features"T
activations"T"
Ttype:
2		
S
ReluGrad
	gradients"T
features"T
	backprops"T"
Ttype:
2		
[
Reshape
tensor"T
shape"Tshape
output"T"	
Ttype"
Tshapetype0:
2	
o
	RestoreV2

prefix
tensor_names
shape_and_slices
tensors2dtypes"
dtypes
list(type)(0
l
SaveV2

prefix
tensor_names
shape_and_slices
tensors2dtypes"
dtypes
list(type)(0
?
Select
	condition

t"T
e"T
output"T"	
Ttype
P
Shape

input"T
output"out_type"	
Ttype"
out_typetype0:
2	
H
ShardedFilename
basename	
shard

num_shards
filename
/
Sigmoid
x"T
y"T"
Ttype:	
2
;
SigmoidGrad
x"T
y"T
z"T"
Ttype:	
2
N

StringJoin
inputs*N

output"
Nint(0"
	separatorstring 
5
Sub
x"T
y"T
z"T"
Ttype:
	2	

Sum

input"T
reduction_indices"Tidx
output"T"
	keep_dimsbool( "
Ttype:
2	"
Tidxtype0:
2	
c
Tile

input"T
	multiples"
Tmultiples
output"T"	
Ttype"

Tmultiplestype0:
2	
s

VariableV2
ref"dtype"
shapeshape"
dtypetype"
	containerstring "
shared_namestring "serve*1.3.02v1.3.0-rc2-20-g0787eeeыв
p
dense_1_inputPlaceholder*
dtype0*'
_output_shapes
:џџџџџџџџџ7*
shape:џџџџџџџџџ7
m
dense_1/random_uniform/shapeConst*
valueB"7   d   *
dtype0*
_output_shapes
:
_
dense_1/random_uniform/minConst*
valueB
 *>xIО*
dtype0*
_output_shapes
: 
_
dense_1/random_uniform/maxConst*
_output_shapes
: *
valueB
 *>xI>*
dtype0
Ј
$dense_1/random_uniform/RandomUniformRandomUniformdense_1/random_uniform/shape*
T0*
dtype0*
_output_shapes

:7d*
seed2ѓь*
seedБџх)
z
dense_1/random_uniform/subSubdense_1/random_uniform/maxdense_1/random_uniform/min*
T0*
_output_shapes
: 

dense_1/random_uniform/mulMul$dense_1/random_uniform/RandomUniformdense_1/random_uniform/sub*
_output_shapes

:7d*
T0
~
dense_1/random_uniformAdddense_1/random_uniform/muldense_1/random_uniform/min*
T0*
_output_shapes

:7d

dense_1/kernel
VariableV2*
shape
:7d*
shared_name *
dtype0*
_output_shapes

:7d*
	container 
М
dense_1/kernel/AssignAssigndense_1/kerneldense_1/random_uniform*
T0*!
_class
loc:@dense_1/kernel*
validate_shape(*
_output_shapes

:7d*
use_locking(
{
dense_1/kernel/readIdentitydense_1/kernel*
T0*!
_class
loc:@dense_1/kernel*
_output_shapes

:7d
Z
dense_1/ConstConst*
valueBd*    *
dtype0*
_output_shapes
:d
x
dense_1/bias
VariableV2*
shared_name *
dtype0*
_output_shapes
:d*
	container *
shape:d
Љ
dense_1/bias/AssignAssigndense_1/biasdense_1/Const*
_output_shapes
:d*
use_locking(*
T0*
_class
loc:@dense_1/bias*
validate_shape(
q
dense_1/bias/readIdentitydense_1/bias*
_output_shapes
:d*
T0*
_class
loc:@dense_1/bias

dense_1/MatMulMatMuldense_1_inputdense_1/kernel/read*
T0*'
_output_shapes
:џџџџџџџџџd*
transpose_a( *
transpose_b( 

dense_1/BiasAddBiasAdddense_1/MatMuldense_1/bias/read*'
_output_shapes
:џџџџџџџџџd*
T0*
data_formatNHWC
W
dense_1/ReluReludense_1/BiasAdd*
T0*'
_output_shapes
:џџџџџџџџџd
m
dense_2/random_uniform/shapeConst*
valueB"d   F   *
dtype0*
_output_shapes
:
_
dense_2/random_uniform/minConst*
valueB
 *H`@О*
dtype0*
_output_shapes
: 
_
dense_2/random_uniform/maxConst*
dtype0*
_output_shapes
: *
valueB
 *H`@>
Ј
$dense_2/random_uniform/RandomUniformRandomUniformdense_2/random_uniform/shape*
seedБџх)*
T0*
dtype0*
_output_shapes

:dF*
seed2КЫЕ
z
dense_2/random_uniform/subSubdense_2/random_uniform/maxdense_2/random_uniform/min*
_output_shapes
: *
T0

dense_2/random_uniform/mulMul$dense_2/random_uniform/RandomUniformdense_2/random_uniform/sub*
_output_shapes

:dF*
T0
~
dense_2/random_uniformAdddense_2/random_uniform/muldense_2/random_uniform/min*
T0*
_output_shapes

:dF

dense_2/kernel
VariableV2*
dtype0*
_output_shapes

:dF*
	container *
shape
:dF*
shared_name 
М
dense_2/kernel/AssignAssigndense_2/kerneldense_2/random_uniform*
use_locking(*
T0*!
_class
loc:@dense_2/kernel*
validate_shape(*
_output_shapes

:dF
{
dense_2/kernel/readIdentitydense_2/kernel*
T0*!
_class
loc:@dense_2/kernel*
_output_shapes

:dF
Z
dense_2/ConstConst*
_output_shapes
:F*
valueBF*    *
dtype0
x
dense_2/bias
VariableV2*
shape:F*
shared_name *
dtype0*
_output_shapes
:F*
	container 
Љ
dense_2/bias/AssignAssigndense_2/biasdense_2/Const*
_class
loc:@dense_2/bias*
validate_shape(*
_output_shapes
:F*
use_locking(*
T0
q
dense_2/bias/readIdentitydense_2/bias*
T0*
_class
loc:@dense_2/bias*
_output_shapes
:F

dense_2/MatMulMatMuldense_1/Reludense_2/kernel/read*'
_output_shapes
:џџџџџџџџџF*
transpose_a( *
transpose_b( *
T0

dense_2/BiasAddBiasAdddense_2/MatMuldense_2/bias/read*
T0*
data_formatNHWC*'
_output_shapes
:џџџџџџџџџF
W
dense_2/ReluReludense_2/BiasAdd*'
_output_shapes
:џџџџџџџџџF*
T0
m
dense_3/random_uniform/shapeConst*
valueB"F   2   *
dtype0*
_output_shapes
:
_
dense_3/random_uniform/minConst*
valueB
 *.љdО*
dtype0*
_output_shapes
: 
_
dense_3/random_uniform/maxConst*
valueB
 *.љd>*
dtype0*
_output_shapes
: 
Ј
$dense_3/random_uniform/RandomUniformRandomUniformdense_3/random_uniform/shape*
dtype0*
_output_shapes

:F2*
seed2ђѕї*
seedБџх)*
T0
z
dense_3/random_uniform/subSubdense_3/random_uniform/maxdense_3/random_uniform/min*
T0*
_output_shapes
: 

dense_3/random_uniform/mulMul$dense_3/random_uniform/RandomUniformdense_3/random_uniform/sub*
_output_shapes

:F2*
T0
~
dense_3/random_uniformAdddense_3/random_uniform/muldense_3/random_uniform/min*
T0*
_output_shapes

:F2

dense_3/kernel
VariableV2*
shape
:F2*
shared_name *
dtype0*
_output_shapes

:F2*
	container 
М
dense_3/kernel/AssignAssigndense_3/kerneldense_3/random_uniform*
validate_shape(*
_output_shapes

:F2*
use_locking(*
T0*!
_class
loc:@dense_3/kernel
{
dense_3/kernel/readIdentitydense_3/kernel*
T0*!
_class
loc:@dense_3/kernel*
_output_shapes

:F2
Z
dense_3/ConstConst*
valueB2*    *
dtype0*
_output_shapes
:2
x
dense_3/bias
VariableV2*
shared_name *
dtype0*
_output_shapes
:2*
	container *
shape:2
Љ
dense_3/bias/AssignAssigndense_3/biasdense_3/Const*
use_locking(*
T0*
_class
loc:@dense_3/bias*
validate_shape(*
_output_shapes
:2
q
dense_3/bias/readIdentitydense_3/bias*
T0*
_class
loc:@dense_3/bias*
_output_shapes
:2

dense_3/MatMulMatMuldense_2/Reludense_3/kernel/read*
T0*'
_output_shapes
:џџџџџџџџџ2*
transpose_a( *
transpose_b( 

dense_3/BiasAddBiasAdddense_3/MatMuldense_3/bias/read*
T0*
data_formatNHWC*'
_output_shapes
:џџџџџџџџџ2
W
dense_3/ReluReludense_3/BiasAdd*'
_output_shapes
:џџџџџџџџџ2*
T0
m
dense_4/random_uniform/shapeConst*
valueB"2      *
dtype0*
_output_shapes
:
_
dense_4/random_uniform/minConst*
valueB
 *єхО*
dtype0*
_output_shapes
: 
_
dense_4/random_uniform/maxConst*
valueB
 *єх>*
dtype0*
_output_shapes
: 
Ј
$dense_4/random_uniform/RandomUniformRandomUniformdense_4/random_uniform/shape*
dtype0*
_output_shapes

:2*
seed2НТр*
seedБџх)*
T0
z
dense_4/random_uniform/subSubdense_4/random_uniform/maxdense_4/random_uniform/min*
T0*
_output_shapes
: 

dense_4/random_uniform/mulMul$dense_4/random_uniform/RandomUniformdense_4/random_uniform/sub*
_output_shapes

:2*
T0
~
dense_4/random_uniformAdddense_4/random_uniform/muldense_4/random_uniform/min*
T0*
_output_shapes

:2

dense_4/kernel
VariableV2*
_output_shapes

:2*
	container *
shape
:2*
shared_name *
dtype0
М
dense_4/kernel/AssignAssigndense_4/kerneldense_4/random_uniform*
use_locking(*
T0*!
_class
loc:@dense_4/kernel*
validate_shape(*
_output_shapes

:2
{
dense_4/kernel/readIdentitydense_4/kernel*
_output_shapes

:2*
T0*!
_class
loc:@dense_4/kernel
Z
dense_4/ConstConst*
valueB*    *
dtype0*
_output_shapes
:
x
dense_4/bias
VariableV2*
dtype0*
_output_shapes
:*
	container *
shape:*
shared_name 
Љ
dense_4/bias/AssignAssigndense_4/biasdense_4/Const*
_class
loc:@dense_4/bias*
validate_shape(*
_output_shapes
:*
use_locking(*
T0
q
dense_4/bias/readIdentitydense_4/bias*
T0*
_class
loc:@dense_4/bias*
_output_shapes
:

dense_4/MatMulMatMuldense_3/Reludense_4/kernel/read*'
_output_shapes
:џџџџџџџџџ*
transpose_a( *
transpose_b( *
T0

dense_4/BiasAddBiasAdddense_4/MatMuldense_4/bias/read*
data_formatNHWC*'
_output_shapes
:џџџџџџџџџ*
T0
W
dense_4/ReluReludense_4/BiasAdd*
T0*'
_output_shapes
:џџџџџџџџџ
m
dense_5/random_uniform/shapeConst*
valueB"      *
dtype0*
_output_shapes
:
_
dense_5/random_uniform/minConst*
valueB
 *БП*
dtype0*
_output_shapes
: 
_
dense_5/random_uniform/maxConst*
valueB
 *Б?*
dtype0*
_output_shapes
: 
Ї
$dense_5/random_uniform/RandomUniformRandomUniformdense_5/random_uniform/shape*
dtype0*
_output_shapes

:*
seed2 o*
seedБџх)*
T0
z
dense_5/random_uniform/subSubdense_5/random_uniform/maxdense_5/random_uniform/min*
T0*
_output_shapes
: 

dense_5/random_uniform/mulMul$dense_5/random_uniform/RandomUniformdense_5/random_uniform/sub*
_output_shapes

:*
T0
~
dense_5/random_uniformAdddense_5/random_uniform/muldense_5/random_uniform/min*
_output_shapes

:*
T0

dense_5/kernel
VariableV2*
dtype0*
_output_shapes

:*
	container *
shape
:*
shared_name 
М
dense_5/kernel/AssignAssigndense_5/kerneldense_5/random_uniform*
use_locking(*
T0*!
_class
loc:@dense_5/kernel*
validate_shape(*
_output_shapes

:
{
dense_5/kernel/readIdentitydense_5/kernel*
T0*!
_class
loc:@dense_5/kernel*
_output_shapes

:
Z
dense_5/ConstConst*
valueB*    *
dtype0*
_output_shapes
:
x
dense_5/bias
VariableV2*
_output_shapes
:*
	container *
shape:*
shared_name *
dtype0
Љ
dense_5/bias/AssignAssigndense_5/biasdense_5/Const*
validate_shape(*
_output_shapes
:*
use_locking(*
T0*
_class
loc:@dense_5/bias
q
dense_5/bias/readIdentitydense_5/bias*
T0*
_class
loc:@dense_5/bias*
_output_shapes
:

dense_5/MatMulMatMuldense_4/Reludense_5/kernel/read*
T0*'
_output_shapes
:џџџџџџџџџ*
transpose_a( *
transpose_b( 

dense_5/BiasAddBiasAdddense_5/MatMuldense_5/bias/read*
data_formatNHWC*'
_output_shapes
:џџџџџџџџџ*
T0
]
dense_5/SigmoidSigmoiddense_5/BiasAdd*
T0*'
_output_shapes
:џџџџџџџџџ
^
SGD/iterations/initial_valueConst*
value	B	 R *
dtype0	*
_output_shapes
: 
r
SGD/iterations
VariableV2*
shape: *
shared_name *
dtype0	*
_output_shapes
: *
	container 
К
SGD/iterations/AssignAssignSGD/iterationsSGD/iterations/initial_value*
use_locking(*
T0	*!
_class
loc:@SGD/iterations*
validate_shape(*
_output_shapes
: 
s
SGD/iterations/readIdentitySGD/iterations*
T0	*!
_class
loc:@SGD/iterations*
_output_shapes
: 
Y
SGD/lr/initial_valueConst*
dtype0*
_output_shapes
: *
valueB
 *ЭЬЬ=
j
SGD/lr
VariableV2*
dtype0*
_output_shapes
: *
	container *
shape: *
shared_name 

SGD/lr/AssignAssignSGD/lrSGD/lr/initial_value*
validate_shape(*
_output_shapes
: *
use_locking(*
T0*
_class
loc:@SGD/lr
[
SGD/lr/readIdentitySGD/lr*
T0*
_class
loc:@SGD/lr*
_output_shapes
: 
_
SGD/momentum/initial_valueConst*
valueB
 *    *
dtype0*
_output_shapes
: 
p
SGD/momentum
VariableV2*
shared_name *
dtype0*
_output_shapes
: *
	container *
shape: 
В
SGD/momentum/AssignAssignSGD/momentumSGD/momentum/initial_value*
_class
loc:@SGD/momentum*
validate_shape(*
_output_shapes
: *
use_locking(*
T0
m
SGD/momentum/readIdentitySGD/momentum*
T0*
_class
loc:@SGD/momentum*
_output_shapes
: 
\
SGD/decay/initial_valueConst*
_output_shapes
: *
valueB
 *    *
dtype0
m
	SGD/decay
VariableV2*
shared_name *
dtype0*
_output_shapes
: *
	container *
shape: 
І
SGD/decay/AssignAssign	SGD/decaySGD/decay/initial_value*
_output_shapes
: *
use_locking(*
T0*
_class
loc:@SGD/decay*
validate_shape(
d
SGD/decay/readIdentity	SGD/decay*
T0*
_class
loc:@SGD/decay*
_output_shapes
: 

dense_5_targetPlaceholder*
dtype0*0
_output_shapes
:џџџџџџџџџџџџџџџџџџ*%
shape:џџџџџџџџџџџџџџџџџџ
q
dense_5_sample_weightsPlaceholder*
dtype0*#
_output_shapes
:џџџџџџџџџ*
shape:џџџџџџџџџ
i
'loss/dense_5_loss/Sum/reduction_indicesConst*
value	B :*
dtype0*
_output_shapes
: 
Ѕ
loss/dense_5_loss/SumSumdense_5/Sigmoid'loss/dense_5_loss/Sum/reduction_indices*
T0*'
_output_shapes
:џџџџџџџџџ*
	keep_dims(*

Tidx0
z
loss/dense_5_loss/divRealDivdense_5/Sigmoidloss/dense_5_loss/Sum*'
_output_shapes
:џџџџџџџџџ*
T0
\
loss/dense_5_loss/ConstConst*
valueB
 *Пж3*
dtype0*
_output_shapes
: 
\
loss/dense_5_loss/sub/xConst*
valueB
 *  ?*
dtype0*
_output_shapes
: 
o
loss/dense_5_loss/subSubloss/dense_5_loss/sub/xloss/dense_5_loss/Const*
T0*
_output_shapes
: 

'loss/dense_5_loss/clip_by_value/MinimumMinimumloss/dense_5_loss/divloss/dense_5_loss/sub*
T0*'
_output_shapes
:џџџџџџџџџ

loss/dense_5_loss/clip_by_valueMaximum'loss/dense_5_loss/clip_by_value/Minimumloss/dense_5_loss/Const*
T0*'
_output_shapes
:џџџџџџџџџ
o
loss/dense_5_loss/LogLogloss/dense_5_loss/clip_by_value*
T0*'
_output_shapes
:џџџџџџџџџ
u
loss/dense_5_loss/mulMuldense_5_targetloss/dense_5_loss/Log*
T0*'
_output_shapes
:џџџџџџџџџ
k
)loss/dense_5_loss/Sum_1/reduction_indicesConst*
value	B :*
dtype0*
_output_shapes
: 
Ћ
loss/dense_5_loss/Sum_1Sumloss/dense_5_loss/mul)loss/dense_5_loss/Sum_1/reduction_indices*#
_output_shapes
:џџџџџџџџџ*
	keep_dims( *

Tidx0*
T0
c
loss/dense_5_loss/NegNegloss/dense_5_loss/Sum_1*
T0*#
_output_shapes
:џџџџџџџџџ
k
(loss/dense_5_loss/Mean/reduction_indicesConst*
valueB *
dtype0*
_output_shapes
: 
Њ
loss/dense_5_loss/MeanMeanloss/dense_5_loss/Neg(loss/dense_5_loss/Mean/reduction_indices*
	keep_dims( *

Tidx0*
T0*#
_output_shapes
:џџџџџџџџџ
|
loss/dense_5_loss/mul_1Mulloss/dense_5_loss/Meandense_5_sample_weights*
T0*#
_output_shapes
:џџџџџџџџџ
a
loss/dense_5_loss/NotEqual/yConst*
valueB
 *    *
dtype0*
_output_shapes
: 

loss/dense_5_loss/NotEqualNotEqualdense_5_sample_weightsloss/dense_5_loss/NotEqual/y*#
_output_shapes
:џџџџџџџџџ*
T0
w
loss/dense_5_loss/CastCastloss/dense_5_loss/NotEqual*

SrcT0
*#
_output_shapes
:џџџџџџџџџ*

DstT0
c
loss/dense_5_loss/Const_1Const*
valueB: *
dtype0*
_output_shapes
:

loss/dense_5_loss/Mean_1Meanloss/dense_5_loss/Castloss/dense_5_loss/Const_1*
	keep_dims( *

Tidx0*
T0*
_output_shapes
: 

loss/dense_5_loss/div_1RealDivloss/dense_5_loss/mul_1loss/dense_5_loss/Mean_1*
T0*#
_output_shapes
:џџџџџџџџџ
c
loss/dense_5_loss/Const_2Const*
_output_shapes
:*
valueB: *
dtype0

loss/dense_5_loss/Mean_2Meanloss/dense_5_loss/div_1loss/dense_5_loss/Const_2*
_output_shapes
: *
	keep_dims( *

Tidx0*
T0
O

loss/mul/xConst*
valueB
 *  ?*
dtype0*
_output_shapes
: 
V
loss/mulMul
loss/mul/xloss/dense_5_loss/Mean_2*
T0*
_output_shapes
: 
g
metrics/acc/ArgMax/dimensionConst*
valueB :
џџџџџџџџџ*
dtype0*
_output_shapes
: 

metrics/acc/ArgMaxArgMaxdense_5_targetmetrics/acc/ArgMax/dimension*#
_output_shapes
:џџџџџџџџџ*

Tidx0*
T0*
output_type0	
i
metrics/acc/ArgMax_1/dimensionConst*
valueB :
џџџџџџџџџ*
dtype0*
_output_shapes
: 

metrics/acc/ArgMax_1ArgMaxdense_5/Sigmoidmetrics/acc/ArgMax_1/dimension*

Tidx0*
T0*
output_type0	*#
_output_shapes
:џџџџџџџџџ
r
metrics/acc/EqualEqualmetrics/acc/ArgMaxmetrics/acc/ArgMax_1*
T0	*#
_output_shapes
:џџџџџџџџџ
h
metrics/acc/CastCastmetrics/acc/Equal*

SrcT0
*#
_output_shapes
:џџџџџџџџџ*

DstT0
[
metrics/acc/ConstConst*
valueB: *
dtype0*
_output_shapes
:
{
metrics/acc/MeanMeanmetrics/acc/Castmetrics/acc/Const*
_output_shapes
: *
	keep_dims( *

Tidx0*
T0
|
training/SGD/gradients/ShapeConst*
dtype0*
_output_shapes
: *
valueB *
_class
loc:@loss/mul
~
training/SGD/gradients/ConstConst*
valueB
 *  ?*
_class
loc:@loss/mul*
dtype0*
_output_shapes
: 

training/SGD/gradients/FillFilltraining/SGD/gradients/Shapetraining/SGD/gradients/Const*
_output_shapes
: *
T0*
_class
loc:@loss/mul

*training/SGD/gradients/loss/mul_grad/ShapeConst*
dtype0*
_output_shapes
: *
valueB *
_class
loc:@loss/mul

,training/SGD/gradients/loss/mul_grad/Shape_1Const*
valueB *
_class
loc:@loss/mul*
dtype0*
_output_shapes
: 

:training/SGD/gradients/loss/mul_grad/BroadcastGradientArgsBroadcastGradientArgs*training/SGD/gradients/loss/mul_grad/Shape,training/SGD/gradients/loss/mul_grad/Shape_1*
T0*
_class
loc:@loss/mul*2
_output_shapes 
:џџџџџџџџџ:џџџџџџџџџ
Є
(training/SGD/gradients/loss/mul_grad/mulMultraining/SGD/gradients/Fillloss/dense_5_loss/Mean_2*
T0*
_class
loc:@loss/mul*
_output_shapes
: 
ђ
(training/SGD/gradients/loss/mul_grad/SumSum(training/SGD/gradients/loss/mul_grad/mul:training/SGD/gradients/loss/mul_grad/BroadcastGradientArgs*
_output_shapes
:*

Tidx0*
	keep_dims( *
T0*
_class
loc:@loss/mul
й
,training/SGD/gradients/loss/mul_grad/ReshapeReshape(training/SGD/gradients/loss/mul_grad/Sum*training/SGD/gradients/loss/mul_grad/Shape*
T0*
Tshape0*
_class
loc:@loss/mul*
_output_shapes
: 

*training/SGD/gradients/loss/mul_grad/mul_1Mul
loss/mul/xtraining/SGD/gradients/Fill*
_output_shapes
: *
T0*
_class
loc:@loss/mul
ј
*training/SGD/gradients/loss/mul_grad/Sum_1Sum*training/SGD/gradients/loss/mul_grad/mul_1<training/SGD/gradients/loss/mul_grad/BroadcastGradientArgs:1*
T0*
_class
loc:@loss/mul*
_output_shapes
:*

Tidx0*
	keep_dims( 
п
.training/SGD/gradients/loss/mul_grad/Reshape_1Reshape*training/SGD/gradients/loss/mul_grad/Sum_1,training/SGD/gradients/loss/mul_grad/Shape_1*
T0*
Tshape0*
_class
loc:@loss/mul*
_output_shapes
: 
Й
Btraining/SGD/gradients/loss/dense_5_loss/Mean_2_grad/Reshape/shapeConst*
valueB:*+
_class!
loc:@loss/dense_5_loss/Mean_2*
dtype0*
_output_shapes
:

<training/SGD/gradients/loss/dense_5_loss/Mean_2_grad/ReshapeReshape.training/SGD/gradients/loss/mul_grad/Reshape_1Btraining/SGD/gradients/loss/dense_5_loss/Mean_2_grad/Reshape/shape*
T0*
Tshape0*+
_class!
loc:@loss/dense_5_loss/Mean_2*
_output_shapes
:
О
:training/SGD/gradients/loss/dense_5_loss/Mean_2_grad/ShapeShapeloss/dense_5_loss/div_1*
T0*
out_type0*+
_class!
loc:@loss/dense_5_loss/Mean_2*
_output_shapes
:
Ј
9training/SGD/gradients/loss/dense_5_loss/Mean_2_grad/TileTile<training/SGD/gradients/loss/dense_5_loss/Mean_2_grad/Reshape:training/SGD/gradients/loss/dense_5_loss/Mean_2_grad/Shape*

Tmultiples0*
T0*+
_class!
loc:@loss/dense_5_loss/Mean_2*#
_output_shapes
:џџџџџџџџџ
Р
<training/SGD/gradients/loss/dense_5_loss/Mean_2_grad/Shape_1Shapeloss/dense_5_loss/div_1*
T0*
out_type0*+
_class!
loc:@loss/dense_5_loss/Mean_2*
_output_shapes
:
Ќ
<training/SGD/gradients/loss/dense_5_loss/Mean_2_grad/Shape_2Const*
valueB *+
_class!
loc:@loss/dense_5_loss/Mean_2*
dtype0*
_output_shapes
: 
Б
:training/SGD/gradients/loss/dense_5_loss/Mean_2_grad/ConstConst*
valueB: *+
_class!
loc:@loss/dense_5_loss/Mean_2*
dtype0*
_output_shapes
:
І
9training/SGD/gradients/loss/dense_5_loss/Mean_2_grad/ProdProd<training/SGD/gradients/loss/dense_5_loss/Mean_2_grad/Shape_1:training/SGD/gradients/loss/dense_5_loss/Mean_2_grad/Const*

Tidx0*
	keep_dims( *
T0*+
_class!
loc:@loss/dense_5_loss/Mean_2*
_output_shapes
: 
Г
<training/SGD/gradients/loss/dense_5_loss/Mean_2_grad/Const_1Const*
valueB: *+
_class!
loc:@loss/dense_5_loss/Mean_2*
dtype0*
_output_shapes
:
Њ
;training/SGD/gradients/loss/dense_5_loss/Mean_2_grad/Prod_1Prod<training/SGD/gradients/loss/dense_5_loss/Mean_2_grad/Shape_2<training/SGD/gradients/loss/dense_5_loss/Mean_2_grad/Const_1*+
_class!
loc:@loss/dense_5_loss/Mean_2*
_output_shapes
: *

Tidx0*
	keep_dims( *
T0
­
>training/SGD/gradients/loss/dense_5_loss/Mean_2_grad/Maximum/yConst*
value	B :*+
_class!
loc:@loss/dense_5_loss/Mean_2*
dtype0*
_output_shapes
: 

<training/SGD/gradients/loss/dense_5_loss/Mean_2_grad/MaximumMaximum;training/SGD/gradients/loss/dense_5_loss/Mean_2_grad/Prod_1>training/SGD/gradients/loss/dense_5_loss/Mean_2_grad/Maximum/y*+
_class!
loc:@loss/dense_5_loss/Mean_2*
_output_shapes
: *
T0

=training/SGD/gradients/loss/dense_5_loss/Mean_2_grad/floordivFloorDiv9training/SGD/gradients/loss/dense_5_loss/Mean_2_grad/Prod<training/SGD/gradients/loss/dense_5_loss/Mean_2_grad/Maximum*
_output_shapes
: *
T0*+
_class!
loc:@loss/dense_5_loss/Mean_2
н
9training/SGD/gradients/loss/dense_5_loss/Mean_2_grad/CastCast=training/SGD/gradients/loss/dense_5_loss/Mean_2_grad/floordiv*
_output_shapes
: *

DstT0*

SrcT0*+
_class!
loc:@loss/dense_5_loss/Mean_2

<training/SGD/gradients/loss/dense_5_loss/Mean_2_grad/truedivRealDiv9training/SGD/gradients/loss/dense_5_loss/Mean_2_grad/Tile9training/SGD/gradients/loss/dense_5_loss/Mean_2_grad/Cast*#
_output_shapes
:џџџџџџџџџ*
T0*+
_class!
loc:@loss/dense_5_loss/Mean_2
М
9training/SGD/gradients/loss/dense_5_loss/div_1_grad/ShapeShapeloss/dense_5_loss/mul_1*
T0*
out_type0**
_class 
loc:@loss/dense_5_loss/div_1*
_output_shapes
:
Њ
;training/SGD/gradients/loss/dense_5_loss/div_1_grad/Shape_1Const*
valueB **
_class 
loc:@loss/dense_5_loss/div_1*
dtype0*
_output_shapes
: 
У
Itraining/SGD/gradients/loss/dense_5_loss/div_1_grad/BroadcastGradientArgsBroadcastGradientArgs9training/SGD/gradients/loss/dense_5_loss/div_1_grad/Shape;training/SGD/gradients/loss/dense_5_loss/div_1_grad/Shape_1*
T0**
_class 
loc:@loss/dense_5_loss/div_1*2
_output_shapes 
:џџџџџџџџџ:џџџџџџџџџ
ј
;training/SGD/gradients/loss/dense_5_loss/div_1_grad/RealDivRealDiv<training/SGD/gradients/loss/dense_5_loss/Mean_2_grad/truedivloss/dense_5_loss/Mean_1*
T0**
_class 
loc:@loss/dense_5_loss/div_1*#
_output_shapes
:џџџџџџџџџ
В
7training/SGD/gradients/loss/dense_5_loss/div_1_grad/SumSum;training/SGD/gradients/loss/dense_5_loss/div_1_grad/RealDivItraining/SGD/gradients/loss/dense_5_loss/div_1_grad/BroadcastGradientArgs*
_output_shapes
:*

Tidx0*
	keep_dims( *
T0**
_class 
loc:@loss/dense_5_loss/div_1
Ђ
;training/SGD/gradients/loss/dense_5_loss/div_1_grad/ReshapeReshape7training/SGD/gradients/loss/dense_5_loss/div_1_grad/Sum9training/SGD/gradients/loss/dense_5_loss/div_1_grad/Shape*#
_output_shapes
:џџџџџџџџџ*
T0*
Tshape0**
_class 
loc:@loss/dense_5_loss/div_1
Б
7training/SGD/gradients/loss/dense_5_loss/div_1_grad/NegNegloss/dense_5_loss/mul_1*
T0**
_class 
loc:@loss/dense_5_loss/div_1*#
_output_shapes
:џџџџџџџџџ
ѕ
=training/SGD/gradients/loss/dense_5_loss/div_1_grad/RealDiv_1RealDiv7training/SGD/gradients/loss/dense_5_loss/div_1_grad/Negloss/dense_5_loss/Mean_1*
T0**
_class 
loc:@loss/dense_5_loss/div_1*#
_output_shapes
:џџџџџџџџџ
ћ
=training/SGD/gradients/loss/dense_5_loss/div_1_grad/RealDiv_2RealDiv=training/SGD/gradients/loss/dense_5_loss/div_1_grad/RealDiv_1loss/dense_5_loss/Mean_1**
_class 
loc:@loss/dense_5_loss/div_1*#
_output_shapes
:џџџџџџџџџ*
T0

7training/SGD/gradients/loss/dense_5_loss/div_1_grad/mulMul<training/SGD/gradients/loss/dense_5_loss/Mean_2_grad/truediv=training/SGD/gradients/loss/dense_5_loss/div_1_grad/RealDiv_2*
T0**
_class 
loc:@loss/dense_5_loss/div_1*#
_output_shapes
:џџџџџџџџџ
В
9training/SGD/gradients/loss/dense_5_loss/div_1_grad/Sum_1Sum7training/SGD/gradients/loss/dense_5_loss/div_1_grad/mulKtraining/SGD/gradients/loss/dense_5_loss/div_1_grad/BroadcastGradientArgs:1*
_output_shapes
:*

Tidx0*
	keep_dims( *
T0**
_class 
loc:@loss/dense_5_loss/div_1

=training/SGD/gradients/loss/dense_5_loss/div_1_grad/Reshape_1Reshape9training/SGD/gradients/loss/dense_5_loss/div_1_grad/Sum_1;training/SGD/gradients/loss/dense_5_loss/div_1_grad/Shape_1*
T0*
Tshape0**
_class 
loc:@loss/dense_5_loss/div_1*
_output_shapes
: 
Л
9training/SGD/gradients/loss/dense_5_loss/mul_1_grad/ShapeShapeloss/dense_5_loss/Mean*
T0*
out_type0**
_class 
loc:@loss/dense_5_loss/mul_1*
_output_shapes
:
Н
;training/SGD/gradients/loss/dense_5_loss/mul_1_grad/Shape_1Shapedense_5_sample_weights*
_output_shapes
:*
T0*
out_type0**
_class 
loc:@loss/dense_5_loss/mul_1
У
Itraining/SGD/gradients/loss/dense_5_loss/mul_1_grad/BroadcastGradientArgsBroadcastGradientArgs9training/SGD/gradients/loss/dense_5_loss/mul_1_grad/Shape;training/SGD/gradients/loss/dense_5_loss/mul_1_grad/Shape_1*
T0**
_class 
loc:@loss/dense_5_loss/mul_1*2
_output_shapes 
:џџџџџџџџџ:џџџџџџџџџ
э
7training/SGD/gradients/loss/dense_5_loss/mul_1_grad/mulMul;training/SGD/gradients/loss/dense_5_loss/div_1_grad/Reshapedense_5_sample_weights*
T0**
_class 
loc:@loss/dense_5_loss/mul_1*#
_output_shapes
:џџџџџџџџџ
Ў
7training/SGD/gradients/loss/dense_5_loss/mul_1_grad/SumSum7training/SGD/gradients/loss/dense_5_loss/mul_1_grad/mulItraining/SGD/gradients/loss/dense_5_loss/mul_1_grad/BroadcastGradientArgs*
_output_shapes
:*

Tidx0*
	keep_dims( *
T0**
_class 
loc:@loss/dense_5_loss/mul_1
Ђ
;training/SGD/gradients/loss/dense_5_loss/mul_1_grad/ReshapeReshape7training/SGD/gradients/loss/dense_5_loss/mul_1_grad/Sum9training/SGD/gradients/loss/dense_5_loss/mul_1_grad/Shape*
T0*
Tshape0**
_class 
loc:@loss/dense_5_loss/mul_1*#
_output_shapes
:џџџџџџџџџ
я
9training/SGD/gradients/loss/dense_5_loss/mul_1_grad/mul_1Mulloss/dense_5_loss/Mean;training/SGD/gradients/loss/dense_5_loss/div_1_grad/Reshape*
T0**
_class 
loc:@loss/dense_5_loss/mul_1*#
_output_shapes
:џџџџџџџџџ
Д
9training/SGD/gradients/loss/dense_5_loss/mul_1_grad/Sum_1Sum9training/SGD/gradients/loss/dense_5_loss/mul_1_grad/mul_1Ktraining/SGD/gradients/loss/dense_5_loss/mul_1_grad/BroadcastGradientArgs:1**
_class 
loc:@loss/dense_5_loss/mul_1*
_output_shapes
:*

Tidx0*
	keep_dims( *
T0
Ј
=training/SGD/gradients/loss/dense_5_loss/mul_1_grad/Reshape_1Reshape9training/SGD/gradients/loss/dense_5_loss/mul_1_grad/Sum_1;training/SGD/gradients/loss/dense_5_loss/mul_1_grad/Shape_1*
T0*
Tshape0**
_class 
loc:@loss/dense_5_loss/mul_1*#
_output_shapes
:џџџџџџџџџ
И
8training/SGD/gradients/loss/dense_5_loss/Mean_grad/ShapeShapeloss/dense_5_loss/Neg*
_output_shapes
:*
T0*
out_type0*)
_class
loc:@loss/dense_5_loss/Mean
Є
7training/SGD/gradients/loss/dense_5_loss/Mean_grad/SizeConst*
value	B :*)
_class
loc:@loss/dense_5_loss/Mean*
dtype0*
_output_shapes
: 
ю
6training/SGD/gradients/loss/dense_5_loss/Mean_grad/addAdd(loss/dense_5_loss/Mean/reduction_indices7training/SGD/gradients/loss/dense_5_loss/Mean_grad/Size*
T0*)
_class
loc:@loss/dense_5_loss/Mean*
_output_shapes
: 

6training/SGD/gradients/loss/dense_5_loss/Mean_grad/modFloorMod6training/SGD/gradients/loss/dense_5_loss/Mean_grad/add7training/SGD/gradients/loss/dense_5_loss/Mean_grad/Size*
T0*)
_class
loc:@loss/dense_5_loss/Mean*
_output_shapes
: 
Џ
:training/SGD/gradients/loss/dense_5_loss/Mean_grad/Shape_1Const*
valueB: *)
_class
loc:@loss/dense_5_loss/Mean*
dtype0*
_output_shapes
:
Ћ
>training/SGD/gradients/loss/dense_5_loss/Mean_grad/range/startConst*
_output_shapes
: *
value	B : *)
_class
loc:@loss/dense_5_loss/Mean*
dtype0
Ћ
>training/SGD/gradients/loss/dense_5_loss/Mean_grad/range/deltaConst*
value	B :*)
_class
loc:@loss/dense_5_loss/Mean*
dtype0*
_output_shapes
: 
Э
8training/SGD/gradients/loss/dense_5_loss/Mean_grad/rangeRange>training/SGD/gradients/loss/dense_5_loss/Mean_grad/range/start7training/SGD/gradients/loss/dense_5_loss/Mean_grad/Size>training/SGD/gradients/loss/dense_5_loss/Mean_grad/range/delta*
_output_shapes
:*

Tidx0*)
_class
loc:@loss/dense_5_loss/Mean
Њ
=training/SGD/gradients/loss/dense_5_loss/Mean_grad/Fill/valueConst*
dtype0*
_output_shapes
: *
value	B :*)
_class
loc:@loss/dense_5_loss/Mean

7training/SGD/gradients/loss/dense_5_loss/Mean_grad/FillFill:training/SGD/gradients/loss/dense_5_loss/Mean_grad/Shape_1=training/SGD/gradients/loss/dense_5_loss/Mean_grad/Fill/value*
T0*)
_class
loc:@loss/dense_5_loss/Mean*
_output_shapes
: 

@training/SGD/gradients/loss/dense_5_loss/Mean_grad/DynamicStitchDynamicStitch8training/SGD/gradients/loss/dense_5_loss/Mean_grad/range6training/SGD/gradients/loss/dense_5_loss/Mean_grad/mod8training/SGD/gradients/loss/dense_5_loss/Mean_grad/Shape7training/SGD/gradients/loss/dense_5_loss/Mean_grad/Fill*
T0*)
_class
loc:@loss/dense_5_loss/Mean*
N*#
_output_shapes
:џџџџџџџџџ
Љ
<training/SGD/gradients/loss/dense_5_loss/Mean_grad/Maximum/yConst*
_output_shapes
: *
value	B :*)
_class
loc:@loss/dense_5_loss/Mean*
dtype0

:training/SGD/gradients/loss/dense_5_loss/Mean_grad/MaximumMaximum@training/SGD/gradients/loss/dense_5_loss/Mean_grad/DynamicStitch<training/SGD/gradients/loss/dense_5_loss/Mean_grad/Maximum/y*
T0*)
_class
loc:@loss/dense_5_loss/Mean*#
_output_shapes
:џџџџџџџџџ

;training/SGD/gradients/loss/dense_5_loss/Mean_grad/floordivFloorDiv8training/SGD/gradients/loss/dense_5_loss/Mean_grad/Shape:training/SGD/gradients/loss/dense_5_loss/Mean_grad/Maximum*)
_class
loc:@loss/dense_5_loss/Mean*#
_output_shapes
:џџџџџџџџџ*
T0
 
:training/SGD/gradients/loss/dense_5_loss/Mean_grad/ReshapeReshape;training/SGD/gradients/loss/dense_5_loss/mul_1_grad/Reshape@training/SGD/gradients/loss/dense_5_loss/Mean_grad/DynamicStitch*
T0*
Tshape0*)
_class
loc:@loss/dense_5_loss/Mean*
_output_shapes
:

7training/SGD/gradients/loss/dense_5_loss/Mean_grad/TileTile:training/SGD/gradients/loss/dense_5_loss/Mean_grad/Reshape;training/SGD/gradients/loss/dense_5_loss/Mean_grad/floordiv*)
_class
loc:@loss/dense_5_loss/Mean*
_output_shapes
:*

Tmultiples0*
T0
К
:training/SGD/gradients/loss/dense_5_loss/Mean_grad/Shape_2Shapeloss/dense_5_loss/Neg*
_output_shapes
:*
T0*
out_type0*)
_class
loc:@loss/dense_5_loss/Mean
Л
:training/SGD/gradients/loss/dense_5_loss/Mean_grad/Shape_3Shapeloss/dense_5_loss/Mean*
T0*
out_type0*)
_class
loc:@loss/dense_5_loss/Mean*
_output_shapes
:
­
8training/SGD/gradients/loss/dense_5_loss/Mean_grad/ConstConst*
_output_shapes
:*
valueB: *)
_class
loc:@loss/dense_5_loss/Mean*
dtype0

7training/SGD/gradients/loss/dense_5_loss/Mean_grad/ProdProd:training/SGD/gradients/loss/dense_5_loss/Mean_grad/Shape_28training/SGD/gradients/loss/dense_5_loss/Mean_grad/Const*
T0*)
_class
loc:@loss/dense_5_loss/Mean*
_output_shapes
: *

Tidx0*
	keep_dims( 
Џ
:training/SGD/gradients/loss/dense_5_loss/Mean_grad/Const_1Const*
dtype0*
_output_shapes
:*
valueB: *)
_class
loc:@loss/dense_5_loss/Mean
Ђ
9training/SGD/gradients/loss/dense_5_loss/Mean_grad/Prod_1Prod:training/SGD/gradients/loss/dense_5_loss/Mean_grad/Shape_3:training/SGD/gradients/loss/dense_5_loss/Mean_grad/Const_1*
T0*)
_class
loc:@loss/dense_5_loss/Mean*
_output_shapes
: *

Tidx0*
	keep_dims( 
Ћ
>training/SGD/gradients/loss/dense_5_loss/Mean_grad/Maximum_1/yConst*
value	B :*)
_class
loc:@loss/dense_5_loss/Mean*
dtype0*
_output_shapes
: 

<training/SGD/gradients/loss/dense_5_loss/Mean_grad/Maximum_1Maximum9training/SGD/gradients/loss/dense_5_loss/Mean_grad/Prod_1>training/SGD/gradients/loss/dense_5_loss/Mean_grad/Maximum_1/y*
T0*)
_class
loc:@loss/dense_5_loss/Mean*
_output_shapes
: 

=training/SGD/gradients/loss/dense_5_loss/Mean_grad/floordiv_1FloorDiv7training/SGD/gradients/loss/dense_5_loss/Mean_grad/Prod<training/SGD/gradients/loss/dense_5_loss/Mean_grad/Maximum_1*)
_class
loc:@loss/dense_5_loss/Mean*
_output_shapes
: *
T0
й
7training/SGD/gradients/loss/dense_5_loss/Mean_grad/CastCast=training/SGD/gradients/loss/dense_5_loss/Mean_grad/floordiv_1*

SrcT0*)
_class
loc:@loss/dense_5_loss/Mean*
_output_shapes
: *

DstT0

:training/SGD/gradients/loss/dense_5_loss/Mean_grad/truedivRealDiv7training/SGD/gradients/loss/dense_5_loss/Mean_grad/Tile7training/SGD/gradients/loss/dense_5_loss/Mean_grad/Cast*
T0*)
_class
loc:@loss/dense_5_loss/Mean*#
_output_shapes
:џџџџџџџџџ
а
5training/SGD/gradients/loss/dense_5_loss/Neg_grad/NegNeg:training/SGD/gradients/loss/dense_5_loss/Mean_grad/truediv*
T0*(
_class
loc:@loss/dense_5_loss/Neg*#
_output_shapes
:џџџџџџџџџ
К
9training/SGD/gradients/loss/dense_5_loss/Sum_1_grad/ShapeShapeloss/dense_5_loss/mul*
T0*
out_type0**
_class 
loc:@loss/dense_5_loss/Sum_1*
_output_shapes
:
І
8training/SGD/gradients/loss/dense_5_loss/Sum_1_grad/SizeConst*
value	B :**
_class 
loc:@loss/dense_5_loss/Sum_1*
dtype0*
_output_shapes
: 
№
7training/SGD/gradients/loss/dense_5_loss/Sum_1_grad/addAdd)loss/dense_5_loss/Sum_1/reduction_indices8training/SGD/gradients/loss/dense_5_loss/Sum_1_grad/Size**
_class 
loc:@loss/dense_5_loss/Sum_1*
_output_shapes
: *
T0

7training/SGD/gradients/loss/dense_5_loss/Sum_1_grad/modFloorMod7training/SGD/gradients/loss/dense_5_loss/Sum_1_grad/add8training/SGD/gradients/loss/dense_5_loss/Sum_1_grad/Size*
T0**
_class 
loc:@loss/dense_5_loss/Sum_1*
_output_shapes
: 
Њ
;training/SGD/gradients/loss/dense_5_loss/Sum_1_grad/Shape_1Const*
valueB **
_class 
loc:@loss/dense_5_loss/Sum_1*
dtype0*
_output_shapes
: 
­
?training/SGD/gradients/loss/dense_5_loss/Sum_1_grad/range/startConst*
value	B : **
_class 
loc:@loss/dense_5_loss/Sum_1*
dtype0*
_output_shapes
: 
­
?training/SGD/gradients/loss/dense_5_loss/Sum_1_grad/range/deltaConst*
dtype0*
_output_shapes
: *
value	B :**
_class 
loc:@loss/dense_5_loss/Sum_1
в
9training/SGD/gradients/loss/dense_5_loss/Sum_1_grad/rangeRange?training/SGD/gradients/loss/dense_5_loss/Sum_1_grad/range/start8training/SGD/gradients/loss/dense_5_loss/Sum_1_grad/Size?training/SGD/gradients/loss/dense_5_loss/Sum_1_grad/range/delta**
_class 
loc:@loss/dense_5_loss/Sum_1*
_output_shapes
:*

Tidx0
Ќ
>training/SGD/gradients/loss/dense_5_loss/Sum_1_grad/Fill/valueConst*
value	B :**
_class 
loc:@loss/dense_5_loss/Sum_1*
dtype0*
_output_shapes
: 

8training/SGD/gradients/loss/dense_5_loss/Sum_1_grad/FillFill;training/SGD/gradients/loss/dense_5_loss/Sum_1_grad/Shape_1>training/SGD/gradients/loss/dense_5_loss/Sum_1_grad/Fill/value*
T0**
_class 
loc:@loss/dense_5_loss/Sum_1*
_output_shapes
: 

Atraining/SGD/gradients/loss/dense_5_loss/Sum_1_grad/DynamicStitchDynamicStitch9training/SGD/gradients/loss/dense_5_loss/Sum_1_grad/range7training/SGD/gradients/loss/dense_5_loss/Sum_1_grad/mod9training/SGD/gradients/loss/dense_5_loss/Sum_1_grad/Shape8training/SGD/gradients/loss/dense_5_loss/Sum_1_grad/Fill*
N*#
_output_shapes
:џџџџџџџџџ*
T0**
_class 
loc:@loss/dense_5_loss/Sum_1
Ћ
=training/SGD/gradients/loss/dense_5_loss/Sum_1_grad/Maximum/yConst*
_output_shapes
: *
value	B :**
_class 
loc:@loss/dense_5_loss/Sum_1*
dtype0
Ђ
;training/SGD/gradients/loss/dense_5_loss/Sum_1_grad/MaximumMaximumAtraining/SGD/gradients/loss/dense_5_loss/Sum_1_grad/DynamicStitch=training/SGD/gradients/loss/dense_5_loss/Sum_1_grad/Maximum/y*
T0**
_class 
loc:@loss/dense_5_loss/Sum_1*#
_output_shapes
:џџџџџџџџџ

<training/SGD/gradients/loss/dense_5_loss/Sum_1_grad/floordivFloorDiv9training/SGD/gradients/loss/dense_5_loss/Sum_1_grad/Shape;training/SGD/gradients/loss/dense_5_loss/Sum_1_grad/Maximum*
_output_shapes
:*
T0**
_class 
loc:@loss/dense_5_loss/Sum_1

;training/SGD/gradients/loss/dense_5_loss/Sum_1_grad/ReshapeReshape5training/SGD/gradients/loss/dense_5_loss/Neg_grad/NegAtraining/SGD/gradients/loss/dense_5_loss/Sum_1_grad/DynamicStitch*
_output_shapes
:*
T0*
Tshape0**
_class 
loc:@loss/dense_5_loss/Sum_1
Ћ
8training/SGD/gradients/loss/dense_5_loss/Sum_1_grad/TileTile;training/SGD/gradients/loss/dense_5_loss/Sum_1_grad/Reshape<training/SGD/gradients/loss/dense_5_loss/Sum_1_grad/floordiv*

Tmultiples0*
T0**
_class 
loc:@loss/dense_5_loss/Sum_1*'
_output_shapes
:џџџџџџџџџ
Џ
7training/SGD/gradients/loss/dense_5_loss/mul_grad/ShapeShapedense_5_target*
T0*
out_type0*(
_class
loc:@loss/dense_5_loss/mul*
_output_shapes
:
И
9training/SGD/gradients/loss/dense_5_loss/mul_grad/Shape_1Shapeloss/dense_5_loss/Log*
T0*
out_type0*(
_class
loc:@loss/dense_5_loss/mul*
_output_shapes
:
Л
Gtraining/SGD/gradients/loss/dense_5_loss/mul_grad/BroadcastGradientArgsBroadcastGradientArgs7training/SGD/gradients/loss/dense_5_loss/mul_grad/Shape9training/SGD/gradients/loss/dense_5_loss/mul_grad/Shape_1*
T0*(
_class
loc:@loss/dense_5_loss/mul*2
_output_shapes 
:џџџџџџџџџ:џџџџџџџџџ
щ
5training/SGD/gradients/loss/dense_5_loss/mul_grad/mulMul8training/SGD/gradients/loss/dense_5_loss/Sum_1_grad/Tileloss/dense_5_loss/Log*
T0*(
_class
loc:@loss/dense_5_loss/mul*'
_output_shapes
:џџџџџџџџџ
І
5training/SGD/gradients/loss/dense_5_loss/mul_grad/SumSum5training/SGD/gradients/loss/dense_5_loss/mul_grad/mulGtraining/SGD/gradients/loss/dense_5_loss/mul_grad/BroadcastGradientArgs*
T0*(
_class
loc:@loss/dense_5_loss/mul*
_output_shapes
:*

Tidx0*
	keep_dims( 
Ї
9training/SGD/gradients/loss/dense_5_loss/mul_grad/ReshapeReshape5training/SGD/gradients/loss/dense_5_loss/mul_grad/Sum7training/SGD/gradients/loss/dense_5_loss/mul_grad/Shape*
T0*
Tshape0*(
_class
loc:@loss/dense_5_loss/mul*0
_output_shapes
:џџџџџџџџџџџџџџџџџџ
ф
7training/SGD/gradients/loss/dense_5_loss/mul_grad/mul_1Muldense_5_target8training/SGD/gradients/loss/dense_5_loss/Sum_1_grad/Tile*
T0*(
_class
loc:@loss/dense_5_loss/mul*'
_output_shapes
:џџџџџџџџџ
Ќ
7training/SGD/gradients/loss/dense_5_loss/mul_grad/Sum_1Sum7training/SGD/gradients/loss/dense_5_loss/mul_grad/mul_1Itraining/SGD/gradients/loss/dense_5_loss/mul_grad/BroadcastGradientArgs:1*

Tidx0*
	keep_dims( *
T0*(
_class
loc:@loss/dense_5_loss/mul*
_output_shapes
:
Є
;training/SGD/gradients/loss/dense_5_loss/mul_grad/Reshape_1Reshape7training/SGD/gradients/loss/dense_5_loss/mul_grad/Sum_19training/SGD/gradients/loss/dense_5_loss/mul_grad/Shape_1*'
_output_shapes
:џџџџџџџџџ*
T0*
Tshape0*(
_class
loc:@loss/dense_5_loss/mul

<training/SGD/gradients/loss/dense_5_loss/Log_grad/Reciprocal
Reciprocalloss/dense_5_loss/clip_by_value<^training/SGD/gradients/loss/dense_5_loss/mul_grad/Reshape_1*(
_class
loc:@loss/dense_5_loss/Log*'
_output_shapes
:џџџџџџџџџ*
T0

5training/SGD/gradients/loss/dense_5_loss/Log_grad/mulMul;training/SGD/gradients/loss/dense_5_loss/mul_grad/Reshape_1<training/SGD/gradients/loss/dense_5_loss/Log_grad/Reciprocal*
T0*(
_class
loc:@loss/dense_5_loss/Log*'
_output_shapes
:џџџџџџџџџ
м
Atraining/SGD/gradients/loss/dense_5_loss/clip_by_value_grad/ShapeShape'loss/dense_5_loss/clip_by_value/Minimum*
T0*
out_type0*2
_class(
&$loc:@loss/dense_5_loss/clip_by_value*
_output_shapes
:
К
Ctraining/SGD/gradients/loss/dense_5_loss/clip_by_value_grad/Shape_1Const*
valueB *2
_class(
&$loc:@loss/dense_5_loss/clip_by_value*
dtype0*
_output_shapes
: 
ь
Ctraining/SGD/gradients/loss/dense_5_loss/clip_by_value_grad/Shape_2Shape5training/SGD/gradients/loss/dense_5_loss/Log_grad/mul*
T0*
out_type0*2
_class(
&$loc:@loss/dense_5_loss/clip_by_value*
_output_shapes
:
Р
Gtraining/SGD/gradients/loss/dense_5_loss/clip_by_value_grad/zeros/ConstConst*
valueB
 *    *2
_class(
&$loc:@loss/dense_5_loss/clip_by_value*
dtype0*
_output_shapes
: 
Н
Atraining/SGD/gradients/loss/dense_5_loss/clip_by_value_grad/zerosFillCtraining/SGD/gradients/loss/dense_5_loss/clip_by_value_grad/Shape_2Gtraining/SGD/gradients/loss/dense_5_loss/clip_by_value_grad/zeros/Const*
T0*2
_class(
&$loc:@loss/dense_5_loss/clip_by_value*'
_output_shapes
:џџџџџџџџџ

Htraining/SGD/gradients/loss/dense_5_loss/clip_by_value_grad/GreaterEqualGreaterEqual'loss/dense_5_loss/clip_by_value/Minimumloss/dense_5_loss/Const*
T0*2
_class(
&$loc:@loss/dense_5_loss/clip_by_value*'
_output_shapes
:џџџџџџџџџ
у
Qtraining/SGD/gradients/loss/dense_5_loss/clip_by_value_grad/BroadcastGradientArgsBroadcastGradientArgsAtraining/SGD/gradients/loss/dense_5_loss/clip_by_value_grad/ShapeCtraining/SGD/gradients/loss/dense_5_loss/clip_by_value_grad/Shape_1*2
_output_shapes 
:џџџџџџџџџ:џџџџџџџџџ*
T0*2
_class(
&$loc:@loss/dense_5_loss/clip_by_value
і
Btraining/SGD/gradients/loss/dense_5_loss/clip_by_value_grad/SelectSelectHtraining/SGD/gradients/loss/dense_5_loss/clip_by_value_grad/GreaterEqual5training/SGD/gradients/loss/dense_5_loss/Log_grad/mulAtraining/SGD/gradients/loss/dense_5_loss/clip_by_value_grad/zeros*
T0*2
_class(
&$loc:@loss/dense_5_loss/clip_by_value*'
_output_shapes
:џџџџџџџџџ
ћ
Ftraining/SGD/gradients/loss/dense_5_loss/clip_by_value_grad/LogicalNot
LogicalNotHtraining/SGD/gradients/loss/dense_5_loss/clip_by_value_grad/GreaterEqual*2
_class(
&$loc:@loss/dense_5_loss/clip_by_value*'
_output_shapes
:џџџџџџџџџ
і
Dtraining/SGD/gradients/loss/dense_5_loss/clip_by_value_grad/Select_1SelectFtraining/SGD/gradients/loss/dense_5_loss/clip_by_value_grad/LogicalNot5training/SGD/gradients/loss/dense_5_loss/Log_grad/mulAtraining/SGD/gradients/loss/dense_5_loss/clip_by_value_grad/zeros*
T0*2
_class(
&$loc:@loss/dense_5_loss/clip_by_value*'
_output_shapes
:џџџџџџџџџ
б
?training/SGD/gradients/loss/dense_5_loss/clip_by_value_grad/SumSumBtraining/SGD/gradients/loss/dense_5_loss/clip_by_value_grad/SelectQtraining/SGD/gradients/loss/dense_5_loss/clip_by_value_grad/BroadcastGradientArgs*

Tidx0*
	keep_dims( *
T0*2
_class(
&$loc:@loss/dense_5_loss/clip_by_value*
_output_shapes
:
Ц
Ctraining/SGD/gradients/loss/dense_5_loss/clip_by_value_grad/ReshapeReshape?training/SGD/gradients/loss/dense_5_loss/clip_by_value_grad/SumAtraining/SGD/gradients/loss/dense_5_loss/clip_by_value_grad/Shape*
T0*
Tshape0*2
_class(
&$loc:@loss/dense_5_loss/clip_by_value*'
_output_shapes
:џџџџџџџџџ
з
Atraining/SGD/gradients/loss/dense_5_loss/clip_by_value_grad/Sum_1SumDtraining/SGD/gradients/loss/dense_5_loss/clip_by_value_grad/Select_1Straining/SGD/gradients/loss/dense_5_loss/clip_by_value_grad/BroadcastGradientArgs:1*

Tidx0*
	keep_dims( *
T0*2
_class(
&$loc:@loss/dense_5_loss/clip_by_value*
_output_shapes
:
Л
Etraining/SGD/gradients/loss/dense_5_loss/clip_by_value_grad/Reshape_1ReshapeAtraining/SGD/gradients/loss/dense_5_loss/clip_by_value_grad/Sum_1Ctraining/SGD/gradients/loss/dense_5_loss/clip_by_value_grad/Shape_1*
T0*
Tshape0*2
_class(
&$loc:@loss/dense_5_loss/clip_by_value*
_output_shapes
: 
к
Itraining/SGD/gradients/loss/dense_5_loss/clip_by_value/Minimum_grad/ShapeShapeloss/dense_5_loss/div*
_output_shapes
:*
T0*
out_type0*:
_class0
.,loc:@loss/dense_5_loss/clip_by_value/Minimum
Ъ
Ktraining/SGD/gradients/loss/dense_5_loss/clip_by_value/Minimum_grad/Shape_1Const*
valueB *:
_class0
.,loc:@loss/dense_5_loss/clip_by_value/Minimum*
dtype0*
_output_shapes
: 

Ktraining/SGD/gradients/loss/dense_5_loss/clip_by_value/Minimum_grad/Shape_2ShapeCtraining/SGD/gradients/loss/dense_5_loss/clip_by_value_grad/Reshape*
T0*
out_type0*:
_class0
.,loc:@loss/dense_5_loss/clip_by_value/Minimum*
_output_shapes
:
а
Otraining/SGD/gradients/loss/dense_5_loss/clip_by_value/Minimum_grad/zeros/ConstConst*
valueB
 *    *:
_class0
.,loc:@loss/dense_5_loss/clip_by_value/Minimum*
dtype0*
_output_shapes
: 
н
Itraining/SGD/gradients/loss/dense_5_loss/clip_by_value/Minimum_grad/zerosFillKtraining/SGD/gradients/loss/dense_5_loss/clip_by_value/Minimum_grad/Shape_2Otraining/SGD/gradients/loss/dense_5_loss/clip_by_value/Minimum_grad/zeros/Const*
T0*:
_class0
.,loc:@loss/dense_5_loss/clip_by_value/Minimum*'
_output_shapes
:џџџџџџџџџ
і
Mtraining/SGD/gradients/loss/dense_5_loss/clip_by_value/Minimum_grad/LessEqual	LessEqualloss/dense_5_loss/divloss/dense_5_loss/sub*'
_output_shapes
:џџџџџџџџџ*
T0*:
_class0
.,loc:@loss/dense_5_loss/clip_by_value/Minimum

Ytraining/SGD/gradients/loss/dense_5_loss/clip_by_value/Minimum_grad/BroadcastGradientArgsBroadcastGradientArgsItraining/SGD/gradients/loss/dense_5_loss/clip_by_value/Minimum_grad/ShapeKtraining/SGD/gradients/loss/dense_5_loss/clip_by_value/Minimum_grad/Shape_1*
T0*:
_class0
.,loc:@loss/dense_5_loss/clip_by_value/Minimum*2
_output_shapes 
:џџџџџџџџџ:џџџџџџџџџ
Ё
Jtraining/SGD/gradients/loss/dense_5_loss/clip_by_value/Minimum_grad/SelectSelectMtraining/SGD/gradients/loss/dense_5_loss/clip_by_value/Minimum_grad/LessEqualCtraining/SGD/gradients/loss/dense_5_loss/clip_by_value_grad/ReshapeItraining/SGD/gradients/loss/dense_5_loss/clip_by_value/Minimum_grad/zeros*
T0*:
_class0
.,loc:@loss/dense_5_loss/clip_by_value/Minimum*'
_output_shapes
:џџџџџџџџџ

Ntraining/SGD/gradients/loss/dense_5_loss/clip_by_value/Minimum_grad/LogicalNot
LogicalNotMtraining/SGD/gradients/loss/dense_5_loss/clip_by_value/Minimum_grad/LessEqual*:
_class0
.,loc:@loss/dense_5_loss/clip_by_value/Minimum*'
_output_shapes
:џџџџџџџџџ
Є
Ltraining/SGD/gradients/loss/dense_5_loss/clip_by_value/Minimum_grad/Select_1SelectNtraining/SGD/gradients/loss/dense_5_loss/clip_by_value/Minimum_grad/LogicalNotCtraining/SGD/gradients/loss/dense_5_loss/clip_by_value_grad/ReshapeItraining/SGD/gradients/loss/dense_5_loss/clip_by_value/Minimum_grad/zeros*'
_output_shapes
:џџџџџџџџџ*
T0*:
_class0
.,loc:@loss/dense_5_loss/clip_by_value/Minimum
ё
Gtraining/SGD/gradients/loss/dense_5_loss/clip_by_value/Minimum_grad/SumSumJtraining/SGD/gradients/loss/dense_5_loss/clip_by_value/Minimum_grad/SelectYtraining/SGD/gradients/loss/dense_5_loss/clip_by_value/Minimum_grad/BroadcastGradientArgs*
_output_shapes
:*

Tidx0*
	keep_dims( *
T0*:
_class0
.,loc:@loss/dense_5_loss/clip_by_value/Minimum
ц
Ktraining/SGD/gradients/loss/dense_5_loss/clip_by_value/Minimum_grad/ReshapeReshapeGtraining/SGD/gradients/loss/dense_5_loss/clip_by_value/Minimum_grad/SumItraining/SGD/gradients/loss/dense_5_loss/clip_by_value/Minimum_grad/Shape*
T0*
Tshape0*:
_class0
.,loc:@loss/dense_5_loss/clip_by_value/Minimum*'
_output_shapes
:џџџџџџџџџ
ї
Itraining/SGD/gradients/loss/dense_5_loss/clip_by_value/Minimum_grad/Sum_1SumLtraining/SGD/gradients/loss/dense_5_loss/clip_by_value/Minimum_grad/Select_1[training/SGD/gradients/loss/dense_5_loss/clip_by_value/Minimum_grad/BroadcastGradientArgs:1*

Tidx0*
	keep_dims( *
T0*:
_class0
.,loc:@loss/dense_5_loss/clip_by_value/Minimum*
_output_shapes
:
л
Mtraining/SGD/gradients/loss/dense_5_loss/clip_by_value/Minimum_grad/Reshape_1ReshapeItraining/SGD/gradients/loss/dense_5_loss/clip_by_value/Minimum_grad/Sum_1Ktraining/SGD/gradients/loss/dense_5_loss/clip_by_value/Minimum_grad/Shape_1*
_output_shapes
: *
T0*
Tshape0*:
_class0
.,loc:@loss/dense_5_loss/clip_by_value/Minimum
А
7training/SGD/gradients/loss/dense_5_loss/div_grad/ShapeShapedense_5/Sigmoid*
T0*
out_type0*(
_class
loc:@loss/dense_5_loss/div*
_output_shapes
:
И
9training/SGD/gradients/loss/dense_5_loss/div_grad/Shape_1Shapeloss/dense_5_loss/Sum*
T0*
out_type0*(
_class
loc:@loss/dense_5_loss/div*
_output_shapes
:
Л
Gtraining/SGD/gradients/loss/dense_5_loss/div_grad/BroadcastGradientArgsBroadcastGradientArgs7training/SGD/gradients/loss/dense_5_loss/div_grad/Shape9training/SGD/gradients/loss/dense_5_loss/div_grad/Shape_1*
T0*(
_class
loc:@loss/dense_5_loss/div*2
_output_shapes 
:џџџџџџџџџ:џџџџџџџџџ

9training/SGD/gradients/loss/dense_5_loss/div_grad/RealDivRealDivKtraining/SGD/gradients/loss/dense_5_loss/clip_by_value/Minimum_grad/Reshapeloss/dense_5_loss/Sum*
T0*(
_class
loc:@loss/dense_5_loss/div*'
_output_shapes
:џџџџџџџџџ
Њ
5training/SGD/gradients/loss/dense_5_loss/div_grad/SumSum9training/SGD/gradients/loss/dense_5_loss/div_grad/RealDivGtraining/SGD/gradients/loss/dense_5_loss/div_grad/BroadcastGradientArgs*
T0*(
_class
loc:@loss/dense_5_loss/div*
_output_shapes
:*

Tidx0*
	keep_dims( 

9training/SGD/gradients/loss/dense_5_loss/div_grad/ReshapeReshape5training/SGD/gradients/loss/dense_5_loss/div_grad/Sum7training/SGD/gradients/loss/dense_5_loss/div_grad/Shape*'
_output_shapes
:џџџџџџџџџ*
T0*
Tshape0*(
_class
loc:@loss/dense_5_loss/div
Љ
5training/SGD/gradients/loss/dense_5_loss/div_grad/NegNegdense_5/Sigmoid*'
_output_shapes
:џџџџџџџџџ*
T0*(
_class
loc:@loss/dense_5_loss/div
№
;training/SGD/gradients/loss/dense_5_loss/div_grad/RealDiv_1RealDiv5training/SGD/gradients/loss/dense_5_loss/div_grad/Negloss/dense_5_loss/Sum*
T0*(
_class
loc:@loss/dense_5_loss/div*'
_output_shapes
:џџџџџџџџџ
і
;training/SGD/gradients/loss/dense_5_loss/div_grad/RealDiv_2RealDiv;training/SGD/gradients/loss/dense_5_loss/div_grad/RealDiv_1loss/dense_5_loss/Sum*'
_output_shapes
:џџџџџџџџџ*
T0*(
_class
loc:@loss/dense_5_loss/div
Ђ
5training/SGD/gradients/loss/dense_5_loss/div_grad/mulMulKtraining/SGD/gradients/loss/dense_5_loss/clip_by_value/Minimum_grad/Reshape;training/SGD/gradients/loss/dense_5_loss/div_grad/RealDiv_2*'
_output_shapes
:џџџџџџџџџ*
T0*(
_class
loc:@loss/dense_5_loss/div
Њ
7training/SGD/gradients/loss/dense_5_loss/div_grad/Sum_1Sum5training/SGD/gradients/loss/dense_5_loss/div_grad/mulItraining/SGD/gradients/loss/dense_5_loss/div_grad/BroadcastGradientArgs:1*
_output_shapes
:*

Tidx0*
	keep_dims( *
T0*(
_class
loc:@loss/dense_5_loss/div
Є
;training/SGD/gradients/loss/dense_5_loss/div_grad/Reshape_1Reshape7training/SGD/gradients/loss/dense_5_loss/div_grad/Sum_19training/SGD/gradients/loss/dense_5_loss/div_grad/Shape_1*'
_output_shapes
:џџџџџџџџџ*
T0*
Tshape0*(
_class
loc:@loss/dense_5_loss/div
А
7training/SGD/gradients/loss/dense_5_loss/Sum_grad/ShapeShapedense_5/Sigmoid*
_output_shapes
:*
T0*
out_type0*(
_class
loc:@loss/dense_5_loss/Sum
Ђ
6training/SGD/gradients/loss/dense_5_loss/Sum_grad/SizeConst*
value	B :*(
_class
loc:@loss/dense_5_loss/Sum*
dtype0*
_output_shapes
: 
ш
5training/SGD/gradients/loss/dense_5_loss/Sum_grad/addAdd'loss/dense_5_loss/Sum/reduction_indices6training/SGD/gradients/loss/dense_5_loss/Sum_grad/Size*
_output_shapes
: *
T0*(
_class
loc:@loss/dense_5_loss/Sum
ћ
5training/SGD/gradients/loss/dense_5_loss/Sum_grad/modFloorMod5training/SGD/gradients/loss/dense_5_loss/Sum_grad/add6training/SGD/gradients/loss/dense_5_loss/Sum_grad/Size*(
_class
loc:@loss/dense_5_loss/Sum*
_output_shapes
: *
T0
І
9training/SGD/gradients/loss/dense_5_loss/Sum_grad/Shape_1Const*
dtype0*
_output_shapes
: *
valueB *(
_class
loc:@loss/dense_5_loss/Sum
Љ
=training/SGD/gradients/loss/dense_5_loss/Sum_grad/range/startConst*
dtype0*
_output_shapes
: *
value	B : *(
_class
loc:@loss/dense_5_loss/Sum
Љ
=training/SGD/gradients/loss/dense_5_loss/Sum_grad/range/deltaConst*
value	B :*(
_class
loc:@loss/dense_5_loss/Sum*
dtype0*
_output_shapes
: 
Ш
7training/SGD/gradients/loss/dense_5_loss/Sum_grad/rangeRange=training/SGD/gradients/loss/dense_5_loss/Sum_grad/range/start6training/SGD/gradients/loss/dense_5_loss/Sum_grad/Size=training/SGD/gradients/loss/dense_5_loss/Sum_grad/range/delta*
_output_shapes
:*

Tidx0*(
_class
loc:@loss/dense_5_loss/Sum
Ј
<training/SGD/gradients/loss/dense_5_loss/Sum_grad/Fill/valueConst*
value	B :*(
_class
loc:@loss/dense_5_loss/Sum*
dtype0*
_output_shapes
: 

6training/SGD/gradients/loss/dense_5_loss/Sum_grad/FillFill9training/SGD/gradients/loss/dense_5_loss/Sum_grad/Shape_1<training/SGD/gradients/loss/dense_5_loss/Sum_grad/Fill/value*
T0*(
_class
loc:@loss/dense_5_loss/Sum*
_output_shapes
: 

?training/SGD/gradients/loss/dense_5_loss/Sum_grad/DynamicStitchDynamicStitch7training/SGD/gradients/loss/dense_5_loss/Sum_grad/range5training/SGD/gradients/loss/dense_5_loss/Sum_grad/mod7training/SGD/gradients/loss/dense_5_loss/Sum_grad/Shape6training/SGD/gradients/loss/dense_5_loss/Sum_grad/Fill*
T0*(
_class
loc:@loss/dense_5_loss/Sum*
N*#
_output_shapes
:џџџџџџџџџ
Ї
;training/SGD/gradients/loss/dense_5_loss/Sum_grad/Maximum/yConst*
value	B :*(
_class
loc:@loss/dense_5_loss/Sum*
dtype0*
_output_shapes
: 

9training/SGD/gradients/loss/dense_5_loss/Sum_grad/MaximumMaximum?training/SGD/gradients/loss/dense_5_loss/Sum_grad/DynamicStitch;training/SGD/gradients/loss/dense_5_loss/Sum_grad/Maximum/y*
T0*(
_class
loc:@loss/dense_5_loss/Sum*#
_output_shapes
:џџџџџџџџџ

:training/SGD/gradients/loss/dense_5_loss/Sum_grad/floordivFloorDiv7training/SGD/gradients/loss/dense_5_loss/Sum_grad/Shape9training/SGD/gradients/loss/dense_5_loss/Sum_grad/Maximum*
T0*(
_class
loc:@loss/dense_5_loss/Sum*
_output_shapes
:

9training/SGD/gradients/loss/dense_5_loss/Sum_grad/ReshapeReshape;training/SGD/gradients/loss/dense_5_loss/div_grad/Reshape_1?training/SGD/gradients/loss/dense_5_loss/Sum_grad/DynamicStitch*
Tshape0*(
_class
loc:@loss/dense_5_loss/Sum*
_output_shapes
:*
T0
Ѓ
6training/SGD/gradients/loss/dense_5_loss/Sum_grad/TileTile9training/SGD/gradients/loss/dense_5_loss/Sum_grad/Reshape:training/SGD/gradients/loss/dense_5_loss/Sum_grad/floordiv*'
_output_shapes
:џџџџџџџџџ*

Tmultiples0*
T0*(
_class
loc:@loss/dense_5_loss/Sum
ћ
training/SGD/gradients/AddNAddN9training/SGD/gradients/loss/dense_5_loss/div_grad/Reshape6training/SGD/gradients/loss/dense_5_loss/Sum_grad/Tile*
T0*(
_class
loc:@loss/dense_5_loss/div*
N*'
_output_shapes
:џџџџџџџџџ
Ъ
7training/SGD/gradients/dense_5/Sigmoid_grad/SigmoidGradSigmoidGraddense_5/Sigmoidtraining/SGD/gradients/AddN*
T0*"
_class
loc:@dense_5/Sigmoid*'
_output_shapes
:џџџџџџџџџ
п
7training/SGD/gradients/dense_5/BiasAdd_grad/BiasAddGradBiasAddGrad7training/SGD/gradients/dense_5/Sigmoid_grad/SigmoidGrad*"
_class
loc:@dense_5/BiasAdd*
data_formatNHWC*
_output_shapes
:*
T0

1training/SGD/gradients/dense_5/MatMul_grad/MatMulMatMul7training/SGD/gradients/dense_5/Sigmoid_grad/SigmoidGraddense_5/kernel/read*
T0*!
_class
loc:@dense_5/MatMul*'
_output_shapes
:џџџџџџџџџ*
transpose_a( *
transpose_b(
і
3training/SGD/gradients/dense_5/MatMul_grad/MatMul_1MatMuldense_4/Relu7training/SGD/gradients/dense_5/Sigmoid_grad/SigmoidGrad*
T0*!
_class
loc:@dense_5/MatMul*
_output_shapes

:*
transpose_a(*
transpose_b( 
б
1training/SGD/gradients/dense_4/Relu_grad/ReluGradReluGrad1training/SGD/gradients/dense_5/MatMul_grad/MatMuldense_4/Relu*
T0*
_class
loc:@dense_4/Relu*'
_output_shapes
:џџџџџџџџџ
й
7training/SGD/gradients/dense_4/BiasAdd_grad/BiasAddGradBiasAddGrad1training/SGD/gradients/dense_4/Relu_grad/ReluGrad*
T0*"
_class
loc:@dense_4/BiasAdd*
data_formatNHWC*
_output_shapes
:
ў
1training/SGD/gradients/dense_4/MatMul_grad/MatMulMatMul1training/SGD/gradients/dense_4/Relu_grad/ReluGraddense_4/kernel/read*'
_output_shapes
:џџџџџџџџџ2*
transpose_a( *
transpose_b(*
T0*!
_class
loc:@dense_4/MatMul
№
3training/SGD/gradients/dense_4/MatMul_grad/MatMul_1MatMuldense_3/Relu1training/SGD/gradients/dense_4/Relu_grad/ReluGrad*
_output_shapes

:2*
transpose_a(*
transpose_b( *
T0*!
_class
loc:@dense_4/MatMul
б
1training/SGD/gradients/dense_3/Relu_grad/ReluGradReluGrad1training/SGD/gradients/dense_4/MatMul_grad/MatMuldense_3/Relu*'
_output_shapes
:џџџџџџџџџ2*
T0*
_class
loc:@dense_3/Relu
й
7training/SGD/gradients/dense_3/BiasAdd_grad/BiasAddGradBiasAddGrad1training/SGD/gradients/dense_3/Relu_grad/ReluGrad*
data_formatNHWC*
_output_shapes
:2*
T0*"
_class
loc:@dense_3/BiasAdd
ў
1training/SGD/gradients/dense_3/MatMul_grad/MatMulMatMul1training/SGD/gradients/dense_3/Relu_grad/ReluGraddense_3/kernel/read*
T0*!
_class
loc:@dense_3/MatMul*'
_output_shapes
:џџџџџџџџџF*
transpose_a( *
transpose_b(
№
3training/SGD/gradients/dense_3/MatMul_grad/MatMul_1MatMuldense_2/Relu1training/SGD/gradients/dense_3/Relu_grad/ReluGrad*
T0*!
_class
loc:@dense_3/MatMul*
_output_shapes

:F2*
transpose_a(*
transpose_b( 
б
1training/SGD/gradients/dense_2/Relu_grad/ReluGradReluGrad1training/SGD/gradients/dense_3/MatMul_grad/MatMuldense_2/Relu*'
_output_shapes
:џџџџџџџџџF*
T0*
_class
loc:@dense_2/Relu
й
7training/SGD/gradients/dense_2/BiasAdd_grad/BiasAddGradBiasAddGrad1training/SGD/gradients/dense_2/Relu_grad/ReluGrad*
T0*"
_class
loc:@dense_2/BiasAdd*
data_formatNHWC*
_output_shapes
:F
ў
1training/SGD/gradients/dense_2/MatMul_grad/MatMulMatMul1training/SGD/gradients/dense_2/Relu_grad/ReluGraddense_2/kernel/read*
T0*!
_class
loc:@dense_2/MatMul*'
_output_shapes
:џџџџџџџџџd*
transpose_a( *
transpose_b(
№
3training/SGD/gradients/dense_2/MatMul_grad/MatMul_1MatMuldense_1/Relu1training/SGD/gradients/dense_2/Relu_grad/ReluGrad*
_output_shapes

:dF*
transpose_a(*
transpose_b( *
T0*!
_class
loc:@dense_2/MatMul
б
1training/SGD/gradients/dense_1/Relu_grad/ReluGradReluGrad1training/SGD/gradients/dense_2/MatMul_grad/MatMuldense_1/Relu*'
_output_shapes
:џџџџџџџџџd*
T0*
_class
loc:@dense_1/Relu
й
7training/SGD/gradients/dense_1/BiasAdd_grad/BiasAddGradBiasAddGrad1training/SGD/gradients/dense_1/Relu_grad/ReluGrad*
data_formatNHWC*
_output_shapes
:d*
T0*"
_class
loc:@dense_1/BiasAdd
ў
1training/SGD/gradients/dense_1/MatMul_grad/MatMulMatMul1training/SGD/gradients/dense_1/Relu_grad/ReluGraddense_1/kernel/read*
T0*!
_class
loc:@dense_1/MatMul*'
_output_shapes
:џџџџџџџџџ7*
transpose_a( *
transpose_b(
ё
3training/SGD/gradients/dense_1/MatMul_grad/MatMul_1MatMuldense_1_input1training/SGD/gradients/dense_1/Relu_grad/ReluGrad*
transpose_b( *
T0*!
_class
loc:@dense_1/MatMul*
_output_shapes

:7d*
transpose_a(
^
training/SGD/AssignAdd/valueConst*
dtype0	*
_output_shapes
: *
value	B	 R
Ј
training/SGD/AssignAdd	AssignAddSGD/iterationstraining/SGD/AssignAdd/value*!
_class
loc:@SGD/iterations*
_output_shapes
: *
use_locking( *
T0	
g
training/SGD/ConstConst*
valueB7d*    *
dtype0*
_output_shapes

:7d

training/SGD/Variable
VariableV2*
shape
:7d*
shared_name *
dtype0*
_output_shapes

:7d*
	container 
Э
training/SGD/Variable/AssignAssigntraining/SGD/Variabletraining/SGD/Const*(
_class
loc:@training/SGD/Variable*
validate_shape(*
_output_shapes

:7d*
use_locking(*
T0

training/SGD/Variable/readIdentitytraining/SGD/Variable*
T0*(
_class
loc:@training/SGD/Variable*
_output_shapes

:7d
a
training/SGD/Const_1Const*
valueBd*    *
dtype0*
_output_shapes
:d

training/SGD/Variable_1
VariableV2*
dtype0*
_output_shapes
:d*
	container *
shape:d*
shared_name 
б
training/SGD/Variable_1/AssignAssigntraining/SGD/Variable_1training/SGD/Const_1*
_output_shapes
:d*
use_locking(*
T0**
_class 
loc:@training/SGD/Variable_1*
validate_shape(

training/SGD/Variable_1/readIdentitytraining/SGD/Variable_1*
T0**
_class 
loc:@training/SGD/Variable_1*
_output_shapes
:d
i
training/SGD/Const_2Const*
valueBdF*    *
dtype0*
_output_shapes

:dF

training/SGD/Variable_2
VariableV2*
shared_name *
dtype0*
_output_shapes

:dF*
	container *
shape
:dF
е
training/SGD/Variable_2/AssignAssigntraining/SGD/Variable_2training/SGD/Const_2*
use_locking(*
T0**
_class 
loc:@training/SGD/Variable_2*
validate_shape(*
_output_shapes

:dF

training/SGD/Variable_2/readIdentitytraining/SGD/Variable_2*
T0**
_class 
loc:@training/SGD/Variable_2*
_output_shapes

:dF
a
training/SGD/Const_3Const*
valueBF*    *
dtype0*
_output_shapes
:F

training/SGD/Variable_3
VariableV2*
shared_name *
dtype0*
_output_shapes
:F*
	container *
shape:F
б
training/SGD/Variable_3/AssignAssigntraining/SGD/Variable_3training/SGD/Const_3*
use_locking(*
T0**
_class 
loc:@training/SGD/Variable_3*
validate_shape(*
_output_shapes
:F

training/SGD/Variable_3/readIdentitytraining/SGD/Variable_3*
T0**
_class 
loc:@training/SGD/Variable_3*
_output_shapes
:F
i
training/SGD/Const_4Const*
valueBF2*    *
dtype0*
_output_shapes

:F2

training/SGD/Variable_4
VariableV2*
dtype0*
_output_shapes

:F2*
	container *
shape
:F2*
shared_name 
е
training/SGD/Variable_4/AssignAssigntraining/SGD/Variable_4training/SGD/Const_4*
validate_shape(*
_output_shapes

:F2*
use_locking(*
T0**
_class 
loc:@training/SGD/Variable_4

training/SGD/Variable_4/readIdentitytraining/SGD/Variable_4**
_class 
loc:@training/SGD/Variable_4*
_output_shapes

:F2*
T0
a
training/SGD/Const_5Const*
valueB2*    *
dtype0*
_output_shapes
:2

training/SGD/Variable_5
VariableV2*
dtype0*
_output_shapes
:2*
	container *
shape:2*
shared_name 
б
training/SGD/Variable_5/AssignAssigntraining/SGD/Variable_5training/SGD/Const_5*
validate_shape(*
_output_shapes
:2*
use_locking(*
T0**
_class 
loc:@training/SGD/Variable_5

training/SGD/Variable_5/readIdentitytraining/SGD/Variable_5*
T0**
_class 
loc:@training/SGD/Variable_5*
_output_shapes
:2
i
training/SGD/Const_6Const*
valueB2*    *
dtype0*
_output_shapes

:2

training/SGD/Variable_6
VariableV2*
dtype0*
_output_shapes

:2*
	container *
shape
:2*
shared_name 
е
training/SGD/Variable_6/AssignAssigntraining/SGD/Variable_6training/SGD/Const_6*
use_locking(*
T0**
_class 
loc:@training/SGD/Variable_6*
validate_shape(*
_output_shapes

:2

training/SGD/Variable_6/readIdentitytraining/SGD/Variable_6*
T0**
_class 
loc:@training/SGD/Variable_6*
_output_shapes

:2
a
training/SGD/Const_7Const*
valueB*    *
dtype0*
_output_shapes
:

training/SGD/Variable_7
VariableV2*
shared_name *
dtype0*
_output_shapes
:*
	container *
shape:
б
training/SGD/Variable_7/AssignAssigntraining/SGD/Variable_7training/SGD/Const_7**
_class 
loc:@training/SGD/Variable_7*
validate_shape(*
_output_shapes
:*
use_locking(*
T0

training/SGD/Variable_7/readIdentitytraining/SGD/Variable_7*
T0**
_class 
loc:@training/SGD/Variable_7*
_output_shapes
:
i
training/SGD/Const_8Const*
valueB*    *
dtype0*
_output_shapes

:

training/SGD/Variable_8
VariableV2*
dtype0*
_output_shapes

:*
	container *
shape
:*
shared_name 
е
training/SGD/Variable_8/AssignAssigntraining/SGD/Variable_8training/SGD/Const_8*
T0**
_class 
loc:@training/SGD/Variable_8*
validate_shape(*
_output_shapes

:*
use_locking(

training/SGD/Variable_8/readIdentitytraining/SGD/Variable_8*
T0**
_class 
loc:@training/SGD/Variable_8*
_output_shapes

:
a
training/SGD/Const_9Const*
valueB*    *
dtype0*
_output_shapes
:

training/SGD/Variable_9
VariableV2*
dtype0*
_output_shapes
:*
	container *
shape:*
shared_name 
б
training/SGD/Variable_9/AssignAssigntraining/SGD/Variable_9training/SGD/Const_9*
_output_shapes
:*
use_locking(*
T0**
_class 
loc:@training/SGD/Variable_9*
validate_shape(

training/SGD/Variable_9/readIdentitytraining/SGD/Variable_9*
T0**
_class 
loc:@training/SGD/Variable_9*
_output_shapes
:
o
training/SGD/mulMulSGD/momentum/readtraining/SGD/Variable/read*
T0*
_output_shapes

:7d

training/SGD/mul_1MulSGD/lr/read3training/SGD/gradients/dense_1/MatMul_grad/MatMul_1*
_output_shapes

:7d*
T0
f
training/SGD/subSubtraining/SGD/multraining/SGD/mul_1*
T0*
_output_shapes

:7d
Т
training/SGD/AssignAssigntraining/SGD/Variabletraining/SGD/sub*
use_locking(*
T0*(
_class
loc:@training/SGD/Variable*
validate_shape(*
_output_shapes

:7d
g
training/SGD/addAdddense_1/kernel/readtraining/SGD/sub*
_output_shapes

:7d*
T0
Ж
training/SGD/Assign_1Assigndense_1/kerneltraining/SGD/add*!
_class
loc:@dense_1/kernel*
validate_shape(*
_output_shapes

:7d*
use_locking(*
T0
o
training/SGD/mul_2MulSGD/momentum/readtraining/SGD/Variable_1/read*
T0*
_output_shapes
:d

training/SGD/mul_3MulSGD/lr/read7training/SGD/gradients/dense_1/BiasAdd_grad/BiasAddGrad*
_output_shapes
:d*
T0
f
training/SGD/sub_1Subtraining/SGD/mul_2training/SGD/mul_3*
_output_shapes
:d*
T0
Ц
training/SGD/Assign_2Assigntraining/SGD/Variable_1training/SGD/sub_1**
_class 
loc:@training/SGD/Variable_1*
validate_shape(*
_output_shapes
:d*
use_locking(*
T0
e
training/SGD/add_1Adddense_1/bias/readtraining/SGD/sub_1*
T0*
_output_shapes
:d
А
training/SGD/Assign_3Assigndense_1/biastraining/SGD/add_1*
use_locking(*
T0*
_class
loc:@dense_1/bias*
validate_shape(*
_output_shapes
:d
s
training/SGD/mul_4MulSGD/momentum/readtraining/SGD/Variable_2/read*
T0*
_output_shapes

:dF

training/SGD/mul_5MulSGD/lr/read3training/SGD/gradients/dense_2/MatMul_grad/MatMul_1*
T0*
_output_shapes

:dF
j
training/SGD/sub_2Subtraining/SGD/mul_4training/SGD/mul_5*
_output_shapes

:dF*
T0
Ъ
training/SGD/Assign_4Assigntraining/SGD/Variable_2training/SGD/sub_2*
T0**
_class 
loc:@training/SGD/Variable_2*
validate_shape(*
_output_shapes

:dF*
use_locking(
k
training/SGD/add_2Adddense_2/kernel/readtraining/SGD/sub_2*
T0*
_output_shapes

:dF
И
training/SGD/Assign_5Assigndense_2/kerneltraining/SGD/add_2*
use_locking(*
T0*!
_class
loc:@dense_2/kernel*
validate_shape(*
_output_shapes

:dF
o
training/SGD/mul_6MulSGD/momentum/readtraining/SGD/Variable_3/read*
T0*
_output_shapes
:F

training/SGD/mul_7MulSGD/lr/read7training/SGD/gradients/dense_2/BiasAdd_grad/BiasAddGrad*
T0*
_output_shapes
:F
f
training/SGD/sub_3Subtraining/SGD/mul_6training/SGD/mul_7*
_output_shapes
:F*
T0
Ц
training/SGD/Assign_6Assigntraining/SGD/Variable_3training/SGD/sub_3*
_output_shapes
:F*
use_locking(*
T0**
_class 
loc:@training/SGD/Variable_3*
validate_shape(
e
training/SGD/add_3Adddense_2/bias/readtraining/SGD/sub_3*
T0*
_output_shapes
:F
А
training/SGD/Assign_7Assigndense_2/biastraining/SGD/add_3*
use_locking(*
T0*
_class
loc:@dense_2/bias*
validate_shape(*
_output_shapes
:F
s
training/SGD/mul_8MulSGD/momentum/readtraining/SGD/Variable_4/read*
T0*
_output_shapes

:F2

training/SGD/mul_9MulSGD/lr/read3training/SGD/gradients/dense_3/MatMul_grad/MatMul_1*
T0*
_output_shapes

:F2
j
training/SGD/sub_4Subtraining/SGD/mul_8training/SGD/mul_9*
T0*
_output_shapes

:F2
Ъ
training/SGD/Assign_8Assigntraining/SGD/Variable_4training/SGD/sub_4*
_output_shapes

:F2*
use_locking(*
T0**
_class 
loc:@training/SGD/Variable_4*
validate_shape(
k
training/SGD/add_4Adddense_3/kernel/readtraining/SGD/sub_4*
_output_shapes

:F2*
T0
И
training/SGD/Assign_9Assigndense_3/kerneltraining/SGD/add_4*!
_class
loc:@dense_3/kernel*
validate_shape(*
_output_shapes

:F2*
use_locking(*
T0
p
training/SGD/mul_10MulSGD/momentum/readtraining/SGD/Variable_5/read*
_output_shapes
:2*
T0

training/SGD/mul_11MulSGD/lr/read7training/SGD/gradients/dense_3/BiasAdd_grad/BiasAddGrad*
_output_shapes
:2*
T0
h
training/SGD/sub_5Subtraining/SGD/mul_10training/SGD/mul_11*
_output_shapes
:2*
T0
Ч
training/SGD/Assign_10Assigntraining/SGD/Variable_5training/SGD/sub_5*
use_locking(*
T0**
_class 
loc:@training/SGD/Variable_5*
validate_shape(*
_output_shapes
:2
e
training/SGD/add_5Adddense_3/bias/readtraining/SGD/sub_5*
T0*
_output_shapes
:2
Б
training/SGD/Assign_11Assigndense_3/biastraining/SGD/add_5*
use_locking(*
T0*
_class
loc:@dense_3/bias*
validate_shape(*
_output_shapes
:2
t
training/SGD/mul_12MulSGD/momentum/readtraining/SGD/Variable_6/read*
_output_shapes

:2*
T0

training/SGD/mul_13MulSGD/lr/read3training/SGD/gradients/dense_4/MatMul_grad/MatMul_1*
_output_shapes

:2*
T0
l
training/SGD/sub_6Subtraining/SGD/mul_12training/SGD/mul_13*
T0*
_output_shapes

:2
Ы
training/SGD/Assign_12Assigntraining/SGD/Variable_6training/SGD/sub_6*
use_locking(*
T0**
_class 
loc:@training/SGD/Variable_6*
validate_shape(*
_output_shapes

:2
k
training/SGD/add_6Adddense_4/kernel/readtraining/SGD/sub_6*
_output_shapes

:2*
T0
Й
training/SGD/Assign_13Assigndense_4/kerneltraining/SGD/add_6*
_output_shapes

:2*
use_locking(*
T0*!
_class
loc:@dense_4/kernel*
validate_shape(
p
training/SGD/mul_14MulSGD/momentum/readtraining/SGD/Variable_7/read*
_output_shapes
:*
T0

training/SGD/mul_15MulSGD/lr/read7training/SGD/gradients/dense_4/BiasAdd_grad/BiasAddGrad*
T0*
_output_shapes
:
h
training/SGD/sub_7Subtraining/SGD/mul_14training/SGD/mul_15*
_output_shapes
:*
T0
Ч
training/SGD/Assign_14Assigntraining/SGD/Variable_7training/SGD/sub_7*
_output_shapes
:*
use_locking(*
T0**
_class 
loc:@training/SGD/Variable_7*
validate_shape(
e
training/SGD/add_7Adddense_4/bias/readtraining/SGD/sub_7*
_output_shapes
:*
T0
Б
training/SGD/Assign_15Assigndense_4/biastraining/SGD/add_7*
_output_shapes
:*
use_locking(*
T0*
_class
loc:@dense_4/bias*
validate_shape(
t
training/SGD/mul_16MulSGD/momentum/readtraining/SGD/Variable_8/read*
T0*
_output_shapes

:

training/SGD/mul_17MulSGD/lr/read3training/SGD/gradients/dense_5/MatMul_grad/MatMul_1*
T0*
_output_shapes

:
l
training/SGD/sub_8Subtraining/SGD/mul_16training/SGD/mul_17*
T0*
_output_shapes

:
Ы
training/SGD/Assign_16Assigntraining/SGD/Variable_8training/SGD/sub_8*
use_locking(*
T0**
_class 
loc:@training/SGD/Variable_8*
validate_shape(*
_output_shapes

:
k
training/SGD/add_8Adddense_5/kernel/readtraining/SGD/sub_8*
T0*
_output_shapes

:
Й
training/SGD/Assign_17Assigndense_5/kerneltraining/SGD/add_8*
T0*!
_class
loc:@dense_5/kernel*
validate_shape(*
_output_shapes

:*
use_locking(
p
training/SGD/mul_18MulSGD/momentum/readtraining/SGD/Variable_9/read*
_output_shapes
:*
T0

training/SGD/mul_19MulSGD/lr/read7training/SGD/gradients/dense_5/BiasAdd_grad/BiasAddGrad*
_output_shapes
:*
T0
h
training/SGD/sub_9Subtraining/SGD/mul_18training/SGD/mul_19*
T0*
_output_shapes
:
Ч
training/SGD/Assign_18Assigntraining/SGD/Variable_9training/SGD/sub_9*
T0**
_class 
loc:@training/SGD/Variable_9*
validate_shape(*
_output_shapes
:*
use_locking(
e
training/SGD/add_9Adddense_5/bias/readtraining/SGD/sub_9*
_output_shapes
:*
T0
Б
training/SGD/Assign_19Assigndense_5/biastraining/SGD/add_9*
use_locking(*
T0*
_class
loc:@dense_5/bias*
validate_shape(*
_output_shapes
:
К
training/group_depsNoOp	^loss/mul^metrics/acc/Mean^training/SGD/AssignAdd^training/SGD/Assign^training/SGD/Assign_1^training/SGD/Assign_2^training/SGD/Assign_3^training/SGD/Assign_4^training/SGD/Assign_5^training/SGD/Assign_6^training/SGD/Assign_7^training/SGD/Assign_8^training/SGD/Assign_9^training/SGD/Assign_10^training/SGD/Assign_11^training/SGD/Assign_12^training/SGD/Assign_13^training/SGD/Assign_14^training/SGD/Assign_15^training/SGD/Assign_16^training/SGD/Assign_17^training/SGD/Assign_18^training/SGD/Assign_19

initNoOp^dense_1/kernel/Assign^dense_1/bias/Assign^dense_2/kernel/Assign^dense_2/bias/Assign^dense_3/kernel/Assign^dense_3/bias/Assign^dense_4/kernel/Assign^dense_4/bias/Assign^dense_5/kernel/Assign^dense_5/bias/Assign^SGD/iterations/Assign^SGD/lr/Assign^SGD/momentum/Assign^SGD/decay/Assign^training/SGD/Variable/Assign^training/SGD/Variable_1/Assign^training/SGD/Variable_2/Assign^training/SGD/Variable_3/Assign^training/SGD/Variable_4/Assign^training/SGD/Variable_5/Assign^training/SGD/Variable_6/Assign^training/SGD/Variable_7/Assign^training/SGD/Variable_8/Assign^training/SGD/Variable_9/Assign
r
dense_1_input_1Placeholder*
shape:џџџџџџџџџ7*
dtype0*'
_output_shapes
:џџџџџџџџџ7
o
dense_1_1/random_uniform/shapeConst*
_output_shapes
:*
valueB"7   d   *
dtype0
a
dense_1_1/random_uniform/minConst*
valueB
 *>xIО*
dtype0*
_output_shapes
: 
a
dense_1_1/random_uniform/maxConst*
valueB
 *>xI>*
dtype0*
_output_shapes
: 
Ќ
&dense_1_1/random_uniform/RandomUniformRandomUniformdense_1_1/random_uniform/shape*
T0*
dtype0*
_output_shapes

:7d*
seed2р*
seedБџх)

dense_1_1/random_uniform/subSubdense_1_1/random_uniform/maxdense_1_1/random_uniform/min*
T0*
_output_shapes
: 

dense_1_1/random_uniform/mulMul&dense_1_1/random_uniform/RandomUniformdense_1_1/random_uniform/sub*
T0*
_output_shapes

:7d

dense_1_1/random_uniformAdddense_1_1/random_uniform/muldense_1_1/random_uniform/min*
T0*
_output_shapes

:7d

dense_1_1/kernel
VariableV2*
_output_shapes

:7d*
	container *
shape
:7d*
shared_name *
dtype0
Ф
dense_1_1/kernel/AssignAssigndense_1_1/kerneldense_1_1/random_uniform*
use_locking(*
T0*#
_class
loc:@dense_1_1/kernel*
validate_shape(*
_output_shapes

:7d

dense_1_1/kernel/readIdentitydense_1_1/kernel*
T0*#
_class
loc:@dense_1_1/kernel*
_output_shapes

:7d
\
dense_1_1/ConstConst*
dtype0*
_output_shapes
:d*
valueBd*    
z
dense_1_1/bias
VariableV2*
dtype0*
_output_shapes
:d*
	container *
shape:d*
shared_name 
Б
dense_1_1/bias/AssignAssigndense_1_1/biasdense_1_1/Const*
use_locking(*
T0*!
_class
loc:@dense_1_1/bias*
validate_shape(*
_output_shapes
:d
w
dense_1_1/bias/readIdentitydense_1_1/bias*
_output_shapes
:d*
T0*!
_class
loc:@dense_1_1/bias

dense_1_1/MatMulMatMuldense_1_input_1dense_1_1/kernel/read*
T0*'
_output_shapes
:џџџџџџџџџd*
transpose_a( *
transpose_b( 

dense_1_1/BiasAddBiasAdddense_1_1/MatMuldense_1_1/bias/read*'
_output_shapes
:џџџџџџџџџd*
T0*
data_formatNHWC
[
dense_1_1/ReluReludense_1_1/BiasAdd*
T0*'
_output_shapes
:џџџџџџџџџd
o
dense_2_1/random_uniform/shapeConst*
valueB"d   F   *
dtype0*
_output_shapes
:
a
dense_2_1/random_uniform/minConst*
valueB
 *H`@О*
dtype0*
_output_shapes
: 
a
dense_2_1/random_uniform/maxConst*
valueB
 *H`@>*
dtype0*
_output_shapes
: 
Ќ
&dense_2_1/random_uniform/RandomUniformRandomUniformdense_2_1/random_uniform/shape*
dtype0*
_output_shapes

:dF*
seed2ЊБљ*
seedБџх)*
T0

dense_2_1/random_uniform/subSubdense_2_1/random_uniform/maxdense_2_1/random_uniform/min*
T0*
_output_shapes
: 

dense_2_1/random_uniform/mulMul&dense_2_1/random_uniform/RandomUniformdense_2_1/random_uniform/sub*
T0*
_output_shapes

:dF

dense_2_1/random_uniformAdddense_2_1/random_uniform/muldense_2_1/random_uniform/min*
T0*
_output_shapes

:dF

dense_2_1/kernel
VariableV2*
_output_shapes

:dF*
	container *
shape
:dF*
shared_name *
dtype0
Ф
dense_2_1/kernel/AssignAssigndense_2_1/kerneldense_2_1/random_uniform*
_output_shapes

:dF*
use_locking(*
T0*#
_class
loc:@dense_2_1/kernel*
validate_shape(

dense_2_1/kernel/readIdentitydense_2_1/kernel*#
_class
loc:@dense_2_1/kernel*
_output_shapes

:dF*
T0
\
dense_2_1/ConstConst*
valueBF*    *
dtype0*
_output_shapes
:F
z
dense_2_1/bias
VariableV2*
shared_name *
dtype0*
_output_shapes
:F*
	container *
shape:F
Б
dense_2_1/bias/AssignAssigndense_2_1/biasdense_2_1/Const*
_output_shapes
:F*
use_locking(*
T0*!
_class
loc:@dense_2_1/bias*
validate_shape(
w
dense_2_1/bias/readIdentitydense_2_1/bias*
T0*!
_class
loc:@dense_2_1/bias*
_output_shapes
:F

dense_2_1/MatMulMatMuldense_1_1/Reludense_2_1/kernel/read*
T0*'
_output_shapes
:џџџџџџџџџF*
transpose_a( *
transpose_b( 

dense_2_1/BiasAddBiasAdddense_2_1/MatMuldense_2_1/bias/read*
T0*
data_formatNHWC*'
_output_shapes
:џџџџџџџџџF
[
dense_2_1/ReluReludense_2_1/BiasAdd*'
_output_shapes
:џџџџџџџџџF*
T0
o
dense_3_1/random_uniform/shapeConst*
valueB"F   2   *
dtype0*
_output_shapes
:
a
dense_3_1/random_uniform/minConst*
valueB
 *.љdО*
dtype0*
_output_shapes
: 
a
dense_3_1/random_uniform/maxConst*
dtype0*
_output_shapes
: *
valueB
 *.љd>
Ќ
&dense_3_1/random_uniform/RandomUniformRandomUniformdense_3_1/random_uniform/shape*
seedБџх)*
T0*
dtype0*
_output_shapes

:F2*
seed2пц

dense_3_1/random_uniform/subSubdense_3_1/random_uniform/maxdense_3_1/random_uniform/min*
T0*
_output_shapes
: 

dense_3_1/random_uniform/mulMul&dense_3_1/random_uniform/RandomUniformdense_3_1/random_uniform/sub*
T0*
_output_shapes

:F2

dense_3_1/random_uniformAdddense_3_1/random_uniform/muldense_3_1/random_uniform/min*
_output_shapes

:F2*
T0

dense_3_1/kernel
VariableV2*
_output_shapes

:F2*
	container *
shape
:F2*
shared_name *
dtype0
Ф
dense_3_1/kernel/AssignAssigndense_3_1/kerneldense_3_1/random_uniform*
validate_shape(*
_output_shapes

:F2*
use_locking(*
T0*#
_class
loc:@dense_3_1/kernel

dense_3_1/kernel/readIdentitydense_3_1/kernel*
_output_shapes

:F2*
T0*#
_class
loc:@dense_3_1/kernel
\
dense_3_1/ConstConst*
valueB2*    *
dtype0*
_output_shapes
:2
z
dense_3_1/bias
VariableV2*
_output_shapes
:2*
	container *
shape:2*
shared_name *
dtype0
Б
dense_3_1/bias/AssignAssigndense_3_1/biasdense_3_1/Const*!
_class
loc:@dense_3_1/bias*
validate_shape(*
_output_shapes
:2*
use_locking(*
T0
w
dense_3_1/bias/readIdentitydense_3_1/bias*
T0*!
_class
loc:@dense_3_1/bias*
_output_shapes
:2

dense_3_1/MatMulMatMuldense_2_1/Reludense_3_1/kernel/read*'
_output_shapes
:џџџџџџџџџ2*
transpose_a( *
transpose_b( *
T0

dense_3_1/BiasAddBiasAdddense_3_1/MatMuldense_3_1/bias/read*
T0*
data_formatNHWC*'
_output_shapes
:џџџџџџџџџ2
[
dense_3_1/ReluReludense_3_1/BiasAdd*'
_output_shapes
:џџџџџџџџџ2*
T0
o
dense_4_1/random_uniform/shapeConst*
valueB"2      *
dtype0*
_output_shapes
:
a
dense_4_1/random_uniform/minConst*
valueB
 *єхО*
dtype0*
_output_shapes
: 
a
dense_4_1/random_uniform/maxConst*
valueB
 *єх>*
dtype0*
_output_shapes
: 
Ќ
&dense_4_1/random_uniform/RandomUniformRandomUniformdense_4_1/random_uniform/shape*
T0*
dtype0*
_output_shapes

:2*
seed2ЊђЏ*
seedБџх)

dense_4_1/random_uniform/subSubdense_4_1/random_uniform/maxdense_4_1/random_uniform/min*
_output_shapes
: *
T0

dense_4_1/random_uniform/mulMul&dense_4_1/random_uniform/RandomUniformdense_4_1/random_uniform/sub*
T0*
_output_shapes

:2

dense_4_1/random_uniformAdddense_4_1/random_uniform/muldense_4_1/random_uniform/min*
_output_shapes

:2*
T0

dense_4_1/kernel
VariableV2*
dtype0*
_output_shapes

:2*
	container *
shape
:2*
shared_name 
Ф
dense_4_1/kernel/AssignAssigndense_4_1/kerneldense_4_1/random_uniform*
use_locking(*
T0*#
_class
loc:@dense_4_1/kernel*
validate_shape(*
_output_shapes

:2

dense_4_1/kernel/readIdentitydense_4_1/kernel*
T0*#
_class
loc:@dense_4_1/kernel*
_output_shapes

:2
\
dense_4_1/ConstConst*
valueB*    *
dtype0*
_output_shapes
:
z
dense_4_1/bias
VariableV2*
dtype0*
_output_shapes
:*
	container *
shape:*
shared_name 
Б
dense_4_1/bias/AssignAssigndense_4_1/biasdense_4_1/Const*
use_locking(*
T0*!
_class
loc:@dense_4_1/bias*
validate_shape(*
_output_shapes
:
w
dense_4_1/bias/readIdentitydense_4_1/bias*
T0*!
_class
loc:@dense_4_1/bias*
_output_shapes
:

dense_4_1/MatMulMatMuldense_3_1/Reludense_4_1/kernel/read*
transpose_b( *
T0*'
_output_shapes
:џџџџџџџџџ*
transpose_a( 

dense_4_1/BiasAddBiasAdddense_4_1/MatMuldense_4_1/bias/read*'
_output_shapes
:џџџџџџџџџ*
T0*
data_formatNHWC
[
dense_4_1/ReluReludense_4_1/BiasAdd*
T0*'
_output_shapes
:џџџџџџџџџ
o
dense_5_1/random_uniform/shapeConst*
valueB"      *
dtype0*
_output_shapes
:
a
dense_5_1/random_uniform/minConst*
valueB
 *БП*
dtype0*
_output_shapes
: 
a
dense_5_1/random_uniform/maxConst*
valueB
 *Б?*
dtype0*
_output_shapes
: 
Ќ
&dense_5_1/random_uniform/RandomUniformRandomUniformdense_5_1/random_uniform/shape*
seedБџх)*
T0*
dtype0*
_output_shapes

:*
seed2є

dense_5_1/random_uniform/subSubdense_5_1/random_uniform/maxdense_5_1/random_uniform/min*
T0*
_output_shapes
: 

dense_5_1/random_uniform/mulMul&dense_5_1/random_uniform/RandomUniformdense_5_1/random_uniform/sub*
T0*
_output_shapes

:

dense_5_1/random_uniformAdddense_5_1/random_uniform/muldense_5_1/random_uniform/min*
T0*
_output_shapes

:

dense_5_1/kernel
VariableV2*
_output_shapes

:*
	container *
shape
:*
shared_name *
dtype0
Ф
dense_5_1/kernel/AssignAssigndense_5_1/kerneldense_5_1/random_uniform*
T0*#
_class
loc:@dense_5_1/kernel*
validate_shape(*
_output_shapes

:*
use_locking(

dense_5_1/kernel/readIdentitydense_5_1/kernel*
T0*#
_class
loc:@dense_5_1/kernel*
_output_shapes

:
\
dense_5_1/ConstConst*
valueB*    *
dtype0*
_output_shapes
:
z
dense_5_1/bias
VariableV2*
_output_shapes
:*
	container *
shape:*
shared_name *
dtype0
Б
dense_5_1/bias/AssignAssigndense_5_1/biasdense_5_1/Const*
validate_shape(*
_output_shapes
:*
use_locking(*
T0*!
_class
loc:@dense_5_1/bias
w
dense_5_1/bias/readIdentitydense_5_1/bias*
T0*!
_class
loc:@dense_5_1/bias*
_output_shapes
:

dense_5_1/MatMulMatMuldense_4_1/Reludense_5_1/kernel/read*
T0*'
_output_shapes
:џџџџџџџџџ*
transpose_a( *
transpose_b( 

dense_5_1/BiasAddBiasAdddense_5_1/MatMuldense_5_1/bias/read*
T0*
data_formatNHWC*'
_output_shapes
:џџџџџџџџџ
a
dense_5_1/SigmoidSigmoiddense_5_1/BiasAdd*
T0*'
_output_shapes
:џџџџџџџџџ
\
PlaceholderPlaceholder*
shape
:7d*
dtype0*
_output_shapes

:7d
І
AssignAssigndense_1_1/kernelPlaceholder*
use_locking( *
T0*#
_class
loc:@dense_1_1/kernel*
validate_shape(*
_output_shapes

:7d
V
Placeholder_1Placeholder*
shape:d*
dtype0*
_output_shapes
:d
Ђ
Assign_1Assigndense_1_1/biasPlaceholder_1*
use_locking( *
T0*!
_class
loc:@dense_1_1/bias*
validate_shape(*
_output_shapes
:d
^
Placeholder_2Placeholder*
_output_shapes

:dF*
shape
:dF*
dtype0
Њ
Assign_2Assigndense_2_1/kernelPlaceholder_2*
validate_shape(*
_output_shapes

:dF*
use_locking( *
T0*#
_class
loc:@dense_2_1/kernel
V
Placeholder_3Placeholder*
dtype0*
_output_shapes
:F*
shape:F
Ђ
Assign_3Assigndense_2_1/biasPlaceholder_3*
_output_shapes
:F*
use_locking( *
T0*!
_class
loc:@dense_2_1/bias*
validate_shape(
^
Placeholder_4Placeholder*
shape
:F2*
dtype0*
_output_shapes

:F2
Њ
Assign_4Assigndense_3_1/kernelPlaceholder_4*
use_locking( *
T0*#
_class
loc:@dense_3_1/kernel*
validate_shape(*
_output_shapes

:F2
V
Placeholder_5Placeholder*
dtype0*
_output_shapes
:2*
shape:2
Ђ
Assign_5Assigndense_3_1/biasPlaceholder_5*
use_locking( *
T0*!
_class
loc:@dense_3_1/bias*
validate_shape(*
_output_shapes
:2
^
Placeholder_6Placeholder*
dtype0*
_output_shapes

:2*
shape
:2
Њ
Assign_6Assigndense_4_1/kernelPlaceholder_6*
use_locking( *
T0*#
_class
loc:@dense_4_1/kernel*
validate_shape(*
_output_shapes

:2
V
Placeholder_7Placeholder*
_output_shapes
:*
shape:*
dtype0
Ђ
Assign_7Assigndense_4_1/biasPlaceholder_7*
_output_shapes
:*
use_locking( *
T0*!
_class
loc:@dense_4_1/bias*
validate_shape(
^
Placeholder_8Placeholder*
_output_shapes

:*
shape
:*
dtype0
Њ
Assign_8Assigndense_5_1/kernelPlaceholder_8*
use_locking( *
T0*#
_class
loc:@dense_5_1/kernel*
validate_shape(*
_output_shapes

:
V
Placeholder_9Placeholder*
dtype0*
_output_shapes
:*
shape:
Ђ
Assign_9Assigndense_5_1/biasPlaceholder_9*
use_locking( *
T0*!
_class
loc:@dense_5_1/bias*
validate_shape(*
_output_shapes
:

init_1NoOp^dense_1_1/kernel/Assign^dense_1_1/bias/Assign^dense_2_1/kernel/Assign^dense_2_1/bias/Assign^dense_3_1/kernel/Assign^dense_3_1/bias/Assign^dense_4_1/kernel/Assign^dense_4_1/bias/Assign^dense_5_1/kernel/Assign^dense_5_1/bias/Assign
`
SGD_1/iterations/initial_valueConst*
value	B	 R *
dtype0	*
_output_shapes
: 
t
SGD_1/iterations
VariableV2*
dtype0	*
_output_shapes
: *
	container *
shape: *
shared_name 
Т
SGD_1/iterations/AssignAssignSGD_1/iterationsSGD_1/iterations/initial_value*
use_locking(*
T0	*#
_class
loc:@SGD_1/iterations*
validate_shape(*
_output_shapes
: 
y
SGD_1/iterations/readIdentitySGD_1/iterations*
T0	*#
_class
loc:@SGD_1/iterations*
_output_shapes
: 
[
SGD_1/lr/initial_valueConst*
valueB
 *ЭЬЬ=*
dtype0*
_output_shapes
: 
l
SGD_1/lr
VariableV2*
dtype0*
_output_shapes
: *
	container *
shape: *
shared_name 
Ђ
SGD_1/lr/AssignAssignSGD_1/lrSGD_1/lr/initial_value*
use_locking(*
T0*
_class
loc:@SGD_1/lr*
validate_shape(*
_output_shapes
: 
a
SGD_1/lr/readIdentitySGD_1/lr*
T0*
_class
loc:@SGD_1/lr*
_output_shapes
: 
a
SGD_1/momentum/initial_valueConst*
valueB
 *    *
dtype0*
_output_shapes
: 
r
SGD_1/momentum
VariableV2*
dtype0*
_output_shapes
: *
	container *
shape: *
shared_name 
К
SGD_1/momentum/AssignAssignSGD_1/momentumSGD_1/momentum/initial_value*!
_class
loc:@SGD_1/momentum*
validate_shape(*
_output_shapes
: *
use_locking(*
T0
s
SGD_1/momentum/readIdentitySGD_1/momentum*
T0*!
_class
loc:@SGD_1/momentum*
_output_shapes
: 
^
SGD_1/decay/initial_valueConst*
valueB
 *    *
dtype0*
_output_shapes
: 
o
SGD_1/decay
VariableV2*
dtype0*
_output_shapes
: *
	container *
shape: *
shared_name 
Ў
SGD_1/decay/AssignAssignSGD_1/decaySGD_1/decay/initial_value*
_class
loc:@SGD_1/decay*
validate_shape(*
_output_shapes
: *
use_locking(*
T0
j
SGD_1/decay/readIdentitySGD_1/decay*
T0*
_class
loc:@SGD_1/decay*
_output_shapes
: 

dense_5_target_1Placeholder*
dtype0*0
_output_shapes
:џџџџџџџџџџџџџџџџџџ*%
shape:џџџџџџџџџџџџџџџџџџ
s
dense_5_sample_weights_1Placeholder*
dtype0*#
_output_shapes
:џџџџџџџџџ*
shape:џџџџџџџџџ
k
)loss_1/dense_5_loss/Sum/reduction_indicesConst*
value	B :*
dtype0*
_output_shapes
: 
Ћ
loss_1/dense_5_loss/SumSumdense_5_1/Sigmoid)loss_1/dense_5_loss/Sum/reduction_indices*'
_output_shapes
:џџџџџџџџџ*
	keep_dims(*

Tidx0*
T0

loss_1/dense_5_loss/divRealDivdense_5_1/Sigmoidloss_1/dense_5_loss/Sum*'
_output_shapes
:џџџџџџџџџ*
T0
^
loss_1/dense_5_loss/ConstConst*
dtype0*
_output_shapes
: *
valueB
 *Пж3
^
loss_1/dense_5_loss/sub/xConst*
valueB
 *  ?*
dtype0*
_output_shapes
: 
u
loss_1/dense_5_loss/subSubloss_1/dense_5_loss/sub/xloss_1/dense_5_loss/Const*
T0*
_output_shapes
: 

)loss_1/dense_5_loss/clip_by_value/MinimumMinimumloss_1/dense_5_loss/divloss_1/dense_5_loss/sub*
T0*'
_output_shapes
:џџџџџџџџџ
Є
!loss_1/dense_5_loss/clip_by_valueMaximum)loss_1/dense_5_loss/clip_by_value/Minimumloss_1/dense_5_loss/Const*'
_output_shapes
:џџџџџџџџџ*
T0
s
loss_1/dense_5_loss/LogLog!loss_1/dense_5_loss/clip_by_value*
T0*'
_output_shapes
:џџџџџџџџџ
{
loss_1/dense_5_loss/mulMuldense_5_target_1loss_1/dense_5_loss/Log*
T0*'
_output_shapes
:џџџџџџџџџ
m
+loss_1/dense_5_loss/Sum_1/reduction_indicesConst*
dtype0*
_output_shapes
: *
value	B :
Б
loss_1/dense_5_loss/Sum_1Sumloss_1/dense_5_loss/mul+loss_1/dense_5_loss/Sum_1/reduction_indices*
T0*#
_output_shapes
:џџџџџџџџџ*
	keep_dims( *

Tidx0
g
loss_1/dense_5_loss/NegNegloss_1/dense_5_loss/Sum_1*
T0*#
_output_shapes
:џџџџџџџџџ
m
*loss_1/dense_5_loss/Mean/reduction_indicesConst*
valueB *
dtype0*
_output_shapes
: 
А
loss_1/dense_5_loss/MeanMeanloss_1/dense_5_loss/Neg*loss_1/dense_5_loss/Mean/reduction_indices*#
_output_shapes
:џџџџџџџџџ*
	keep_dims( *

Tidx0*
T0

loss_1/dense_5_loss/mul_1Mulloss_1/dense_5_loss/Meandense_5_sample_weights_1*
T0*#
_output_shapes
:џџџџџџџџџ
c
loss_1/dense_5_loss/NotEqual/yConst*
_output_shapes
: *
valueB
 *    *
dtype0

loss_1/dense_5_loss/NotEqualNotEqualdense_5_sample_weights_1loss_1/dense_5_loss/NotEqual/y*#
_output_shapes
:џџџџџџџџџ*
T0
{
loss_1/dense_5_loss/CastCastloss_1/dense_5_loss/NotEqual*#
_output_shapes
:џџџџџџџџџ*

DstT0*

SrcT0

e
loss_1/dense_5_loss/Const_1Const*
valueB: *
dtype0*
_output_shapes
:

loss_1/dense_5_loss/Mean_1Meanloss_1/dense_5_loss/Castloss_1/dense_5_loss/Const_1*
T0*
_output_shapes
: *
	keep_dims( *

Tidx0

loss_1/dense_5_loss/div_1RealDivloss_1/dense_5_loss/mul_1loss_1/dense_5_loss/Mean_1*#
_output_shapes
:џџџџџџџџџ*
T0
e
loss_1/dense_5_loss/Const_2Const*
valueB: *
dtype0*
_output_shapes
:

loss_1/dense_5_loss/Mean_2Meanloss_1/dense_5_loss/div_1loss_1/dense_5_loss/Const_2*
	keep_dims( *

Tidx0*
T0*
_output_shapes
: 
Q
loss_1/mul/xConst*
valueB
 *  ?*
dtype0*
_output_shapes
: 
\

loss_1/mulMulloss_1/mul/xloss_1/dense_5_loss/Mean_2*
T0*
_output_shapes
: 
i
metrics_1/acc/ArgMax/dimensionConst*
valueB :
џџџџџџџџџ*
dtype0*
_output_shapes
: 

metrics_1/acc/ArgMaxArgMaxdense_5_target_1metrics_1/acc/ArgMax/dimension*
T0*
output_type0	*#
_output_shapes
:џџџџџџџџџ*

Tidx0
k
 metrics_1/acc/ArgMax_1/dimensionConst*
valueB :
џџџџџџџџџ*
dtype0*
_output_shapes
: 
Ђ
metrics_1/acc/ArgMax_1ArgMaxdense_5_1/Sigmoid metrics_1/acc/ArgMax_1/dimension*
T0*
output_type0	*#
_output_shapes
:џџџџџџџџџ*

Tidx0
x
metrics_1/acc/EqualEqualmetrics_1/acc/ArgMaxmetrics_1/acc/ArgMax_1*
T0	*#
_output_shapes
:џџџџџџџџџ
l
metrics_1/acc/CastCastmetrics_1/acc/Equal*

SrcT0
*#
_output_shapes
:џџџџџџџџџ*

DstT0
]
metrics_1/acc/ConstConst*
dtype0*
_output_shapes
:*
valueB: 

metrics_1/acc/MeanMeanmetrics_1/acc/Castmetrics_1/acc/Const*
_output_shapes
: *
	keep_dims( *

Tidx0*
T0

training_1/SGD/gradients/ShapeConst*
valueB *
_class
loc:@loss_1/mul*
dtype0*
_output_shapes
: 

training_1/SGD/gradients/ConstConst*
_output_shapes
: *
valueB
 *  ?*
_class
loc:@loss_1/mul*
dtype0
Ѕ
training_1/SGD/gradients/FillFilltraining_1/SGD/gradients/Shapetraining_1/SGD/gradients/Const*
_output_shapes
: *
T0*
_class
loc:@loss_1/mul

.training_1/SGD/gradients/loss_1/mul_grad/ShapeConst*
valueB *
_class
loc:@loss_1/mul*
dtype0*
_output_shapes
: 

0training_1/SGD/gradients/loss_1/mul_grad/Shape_1Const*
valueB *
_class
loc:@loss_1/mul*
dtype0*
_output_shapes
: 

>training_1/SGD/gradients/loss_1/mul_grad/BroadcastGradientArgsBroadcastGradientArgs.training_1/SGD/gradients/loss_1/mul_grad/Shape0training_1/SGD/gradients/loss_1/mul_grad/Shape_1*
T0*
_class
loc:@loss_1/mul*2
_output_shapes 
:џџџџџџџџџ:џџџџџџџџџ
Ў
,training_1/SGD/gradients/loss_1/mul_grad/mulMultraining_1/SGD/gradients/Fillloss_1/dense_5_loss/Mean_2*
T0*
_class
loc:@loss_1/mul*
_output_shapes
: 

,training_1/SGD/gradients/loss_1/mul_grad/SumSum,training_1/SGD/gradients/loss_1/mul_grad/mul>training_1/SGD/gradients/loss_1/mul_grad/BroadcastGradientArgs*

Tidx0*
	keep_dims( *
T0*
_class
loc:@loss_1/mul*
_output_shapes
:
ч
0training_1/SGD/gradients/loss_1/mul_grad/ReshapeReshape,training_1/SGD/gradients/loss_1/mul_grad/Sum.training_1/SGD/gradients/loss_1/mul_grad/Shape*
Tshape0*
_class
loc:@loss_1/mul*
_output_shapes
: *
T0
Ђ
.training_1/SGD/gradients/loss_1/mul_grad/mul_1Mulloss_1/mul/xtraining_1/SGD/gradients/Fill*
T0*
_class
loc:@loss_1/mul*
_output_shapes
: 

.training_1/SGD/gradients/loss_1/mul_grad/Sum_1Sum.training_1/SGD/gradients/loss_1/mul_grad/mul_1@training_1/SGD/gradients/loss_1/mul_grad/BroadcastGradientArgs:1*
T0*
_class
loc:@loss_1/mul*
_output_shapes
:*

Tidx0*
	keep_dims( 
э
2training_1/SGD/gradients/loss_1/mul_grad/Reshape_1Reshape.training_1/SGD/gradients/loss_1/mul_grad/Sum_10training_1/SGD/gradients/loss_1/mul_grad/Shape_1*
T0*
Tshape0*
_class
loc:@loss_1/mul*
_output_shapes
: 
П
Ftraining_1/SGD/gradients/loss_1/dense_5_loss/Mean_2_grad/Reshape/shapeConst*
valueB:*-
_class#
!loc:@loss_1/dense_5_loss/Mean_2*
dtype0*
_output_shapes
:
Љ
@training_1/SGD/gradients/loss_1/dense_5_loss/Mean_2_grad/ReshapeReshape2training_1/SGD/gradients/loss_1/mul_grad/Reshape_1Ftraining_1/SGD/gradients/loss_1/dense_5_loss/Mean_2_grad/Reshape/shape*
T0*
Tshape0*-
_class#
!loc:@loss_1/dense_5_loss/Mean_2*
_output_shapes
:
Ц
>training_1/SGD/gradients/loss_1/dense_5_loss/Mean_2_grad/ShapeShapeloss_1/dense_5_loss/div_1*
T0*
out_type0*-
_class#
!loc:@loss_1/dense_5_loss/Mean_2*
_output_shapes
:
Ж
=training_1/SGD/gradients/loss_1/dense_5_loss/Mean_2_grad/TileTile@training_1/SGD/gradients/loss_1/dense_5_loss/Mean_2_grad/Reshape>training_1/SGD/gradients/loss_1/dense_5_loss/Mean_2_grad/Shape*

Tmultiples0*
T0*-
_class#
!loc:@loss_1/dense_5_loss/Mean_2*#
_output_shapes
:џџџџџџџџџ
Ш
@training_1/SGD/gradients/loss_1/dense_5_loss/Mean_2_grad/Shape_1Shapeloss_1/dense_5_loss/div_1*
_output_shapes
:*
T0*
out_type0*-
_class#
!loc:@loss_1/dense_5_loss/Mean_2
В
@training_1/SGD/gradients/loss_1/dense_5_loss/Mean_2_grad/Shape_2Const*
valueB *-
_class#
!loc:@loss_1/dense_5_loss/Mean_2*
dtype0*
_output_shapes
: 
З
>training_1/SGD/gradients/loss_1/dense_5_loss/Mean_2_grad/ConstConst*
valueB: *-
_class#
!loc:@loss_1/dense_5_loss/Mean_2*
dtype0*
_output_shapes
:
Д
=training_1/SGD/gradients/loss_1/dense_5_loss/Mean_2_grad/ProdProd@training_1/SGD/gradients/loss_1/dense_5_loss/Mean_2_grad/Shape_1>training_1/SGD/gradients/loss_1/dense_5_loss/Mean_2_grad/Const*

Tidx0*
	keep_dims( *
T0*-
_class#
!loc:@loss_1/dense_5_loss/Mean_2*
_output_shapes
: 
Й
@training_1/SGD/gradients/loss_1/dense_5_loss/Mean_2_grad/Const_1Const*
valueB: *-
_class#
!loc:@loss_1/dense_5_loss/Mean_2*
dtype0*
_output_shapes
:
И
?training_1/SGD/gradients/loss_1/dense_5_loss/Mean_2_grad/Prod_1Prod@training_1/SGD/gradients/loss_1/dense_5_loss/Mean_2_grad/Shape_2@training_1/SGD/gradients/loss_1/dense_5_loss/Mean_2_grad/Const_1*
T0*-
_class#
!loc:@loss_1/dense_5_loss/Mean_2*
_output_shapes
: *

Tidx0*
	keep_dims( 
Г
Btraining_1/SGD/gradients/loss_1/dense_5_loss/Mean_2_grad/Maximum/yConst*
value	B :*-
_class#
!loc:@loss_1/dense_5_loss/Mean_2*
dtype0*
_output_shapes
: 
 
@training_1/SGD/gradients/loss_1/dense_5_loss/Mean_2_grad/MaximumMaximum?training_1/SGD/gradients/loss_1/dense_5_loss/Mean_2_grad/Prod_1Btraining_1/SGD/gradients/loss_1/dense_5_loss/Mean_2_grad/Maximum/y*
T0*-
_class#
!loc:@loss_1/dense_5_loss/Mean_2*
_output_shapes
: 

Atraining_1/SGD/gradients/loss_1/dense_5_loss/Mean_2_grad/floordivFloorDiv=training_1/SGD/gradients/loss_1/dense_5_loss/Mean_2_grad/Prod@training_1/SGD/gradients/loss_1/dense_5_loss/Mean_2_grad/Maximum*
T0*-
_class#
!loc:@loss_1/dense_5_loss/Mean_2*
_output_shapes
: 
ч
=training_1/SGD/gradients/loss_1/dense_5_loss/Mean_2_grad/CastCastAtraining_1/SGD/gradients/loss_1/dense_5_loss/Mean_2_grad/floordiv*

SrcT0*-
_class#
!loc:@loss_1/dense_5_loss/Mean_2*
_output_shapes
: *

DstT0
І
@training_1/SGD/gradients/loss_1/dense_5_loss/Mean_2_grad/truedivRealDiv=training_1/SGD/gradients/loss_1/dense_5_loss/Mean_2_grad/Tile=training_1/SGD/gradients/loss_1/dense_5_loss/Mean_2_grad/Cast*
T0*-
_class#
!loc:@loss_1/dense_5_loss/Mean_2*#
_output_shapes
:џџџџџџџџџ
Ф
=training_1/SGD/gradients/loss_1/dense_5_loss/div_1_grad/ShapeShapeloss_1/dense_5_loss/mul_1*
T0*
out_type0*,
_class"
 loc:@loss_1/dense_5_loss/div_1*
_output_shapes
:
А
?training_1/SGD/gradients/loss_1/dense_5_loss/div_1_grad/Shape_1Const*
valueB *,
_class"
 loc:@loss_1/dense_5_loss/div_1*
dtype0*
_output_shapes
: 
б
Mtraining_1/SGD/gradients/loss_1/dense_5_loss/div_1_grad/BroadcastGradientArgsBroadcastGradientArgs=training_1/SGD/gradients/loss_1/dense_5_loss/div_1_grad/Shape?training_1/SGD/gradients/loss_1/dense_5_loss/div_1_grad/Shape_1*,
_class"
 loc:@loss_1/dense_5_loss/div_1*2
_output_shapes 
:џџџџџџџџџ:џџџџџџџџџ*
T0

?training_1/SGD/gradients/loss_1/dense_5_loss/div_1_grad/RealDivRealDiv@training_1/SGD/gradients/loss_1/dense_5_loss/Mean_2_grad/truedivloss_1/dense_5_loss/Mean_1*
T0*,
_class"
 loc:@loss_1/dense_5_loss/div_1*#
_output_shapes
:џџџџџџџџџ
Р
;training_1/SGD/gradients/loss_1/dense_5_loss/div_1_grad/SumSum?training_1/SGD/gradients/loss_1/dense_5_loss/div_1_grad/RealDivMtraining_1/SGD/gradients/loss_1/dense_5_loss/div_1_grad/BroadcastGradientArgs*

Tidx0*
	keep_dims( *
T0*,
_class"
 loc:@loss_1/dense_5_loss/div_1*
_output_shapes
:
А
?training_1/SGD/gradients/loss_1/dense_5_loss/div_1_grad/ReshapeReshape;training_1/SGD/gradients/loss_1/dense_5_loss/div_1_grad/Sum=training_1/SGD/gradients/loss_1/dense_5_loss/div_1_grad/Shape*
T0*
Tshape0*,
_class"
 loc:@loss_1/dense_5_loss/div_1*#
_output_shapes
:џџџџџџџџџ
Й
;training_1/SGD/gradients/loss_1/dense_5_loss/div_1_grad/NegNegloss_1/dense_5_loss/mul_1*#
_output_shapes
:џџџџџџџџџ*
T0*,
_class"
 loc:@loss_1/dense_5_loss/div_1

Atraining_1/SGD/gradients/loss_1/dense_5_loss/div_1_grad/RealDiv_1RealDiv;training_1/SGD/gradients/loss_1/dense_5_loss/div_1_grad/Negloss_1/dense_5_loss/Mean_1*
T0*,
_class"
 loc:@loss_1/dense_5_loss/div_1*#
_output_shapes
:џџџџџџџџџ

Atraining_1/SGD/gradients/loss_1/dense_5_loss/div_1_grad/RealDiv_2RealDivAtraining_1/SGD/gradients/loss_1/dense_5_loss/div_1_grad/RealDiv_1loss_1/dense_5_loss/Mean_1*#
_output_shapes
:џџџџџџџџџ*
T0*,
_class"
 loc:@loss_1/dense_5_loss/div_1
Ѓ
;training_1/SGD/gradients/loss_1/dense_5_loss/div_1_grad/mulMul@training_1/SGD/gradients/loss_1/dense_5_loss/Mean_2_grad/truedivAtraining_1/SGD/gradients/loss_1/dense_5_loss/div_1_grad/RealDiv_2*
T0*,
_class"
 loc:@loss_1/dense_5_loss/div_1*#
_output_shapes
:џџџџџџџџџ
Р
=training_1/SGD/gradients/loss_1/dense_5_loss/div_1_grad/Sum_1Sum;training_1/SGD/gradients/loss_1/dense_5_loss/div_1_grad/mulOtraining_1/SGD/gradients/loss_1/dense_5_loss/div_1_grad/BroadcastGradientArgs:1*

Tidx0*
	keep_dims( *
T0*,
_class"
 loc:@loss_1/dense_5_loss/div_1*
_output_shapes
:
Љ
Atraining_1/SGD/gradients/loss_1/dense_5_loss/div_1_grad/Reshape_1Reshape=training_1/SGD/gradients/loss_1/dense_5_loss/div_1_grad/Sum_1?training_1/SGD/gradients/loss_1/dense_5_loss/div_1_grad/Shape_1*
T0*
Tshape0*,
_class"
 loc:@loss_1/dense_5_loss/div_1*
_output_shapes
: 
У
=training_1/SGD/gradients/loss_1/dense_5_loss/mul_1_grad/ShapeShapeloss_1/dense_5_loss/Mean*
T0*
out_type0*,
_class"
 loc:@loss_1/dense_5_loss/mul_1*
_output_shapes
:
Х
?training_1/SGD/gradients/loss_1/dense_5_loss/mul_1_grad/Shape_1Shapedense_5_sample_weights_1*
_output_shapes
:*
T0*
out_type0*,
_class"
 loc:@loss_1/dense_5_loss/mul_1
б
Mtraining_1/SGD/gradients/loss_1/dense_5_loss/mul_1_grad/BroadcastGradientArgsBroadcastGradientArgs=training_1/SGD/gradients/loss_1/dense_5_loss/mul_1_grad/Shape?training_1/SGD/gradients/loss_1/dense_5_loss/mul_1_grad/Shape_1*
T0*,
_class"
 loc:@loss_1/dense_5_loss/mul_1*2
_output_shapes 
:џџџџџџџџџ:џџџџџџџџџ
љ
;training_1/SGD/gradients/loss_1/dense_5_loss/mul_1_grad/mulMul?training_1/SGD/gradients/loss_1/dense_5_loss/div_1_grad/Reshapedense_5_sample_weights_1*
T0*,
_class"
 loc:@loss_1/dense_5_loss/mul_1*#
_output_shapes
:џџџџџџџџџ
М
;training_1/SGD/gradients/loss_1/dense_5_loss/mul_1_grad/SumSum;training_1/SGD/gradients/loss_1/dense_5_loss/mul_1_grad/mulMtraining_1/SGD/gradients/loss_1/dense_5_loss/mul_1_grad/BroadcastGradientArgs*
T0*,
_class"
 loc:@loss_1/dense_5_loss/mul_1*
_output_shapes
:*

Tidx0*
	keep_dims( 
А
?training_1/SGD/gradients/loss_1/dense_5_loss/mul_1_grad/ReshapeReshape;training_1/SGD/gradients/loss_1/dense_5_loss/mul_1_grad/Sum=training_1/SGD/gradients/loss_1/dense_5_loss/mul_1_grad/Shape*
T0*
Tshape0*,
_class"
 loc:@loss_1/dense_5_loss/mul_1*#
_output_shapes
:џџџџџџџџџ
ћ
=training_1/SGD/gradients/loss_1/dense_5_loss/mul_1_grad/mul_1Mulloss_1/dense_5_loss/Mean?training_1/SGD/gradients/loss_1/dense_5_loss/div_1_grad/Reshape*
T0*,
_class"
 loc:@loss_1/dense_5_loss/mul_1*#
_output_shapes
:џџџџџџџџџ
Т
=training_1/SGD/gradients/loss_1/dense_5_loss/mul_1_grad/Sum_1Sum=training_1/SGD/gradients/loss_1/dense_5_loss/mul_1_grad/mul_1Otraining_1/SGD/gradients/loss_1/dense_5_loss/mul_1_grad/BroadcastGradientArgs:1*

Tidx0*
	keep_dims( *
T0*,
_class"
 loc:@loss_1/dense_5_loss/mul_1*
_output_shapes
:
Ж
Atraining_1/SGD/gradients/loss_1/dense_5_loss/mul_1_grad/Reshape_1Reshape=training_1/SGD/gradients/loss_1/dense_5_loss/mul_1_grad/Sum_1?training_1/SGD/gradients/loss_1/dense_5_loss/mul_1_grad/Shape_1*
T0*
Tshape0*,
_class"
 loc:@loss_1/dense_5_loss/mul_1*#
_output_shapes
:џџџџџџџџџ
Р
<training_1/SGD/gradients/loss_1/dense_5_loss/Mean_grad/ShapeShapeloss_1/dense_5_loss/Neg*
T0*
out_type0*+
_class!
loc:@loss_1/dense_5_loss/Mean*
_output_shapes
:
Њ
;training_1/SGD/gradients/loss_1/dense_5_loss/Mean_grad/SizeConst*
_output_shapes
: *
value	B :*+
_class!
loc:@loss_1/dense_5_loss/Mean*
dtype0
њ
:training_1/SGD/gradients/loss_1/dense_5_loss/Mean_grad/addAdd*loss_1/dense_5_loss/Mean/reduction_indices;training_1/SGD/gradients/loss_1/dense_5_loss/Mean_grad/Size*
T0*+
_class!
loc:@loss_1/dense_5_loss/Mean*
_output_shapes
: 

:training_1/SGD/gradients/loss_1/dense_5_loss/Mean_grad/modFloorMod:training_1/SGD/gradients/loss_1/dense_5_loss/Mean_grad/add;training_1/SGD/gradients/loss_1/dense_5_loss/Mean_grad/Size*
T0*+
_class!
loc:@loss_1/dense_5_loss/Mean*
_output_shapes
: 
Е
>training_1/SGD/gradients/loss_1/dense_5_loss/Mean_grad/Shape_1Const*
valueB: *+
_class!
loc:@loss_1/dense_5_loss/Mean*
dtype0*
_output_shapes
:
Б
Btraining_1/SGD/gradients/loss_1/dense_5_loss/Mean_grad/range/startConst*
value	B : *+
_class!
loc:@loss_1/dense_5_loss/Mean*
dtype0*
_output_shapes
: 
Б
Btraining_1/SGD/gradients/loss_1/dense_5_loss/Mean_grad/range/deltaConst*
_output_shapes
: *
value	B :*+
_class!
loc:@loss_1/dense_5_loss/Mean*
dtype0
п
<training_1/SGD/gradients/loss_1/dense_5_loss/Mean_grad/rangeRangeBtraining_1/SGD/gradients/loss_1/dense_5_loss/Mean_grad/range/start;training_1/SGD/gradients/loss_1/dense_5_loss/Mean_grad/SizeBtraining_1/SGD/gradients/loss_1/dense_5_loss/Mean_grad/range/delta*
_output_shapes
:*

Tidx0*+
_class!
loc:@loss_1/dense_5_loss/Mean
А
Atraining_1/SGD/gradients/loss_1/dense_5_loss/Mean_grad/Fill/valueConst*
_output_shapes
: *
value	B :*+
_class!
loc:@loss_1/dense_5_loss/Mean*
dtype0

;training_1/SGD/gradients/loss_1/dense_5_loss/Mean_grad/FillFill>training_1/SGD/gradients/loss_1/dense_5_loss/Mean_grad/Shape_1Atraining_1/SGD/gradients/loss_1/dense_5_loss/Mean_grad/Fill/value*
T0*+
_class!
loc:@loss_1/dense_5_loss/Mean*
_output_shapes
: 
Ў
Dtraining_1/SGD/gradients/loss_1/dense_5_loss/Mean_grad/DynamicStitchDynamicStitch<training_1/SGD/gradients/loss_1/dense_5_loss/Mean_grad/range:training_1/SGD/gradients/loss_1/dense_5_loss/Mean_grad/mod<training_1/SGD/gradients/loss_1/dense_5_loss/Mean_grad/Shape;training_1/SGD/gradients/loss_1/dense_5_loss/Mean_grad/Fill*
T0*+
_class!
loc:@loss_1/dense_5_loss/Mean*
N*#
_output_shapes
:џџџџџџџџџ
Џ
@training_1/SGD/gradients/loss_1/dense_5_loss/Mean_grad/Maximum/yConst*
value	B :*+
_class!
loc:@loss_1/dense_5_loss/Mean*
dtype0*
_output_shapes
: 
Ќ
>training_1/SGD/gradients/loss_1/dense_5_loss/Mean_grad/MaximumMaximumDtraining_1/SGD/gradients/loss_1/dense_5_loss/Mean_grad/DynamicStitch@training_1/SGD/gradients/loss_1/dense_5_loss/Mean_grad/Maximum/y*#
_output_shapes
:џџџџџџџџџ*
T0*+
_class!
loc:@loss_1/dense_5_loss/Mean
Є
?training_1/SGD/gradients/loss_1/dense_5_loss/Mean_grad/floordivFloorDiv<training_1/SGD/gradients/loss_1/dense_5_loss/Mean_grad/Shape>training_1/SGD/gradients/loss_1/dense_5_loss/Mean_grad/Maximum*+
_class!
loc:@loss_1/dense_5_loss/Mean*#
_output_shapes
:џџџџџџџџџ*
T0
Ў
>training_1/SGD/gradients/loss_1/dense_5_loss/Mean_grad/ReshapeReshape?training_1/SGD/gradients/loss_1/dense_5_loss/mul_1_grad/ReshapeDtraining_1/SGD/gradients/loss_1/dense_5_loss/Mean_grad/DynamicStitch*
_output_shapes
:*
T0*
Tshape0*+
_class!
loc:@loss_1/dense_5_loss/Mean
І
;training_1/SGD/gradients/loss_1/dense_5_loss/Mean_grad/TileTile>training_1/SGD/gradients/loss_1/dense_5_loss/Mean_grad/Reshape?training_1/SGD/gradients/loss_1/dense_5_loss/Mean_grad/floordiv*
_output_shapes
:*

Tmultiples0*
T0*+
_class!
loc:@loss_1/dense_5_loss/Mean
Т
>training_1/SGD/gradients/loss_1/dense_5_loss/Mean_grad/Shape_2Shapeloss_1/dense_5_loss/Neg*
T0*
out_type0*+
_class!
loc:@loss_1/dense_5_loss/Mean*
_output_shapes
:
У
>training_1/SGD/gradients/loss_1/dense_5_loss/Mean_grad/Shape_3Shapeloss_1/dense_5_loss/Mean*
out_type0*+
_class!
loc:@loss_1/dense_5_loss/Mean*
_output_shapes
:*
T0
Г
<training_1/SGD/gradients/loss_1/dense_5_loss/Mean_grad/ConstConst*
valueB: *+
_class!
loc:@loss_1/dense_5_loss/Mean*
dtype0*
_output_shapes
:
Ќ
;training_1/SGD/gradients/loss_1/dense_5_loss/Mean_grad/ProdProd>training_1/SGD/gradients/loss_1/dense_5_loss/Mean_grad/Shape_2<training_1/SGD/gradients/loss_1/dense_5_loss/Mean_grad/Const*
_output_shapes
: *

Tidx0*
	keep_dims( *
T0*+
_class!
loc:@loss_1/dense_5_loss/Mean
Е
>training_1/SGD/gradients/loss_1/dense_5_loss/Mean_grad/Const_1Const*
dtype0*
_output_shapes
:*
valueB: *+
_class!
loc:@loss_1/dense_5_loss/Mean
А
=training_1/SGD/gradients/loss_1/dense_5_loss/Mean_grad/Prod_1Prod>training_1/SGD/gradients/loss_1/dense_5_loss/Mean_grad/Shape_3>training_1/SGD/gradients/loss_1/dense_5_loss/Mean_grad/Const_1*
T0*+
_class!
loc:@loss_1/dense_5_loss/Mean*
_output_shapes
: *

Tidx0*
	keep_dims( 
Б
Btraining_1/SGD/gradients/loss_1/dense_5_loss/Mean_grad/Maximum_1/yConst*
value	B :*+
_class!
loc:@loss_1/dense_5_loss/Mean*
dtype0*
_output_shapes
: 

@training_1/SGD/gradients/loss_1/dense_5_loss/Mean_grad/Maximum_1Maximum=training_1/SGD/gradients/loss_1/dense_5_loss/Mean_grad/Prod_1Btraining_1/SGD/gradients/loss_1/dense_5_loss/Mean_grad/Maximum_1/y*
T0*+
_class!
loc:@loss_1/dense_5_loss/Mean*
_output_shapes
: 

Atraining_1/SGD/gradients/loss_1/dense_5_loss/Mean_grad/floordiv_1FloorDiv;training_1/SGD/gradients/loss_1/dense_5_loss/Mean_grad/Prod@training_1/SGD/gradients/loss_1/dense_5_loss/Mean_grad/Maximum_1*
T0*+
_class!
loc:@loss_1/dense_5_loss/Mean*
_output_shapes
: 
у
;training_1/SGD/gradients/loss_1/dense_5_loss/Mean_grad/CastCastAtraining_1/SGD/gradients/loss_1/dense_5_loss/Mean_grad/floordiv_1*

SrcT0*+
_class!
loc:@loss_1/dense_5_loss/Mean*
_output_shapes
: *

DstT0

>training_1/SGD/gradients/loss_1/dense_5_loss/Mean_grad/truedivRealDiv;training_1/SGD/gradients/loss_1/dense_5_loss/Mean_grad/Tile;training_1/SGD/gradients/loss_1/dense_5_loss/Mean_grad/Cast*+
_class!
loc:@loss_1/dense_5_loss/Mean*#
_output_shapes
:џџџџџџџџџ*
T0
к
9training_1/SGD/gradients/loss_1/dense_5_loss/Neg_grad/NegNeg>training_1/SGD/gradients/loss_1/dense_5_loss/Mean_grad/truediv*
T0**
_class 
loc:@loss_1/dense_5_loss/Neg*#
_output_shapes
:џџџџџџџџџ
Т
=training_1/SGD/gradients/loss_1/dense_5_loss/Sum_1_grad/ShapeShapeloss_1/dense_5_loss/mul*
T0*
out_type0*,
_class"
 loc:@loss_1/dense_5_loss/Sum_1*
_output_shapes
:
Ќ
<training_1/SGD/gradients/loss_1/dense_5_loss/Sum_1_grad/SizeConst*
value	B :*,
_class"
 loc:@loss_1/dense_5_loss/Sum_1*
dtype0*
_output_shapes
: 
ќ
;training_1/SGD/gradients/loss_1/dense_5_loss/Sum_1_grad/addAdd+loss_1/dense_5_loss/Sum_1/reduction_indices<training_1/SGD/gradients/loss_1/dense_5_loss/Sum_1_grad/Size*
T0*,
_class"
 loc:@loss_1/dense_5_loss/Sum_1*
_output_shapes
: 

;training_1/SGD/gradients/loss_1/dense_5_loss/Sum_1_grad/modFloorMod;training_1/SGD/gradients/loss_1/dense_5_loss/Sum_1_grad/add<training_1/SGD/gradients/loss_1/dense_5_loss/Sum_1_grad/Size*
T0*,
_class"
 loc:@loss_1/dense_5_loss/Sum_1*
_output_shapes
: 
А
?training_1/SGD/gradients/loss_1/dense_5_loss/Sum_1_grad/Shape_1Const*
valueB *,
_class"
 loc:@loss_1/dense_5_loss/Sum_1*
dtype0*
_output_shapes
: 
Г
Ctraining_1/SGD/gradients/loss_1/dense_5_loss/Sum_1_grad/range/startConst*
value	B : *,
_class"
 loc:@loss_1/dense_5_loss/Sum_1*
dtype0*
_output_shapes
: 
Г
Ctraining_1/SGD/gradients/loss_1/dense_5_loss/Sum_1_grad/range/deltaConst*
value	B :*,
_class"
 loc:@loss_1/dense_5_loss/Sum_1*
dtype0*
_output_shapes
: 
ф
=training_1/SGD/gradients/loss_1/dense_5_loss/Sum_1_grad/rangeRangeCtraining_1/SGD/gradients/loss_1/dense_5_loss/Sum_1_grad/range/start<training_1/SGD/gradients/loss_1/dense_5_loss/Sum_1_grad/SizeCtraining_1/SGD/gradients/loss_1/dense_5_loss/Sum_1_grad/range/delta*,
_class"
 loc:@loss_1/dense_5_loss/Sum_1*
_output_shapes
:*

Tidx0
В
Btraining_1/SGD/gradients/loss_1/dense_5_loss/Sum_1_grad/Fill/valueConst*
value	B :*,
_class"
 loc:@loss_1/dense_5_loss/Sum_1*
dtype0*
_output_shapes
: 

<training_1/SGD/gradients/loss_1/dense_5_loss/Sum_1_grad/FillFill?training_1/SGD/gradients/loss_1/dense_5_loss/Sum_1_grad/Shape_1Btraining_1/SGD/gradients/loss_1/dense_5_loss/Sum_1_grad/Fill/value*
T0*,
_class"
 loc:@loss_1/dense_5_loss/Sum_1*
_output_shapes
: 
Д
Etraining_1/SGD/gradients/loss_1/dense_5_loss/Sum_1_grad/DynamicStitchDynamicStitch=training_1/SGD/gradients/loss_1/dense_5_loss/Sum_1_grad/range;training_1/SGD/gradients/loss_1/dense_5_loss/Sum_1_grad/mod=training_1/SGD/gradients/loss_1/dense_5_loss/Sum_1_grad/Shape<training_1/SGD/gradients/loss_1/dense_5_loss/Sum_1_grad/Fill*
T0*,
_class"
 loc:@loss_1/dense_5_loss/Sum_1*
N*#
_output_shapes
:џџџџџџџџџ
Б
Atraining_1/SGD/gradients/loss_1/dense_5_loss/Sum_1_grad/Maximum/yConst*
_output_shapes
: *
value	B :*,
_class"
 loc:@loss_1/dense_5_loss/Sum_1*
dtype0
А
?training_1/SGD/gradients/loss_1/dense_5_loss/Sum_1_grad/MaximumMaximumEtraining_1/SGD/gradients/loss_1/dense_5_loss/Sum_1_grad/DynamicStitchAtraining_1/SGD/gradients/loss_1/dense_5_loss/Sum_1_grad/Maximum/y*
T0*,
_class"
 loc:@loss_1/dense_5_loss/Sum_1*#
_output_shapes
:џџџџџџџџџ

@training_1/SGD/gradients/loss_1/dense_5_loss/Sum_1_grad/floordivFloorDiv=training_1/SGD/gradients/loss_1/dense_5_loss/Sum_1_grad/Shape?training_1/SGD/gradients/loss_1/dense_5_loss/Sum_1_grad/Maximum*
_output_shapes
:*
T0*,
_class"
 loc:@loss_1/dense_5_loss/Sum_1
Ћ
?training_1/SGD/gradients/loss_1/dense_5_loss/Sum_1_grad/ReshapeReshape9training_1/SGD/gradients/loss_1/dense_5_loss/Neg_grad/NegEtraining_1/SGD/gradients/loss_1/dense_5_loss/Sum_1_grad/DynamicStitch*
T0*
Tshape0*,
_class"
 loc:@loss_1/dense_5_loss/Sum_1*
_output_shapes
:
Й
<training_1/SGD/gradients/loss_1/dense_5_loss/Sum_1_grad/TileTile?training_1/SGD/gradients/loss_1/dense_5_loss/Sum_1_grad/Reshape@training_1/SGD/gradients/loss_1/dense_5_loss/Sum_1_grad/floordiv*

Tmultiples0*
T0*,
_class"
 loc:@loss_1/dense_5_loss/Sum_1*'
_output_shapes
:џџџџџџџџџ
З
;training_1/SGD/gradients/loss_1/dense_5_loss/mul_grad/ShapeShapedense_5_target_1*
T0*
out_type0**
_class 
loc:@loss_1/dense_5_loss/mul*
_output_shapes
:
Р
=training_1/SGD/gradients/loss_1/dense_5_loss/mul_grad/Shape_1Shapeloss_1/dense_5_loss/Log*
_output_shapes
:*
T0*
out_type0**
_class 
loc:@loss_1/dense_5_loss/mul
Щ
Ktraining_1/SGD/gradients/loss_1/dense_5_loss/mul_grad/BroadcastGradientArgsBroadcastGradientArgs;training_1/SGD/gradients/loss_1/dense_5_loss/mul_grad/Shape=training_1/SGD/gradients/loss_1/dense_5_loss/mul_grad/Shape_1*
T0**
_class 
loc:@loss_1/dense_5_loss/mul*2
_output_shapes 
:џџџџџџџџџ:џџџџџџџџџ
ѕ
9training_1/SGD/gradients/loss_1/dense_5_loss/mul_grad/mulMul<training_1/SGD/gradients/loss_1/dense_5_loss/Sum_1_grad/Tileloss_1/dense_5_loss/Log*
T0**
_class 
loc:@loss_1/dense_5_loss/mul*'
_output_shapes
:џџџџџџџџџ
Д
9training_1/SGD/gradients/loss_1/dense_5_loss/mul_grad/SumSum9training_1/SGD/gradients/loss_1/dense_5_loss/mul_grad/mulKtraining_1/SGD/gradients/loss_1/dense_5_loss/mul_grad/BroadcastGradientArgs*

Tidx0*
	keep_dims( *
T0**
_class 
loc:@loss_1/dense_5_loss/mul*
_output_shapes
:
Е
=training_1/SGD/gradients/loss_1/dense_5_loss/mul_grad/ReshapeReshape9training_1/SGD/gradients/loss_1/dense_5_loss/mul_grad/Sum;training_1/SGD/gradients/loss_1/dense_5_loss/mul_grad/Shape*
T0*
Tshape0**
_class 
loc:@loss_1/dense_5_loss/mul*0
_output_shapes
:џџџџџџџџџџџџџџџџџџ
№
;training_1/SGD/gradients/loss_1/dense_5_loss/mul_grad/mul_1Muldense_5_target_1<training_1/SGD/gradients/loss_1/dense_5_loss/Sum_1_grad/Tile*'
_output_shapes
:џџџџџџџџџ*
T0**
_class 
loc:@loss_1/dense_5_loss/mul
К
;training_1/SGD/gradients/loss_1/dense_5_loss/mul_grad/Sum_1Sum;training_1/SGD/gradients/loss_1/dense_5_loss/mul_grad/mul_1Mtraining_1/SGD/gradients/loss_1/dense_5_loss/mul_grad/BroadcastGradientArgs:1*

Tidx0*
	keep_dims( *
T0**
_class 
loc:@loss_1/dense_5_loss/mul*
_output_shapes
:
В
?training_1/SGD/gradients/loss_1/dense_5_loss/mul_grad/Reshape_1Reshape;training_1/SGD/gradients/loss_1/dense_5_loss/mul_grad/Sum_1=training_1/SGD/gradients/loss_1/dense_5_loss/mul_grad/Shape_1*
T0*
Tshape0**
_class 
loc:@loss_1/dense_5_loss/mul*'
_output_shapes
:џџџџџџџџџ

@training_1/SGD/gradients/loss_1/dense_5_loss/Log_grad/Reciprocal
Reciprocal!loss_1/dense_5_loss/clip_by_value@^training_1/SGD/gradients/loss_1/dense_5_loss/mul_grad/Reshape_1*'
_output_shapes
:џџџџџџџџџ*
T0**
_class 
loc:@loss_1/dense_5_loss/Log
Ё
9training_1/SGD/gradients/loss_1/dense_5_loss/Log_grad/mulMul?training_1/SGD/gradients/loss_1/dense_5_loss/mul_grad/Reshape_1@training_1/SGD/gradients/loss_1/dense_5_loss/Log_grad/Reciprocal*
T0**
_class 
loc:@loss_1/dense_5_loss/Log*'
_output_shapes
:џџџџџџџџџ
ф
Etraining_1/SGD/gradients/loss_1/dense_5_loss/clip_by_value_grad/ShapeShape)loss_1/dense_5_loss/clip_by_value/Minimum*
T0*
out_type0*4
_class*
(&loc:@loss_1/dense_5_loss/clip_by_value*
_output_shapes
:
Р
Gtraining_1/SGD/gradients/loss_1/dense_5_loss/clip_by_value_grad/Shape_1Const*
valueB *4
_class*
(&loc:@loss_1/dense_5_loss/clip_by_value*
dtype0*
_output_shapes
: 
і
Gtraining_1/SGD/gradients/loss_1/dense_5_loss/clip_by_value_grad/Shape_2Shape9training_1/SGD/gradients/loss_1/dense_5_loss/Log_grad/mul*
T0*
out_type0*4
_class*
(&loc:@loss_1/dense_5_loss/clip_by_value*
_output_shapes
:
Ц
Ktraining_1/SGD/gradients/loss_1/dense_5_loss/clip_by_value_grad/zeros/ConstConst*
valueB
 *    *4
_class*
(&loc:@loss_1/dense_5_loss/clip_by_value*
dtype0*
_output_shapes
: 
Ы
Etraining_1/SGD/gradients/loss_1/dense_5_loss/clip_by_value_grad/zerosFillGtraining_1/SGD/gradients/loss_1/dense_5_loss/clip_by_value_grad/Shape_2Ktraining_1/SGD/gradients/loss_1/dense_5_loss/clip_by_value_grad/zeros/Const*
T0*4
_class*
(&loc:@loss_1/dense_5_loss/clip_by_value*'
_output_shapes
:џџџџџџџџџ

Ltraining_1/SGD/gradients/loss_1/dense_5_loss/clip_by_value_grad/GreaterEqualGreaterEqual)loss_1/dense_5_loss/clip_by_value/Minimumloss_1/dense_5_loss/Const*'
_output_shapes
:џџџџџџџџџ*
T0*4
_class*
(&loc:@loss_1/dense_5_loss/clip_by_value
ё
Utraining_1/SGD/gradients/loss_1/dense_5_loss/clip_by_value_grad/BroadcastGradientArgsBroadcastGradientArgsEtraining_1/SGD/gradients/loss_1/dense_5_loss/clip_by_value_grad/ShapeGtraining_1/SGD/gradients/loss_1/dense_5_loss/clip_by_value_grad/Shape_1*
T0*4
_class*
(&loc:@loss_1/dense_5_loss/clip_by_value*2
_output_shapes 
:џџџџџџџџџ:џџџџџџџџџ

Ftraining_1/SGD/gradients/loss_1/dense_5_loss/clip_by_value_grad/SelectSelectLtraining_1/SGD/gradients/loss_1/dense_5_loss/clip_by_value_grad/GreaterEqual9training_1/SGD/gradients/loss_1/dense_5_loss/Log_grad/mulEtraining_1/SGD/gradients/loss_1/dense_5_loss/clip_by_value_grad/zeros*
T0*4
_class*
(&loc:@loss_1/dense_5_loss/clip_by_value*'
_output_shapes
:џџџџџџџџџ

Jtraining_1/SGD/gradients/loss_1/dense_5_loss/clip_by_value_grad/LogicalNot
LogicalNotLtraining_1/SGD/gradients/loss_1/dense_5_loss/clip_by_value_grad/GreaterEqual*4
_class*
(&loc:@loss_1/dense_5_loss/clip_by_value*'
_output_shapes
:џџџџџџџџџ

Htraining_1/SGD/gradients/loss_1/dense_5_loss/clip_by_value_grad/Select_1SelectJtraining_1/SGD/gradients/loss_1/dense_5_loss/clip_by_value_grad/LogicalNot9training_1/SGD/gradients/loss_1/dense_5_loss/Log_grad/mulEtraining_1/SGD/gradients/loss_1/dense_5_loss/clip_by_value_grad/zeros*'
_output_shapes
:џџџџџџџџџ*
T0*4
_class*
(&loc:@loss_1/dense_5_loss/clip_by_value
п
Ctraining_1/SGD/gradients/loss_1/dense_5_loss/clip_by_value_grad/SumSumFtraining_1/SGD/gradients/loss_1/dense_5_loss/clip_by_value_grad/SelectUtraining_1/SGD/gradients/loss_1/dense_5_loss/clip_by_value_grad/BroadcastGradientArgs*
T0*4
_class*
(&loc:@loss_1/dense_5_loss/clip_by_value*
_output_shapes
:*

Tidx0*
	keep_dims( 
д
Gtraining_1/SGD/gradients/loss_1/dense_5_loss/clip_by_value_grad/ReshapeReshapeCtraining_1/SGD/gradients/loss_1/dense_5_loss/clip_by_value_grad/SumEtraining_1/SGD/gradients/loss_1/dense_5_loss/clip_by_value_grad/Shape*
T0*
Tshape0*4
_class*
(&loc:@loss_1/dense_5_loss/clip_by_value*'
_output_shapes
:џџџџџџџџџ
х
Etraining_1/SGD/gradients/loss_1/dense_5_loss/clip_by_value_grad/Sum_1SumHtraining_1/SGD/gradients/loss_1/dense_5_loss/clip_by_value_grad/Select_1Wtraining_1/SGD/gradients/loss_1/dense_5_loss/clip_by_value_grad/BroadcastGradientArgs:1*
T0*4
_class*
(&loc:@loss_1/dense_5_loss/clip_by_value*
_output_shapes
:*

Tidx0*
	keep_dims( 
Щ
Itraining_1/SGD/gradients/loss_1/dense_5_loss/clip_by_value_grad/Reshape_1ReshapeEtraining_1/SGD/gradients/loss_1/dense_5_loss/clip_by_value_grad/Sum_1Gtraining_1/SGD/gradients/loss_1/dense_5_loss/clip_by_value_grad/Shape_1*
T0*
Tshape0*4
_class*
(&loc:@loss_1/dense_5_loss/clip_by_value*
_output_shapes
: 
т
Mtraining_1/SGD/gradients/loss_1/dense_5_loss/clip_by_value/Minimum_grad/ShapeShapeloss_1/dense_5_loss/div*
T0*
out_type0*<
_class2
0.loc:@loss_1/dense_5_loss/clip_by_value/Minimum*
_output_shapes
:
а
Otraining_1/SGD/gradients/loss_1/dense_5_loss/clip_by_value/Minimum_grad/Shape_1Const*
valueB *<
_class2
0.loc:@loss_1/dense_5_loss/clip_by_value/Minimum*
dtype0*
_output_shapes
: 

Otraining_1/SGD/gradients/loss_1/dense_5_loss/clip_by_value/Minimum_grad/Shape_2ShapeGtraining_1/SGD/gradients/loss_1/dense_5_loss/clip_by_value_grad/Reshape*
_output_shapes
:*
T0*
out_type0*<
_class2
0.loc:@loss_1/dense_5_loss/clip_by_value/Minimum
ж
Straining_1/SGD/gradients/loss_1/dense_5_loss/clip_by_value/Minimum_grad/zeros/ConstConst*
valueB
 *    *<
_class2
0.loc:@loss_1/dense_5_loss/clip_by_value/Minimum*
dtype0*
_output_shapes
: 
ы
Mtraining_1/SGD/gradients/loss_1/dense_5_loss/clip_by_value/Minimum_grad/zerosFillOtraining_1/SGD/gradients/loss_1/dense_5_loss/clip_by_value/Minimum_grad/Shape_2Straining_1/SGD/gradients/loss_1/dense_5_loss/clip_by_value/Minimum_grad/zeros/Const*
T0*<
_class2
0.loc:@loss_1/dense_5_loss/clip_by_value/Minimum*'
_output_shapes
:џџџџџџџџџ

Qtraining_1/SGD/gradients/loss_1/dense_5_loss/clip_by_value/Minimum_grad/LessEqual	LessEqualloss_1/dense_5_loss/divloss_1/dense_5_loss/sub*
T0*<
_class2
0.loc:@loss_1/dense_5_loss/clip_by_value/Minimum*'
_output_shapes
:џџџџџџџџџ

]training_1/SGD/gradients/loss_1/dense_5_loss/clip_by_value/Minimum_grad/BroadcastGradientArgsBroadcastGradientArgsMtraining_1/SGD/gradients/loss_1/dense_5_loss/clip_by_value/Minimum_grad/ShapeOtraining_1/SGD/gradients/loss_1/dense_5_loss/clip_by_value/Minimum_grad/Shape_1*
T0*<
_class2
0.loc:@loss_1/dense_5_loss/clip_by_value/Minimum*2
_output_shapes 
:џџџџџџџџџ:џџџџџџџџџ
Г
Ntraining_1/SGD/gradients/loss_1/dense_5_loss/clip_by_value/Minimum_grad/SelectSelectQtraining_1/SGD/gradients/loss_1/dense_5_loss/clip_by_value/Minimum_grad/LessEqualGtraining_1/SGD/gradients/loss_1/dense_5_loss/clip_by_value_grad/ReshapeMtraining_1/SGD/gradients/loss_1/dense_5_loss/clip_by_value/Minimum_grad/zeros*
T0*<
_class2
0.loc:@loss_1/dense_5_loss/clip_by_value/Minimum*'
_output_shapes
:џџџџџџџџџ

Rtraining_1/SGD/gradients/loss_1/dense_5_loss/clip_by_value/Minimum_grad/LogicalNot
LogicalNotQtraining_1/SGD/gradients/loss_1/dense_5_loss/clip_by_value/Minimum_grad/LessEqual*'
_output_shapes
:џџџџџџџџџ*<
_class2
0.loc:@loss_1/dense_5_loss/clip_by_value/Minimum
Ж
Ptraining_1/SGD/gradients/loss_1/dense_5_loss/clip_by_value/Minimum_grad/Select_1SelectRtraining_1/SGD/gradients/loss_1/dense_5_loss/clip_by_value/Minimum_grad/LogicalNotGtraining_1/SGD/gradients/loss_1/dense_5_loss/clip_by_value_grad/ReshapeMtraining_1/SGD/gradients/loss_1/dense_5_loss/clip_by_value/Minimum_grad/zeros*<
_class2
0.loc:@loss_1/dense_5_loss/clip_by_value/Minimum*'
_output_shapes
:џџџџџџџџџ*
T0
џ
Ktraining_1/SGD/gradients/loss_1/dense_5_loss/clip_by_value/Minimum_grad/SumSumNtraining_1/SGD/gradients/loss_1/dense_5_loss/clip_by_value/Minimum_grad/Select]training_1/SGD/gradients/loss_1/dense_5_loss/clip_by_value/Minimum_grad/BroadcastGradientArgs*
_output_shapes
:*

Tidx0*
	keep_dims( *
T0*<
_class2
0.loc:@loss_1/dense_5_loss/clip_by_value/Minimum
є
Otraining_1/SGD/gradients/loss_1/dense_5_loss/clip_by_value/Minimum_grad/ReshapeReshapeKtraining_1/SGD/gradients/loss_1/dense_5_loss/clip_by_value/Minimum_grad/SumMtraining_1/SGD/gradients/loss_1/dense_5_loss/clip_by_value/Minimum_grad/Shape*'
_output_shapes
:џџџџџџџџџ*
T0*
Tshape0*<
_class2
0.loc:@loss_1/dense_5_loss/clip_by_value/Minimum

Mtraining_1/SGD/gradients/loss_1/dense_5_loss/clip_by_value/Minimum_grad/Sum_1SumPtraining_1/SGD/gradients/loss_1/dense_5_loss/clip_by_value/Minimum_grad/Select_1_training_1/SGD/gradients/loss_1/dense_5_loss/clip_by_value/Minimum_grad/BroadcastGradientArgs:1*

Tidx0*
	keep_dims( *
T0*<
_class2
0.loc:@loss_1/dense_5_loss/clip_by_value/Minimum*
_output_shapes
:
щ
Qtraining_1/SGD/gradients/loss_1/dense_5_loss/clip_by_value/Minimum_grad/Reshape_1ReshapeMtraining_1/SGD/gradients/loss_1/dense_5_loss/clip_by_value/Minimum_grad/Sum_1Otraining_1/SGD/gradients/loss_1/dense_5_loss/clip_by_value/Minimum_grad/Shape_1*
T0*
Tshape0*<
_class2
0.loc:@loss_1/dense_5_loss/clip_by_value/Minimum*
_output_shapes
: 
И
;training_1/SGD/gradients/loss_1/dense_5_loss/div_grad/ShapeShapedense_5_1/Sigmoid*
T0*
out_type0**
_class 
loc:@loss_1/dense_5_loss/div*
_output_shapes
:
Р
=training_1/SGD/gradients/loss_1/dense_5_loss/div_grad/Shape_1Shapeloss_1/dense_5_loss/Sum*
_output_shapes
:*
T0*
out_type0**
_class 
loc:@loss_1/dense_5_loss/div
Щ
Ktraining_1/SGD/gradients/loss_1/dense_5_loss/div_grad/BroadcastGradientArgsBroadcastGradientArgs;training_1/SGD/gradients/loss_1/dense_5_loss/div_grad/Shape=training_1/SGD/gradients/loss_1/dense_5_loss/div_grad/Shape_1**
_class 
loc:@loss_1/dense_5_loss/div*2
_output_shapes 
:џџџџџџџџџ:џџџџџџџџџ*
T0

=training_1/SGD/gradients/loss_1/dense_5_loss/div_grad/RealDivRealDivOtraining_1/SGD/gradients/loss_1/dense_5_loss/clip_by_value/Minimum_grad/Reshapeloss_1/dense_5_loss/Sum*
T0**
_class 
loc:@loss_1/dense_5_loss/div*'
_output_shapes
:џџџџџџџџџ
И
9training_1/SGD/gradients/loss_1/dense_5_loss/div_grad/SumSum=training_1/SGD/gradients/loss_1/dense_5_loss/div_grad/RealDivKtraining_1/SGD/gradients/loss_1/dense_5_loss/div_grad/BroadcastGradientArgs**
_class 
loc:@loss_1/dense_5_loss/div*
_output_shapes
:*

Tidx0*
	keep_dims( *
T0
Ќ
=training_1/SGD/gradients/loss_1/dense_5_loss/div_grad/ReshapeReshape9training_1/SGD/gradients/loss_1/dense_5_loss/div_grad/Sum;training_1/SGD/gradients/loss_1/dense_5_loss/div_grad/Shape*
T0*
Tshape0**
_class 
loc:@loss_1/dense_5_loss/div*'
_output_shapes
:џџџџџџџџџ
Б
9training_1/SGD/gradients/loss_1/dense_5_loss/div_grad/NegNegdense_5_1/Sigmoid*
T0**
_class 
loc:@loss_1/dense_5_loss/div*'
_output_shapes
:џџџџџџџџџ
ќ
?training_1/SGD/gradients/loss_1/dense_5_loss/div_grad/RealDiv_1RealDiv9training_1/SGD/gradients/loss_1/dense_5_loss/div_grad/Negloss_1/dense_5_loss/Sum*
T0**
_class 
loc:@loss_1/dense_5_loss/div*'
_output_shapes
:џџџџџџџџџ

?training_1/SGD/gradients/loss_1/dense_5_loss/div_grad/RealDiv_2RealDiv?training_1/SGD/gradients/loss_1/dense_5_loss/div_grad/RealDiv_1loss_1/dense_5_loss/Sum*
T0**
_class 
loc:@loss_1/dense_5_loss/div*'
_output_shapes
:џџџџџџџџџ
А
9training_1/SGD/gradients/loss_1/dense_5_loss/div_grad/mulMulOtraining_1/SGD/gradients/loss_1/dense_5_loss/clip_by_value/Minimum_grad/Reshape?training_1/SGD/gradients/loss_1/dense_5_loss/div_grad/RealDiv_2*
T0**
_class 
loc:@loss_1/dense_5_loss/div*'
_output_shapes
:џџџџџџџџџ
И
;training_1/SGD/gradients/loss_1/dense_5_loss/div_grad/Sum_1Sum9training_1/SGD/gradients/loss_1/dense_5_loss/div_grad/mulMtraining_1/SGD/gradients/loss_1/dense_5_loss/div_grad/BroadcastGradientArgs:1*
T0**
_class 
loc:@loss_1/dense_5_loss/div*
_output_shapes
:*

Tidx0*
	keep_dims( 
В
?training_1/SGD/gradients/loss_1/dense_5_loss/div_grad/Reshape_1Reshape;training_1/SGD/gradients/loss_1/dense_5_loss/div_grad/Sum_1=training_1/SGD/gradients/loss_1/dense_5_loss/div_grad/Shape_1*
Tshape0**
_class 
loc:@loss_1/dense_5_loss/div*'
_output_shapes
:џџџџџџџџџ*
T0
И
;training_1/SGD/gradients/loss_1/dense_5_loss/Sum_grad/ShapeShapedense_5_1/Sigmoid*
T0*
out_type0**
_class 
loc:@loss_1/dense_5_loss/Sum*
_output_shapes
:
Ј
:training_1/SGD/gradients/loss_1/dense_5_loss/Sum_grad/SizeConst*
value	B :**
_class 
loc:@loss_1/dense_5_loss/Sum*
dtype0*
_output_shapes
: 
є
9training_1/SGD/gradients/loss_1/dense_5_loss/Sum_grad/addAdd)loss_1/dense_5_loss/Sum/reduction_indices:training_1/SGD/gradients/loss_1/dense_5_loss/Sum_grad/Size*
T0**
_class 
loc:@loss_1/dense_5_loss/Sum*
_output_shapes
: 

9training_1/SGD/gradients/loss_1/dense_5_loss/Sum_grad/modFloorMod9training_1/SGD/gradients/loss_1/dense_5_loss/Sum_grad/add:training_1/SGD/gradients/loss_1/dense_5_loss/Sum_grad/Size*
_output_shapes
: *
T0**
_class 
loc:@loss_1/dense_5_loss/Sum
Ќ
=training_1/SGD/gradients/loss_1/dense_5_loss/Sum_grad/Shape_1Const*
valueB **
_class 
loc:@loss_1/dense_5_loss/Sum*
dtype0*
_output_shapes
: 
Џ
Atraining_1/SGD/gradients/loss_1/dense_5_loss/Sum_grad/range/startConst*
dtype0*
_output_shapes
: *
value	B : **
_class 
loc:@loss_1/dense_5_loss/Sum
Џ
Atraining_1/SGD/gradients/loss_1/dense_5_loss/Sum_grad/range/deltaConst*
value	B :**
_class 
loc:@loss_1/dense_5_loss/Sum*
dtype0*
_output_shapes
: 
к
;training_1/SGD/gradients/loss_1/dense_5_loss/Sum_grad/rangeRangeAtraining_1/SGD/gradients/loss_1/dense_5_loss/Sum_grad/range/start:training_1/SGD/gradients/loss_1/dense_5_loss/Sum_grad/SizeAtraining_1/SGD/gradients/loss_1/dense_5_loss/Sum_grad/range/delta**
_class 
loc:@loss_1/dense_5_loss/Sum*
_output_shapes
:*

Tidx0
Ў
@training_1/SGD/gradients/loss_1/dense_5_loss/Sum_grad/Fill/valueConst*
value	B :**
_class 
loc:@loss_1/dense_5_loss/Sum*
dtype0*
_output_shapes
: 

:training_1/SGD/gradients/loss_1/dense_5_loss/Sum_grad/FillFill=training_1/SGD/gradients/loss_1/dense_5_loss/Sum_grad/Shape_1@training_1/SGD/gradients/loss_1/dense_5_loss/Sum_grad/Fill/value**
_class 
loc:@loss_1/dense_5_loss/Sum*
_output_shapes
: *
T0
Ј
Ctraining_1/SGD/gradients/loss_1/dense_5_loss/Sum_grad/DynamicStitchDynamicStitch;training_1/SGD/gradients/loss_1/dense_5_loss/Sum_grad/range9training_1/SGD/gradients/loss_1/dense_5_loss/Sum_grad/mod;training_1/SGD/gradients/loss_1/dense_5_loss/Sum_grad/Shape:training_1/SGD/gradients/loss_1/dense_5_loss/Sum_grad/Fill**
_class 
loc:@loss_1/dense_5_loss/Sum*
N*#
_output_shapes
:џџџџџџџџџ*
T0
­
?training_1/SGD/gradients/loss_1/dense_5_loss/Sum_grad/Maximum/yConst*
value	B :**
_class 
loc:@loss_1/dense_5_loss/Sum*
dtype0*
_output_shapes
: 
Ј
=training_1/SGD/gradients/loss_1/dense_5_loss/Sum_grad/MaximumMaximumCtraining_1/SGD/gradients/loss_1/dense_5_loss/Sum_grad/DynamicStitch?training_1/SGD/gradients/loss_1/dense_5_loss/Sum_grad/Maximum/y*
T0**
_class 
loc:@loss_1/dense_5_loss/Sum*#
_output_shapes
:џџџџџџџџџ

>training_1/SGD/gradients/loss_1/dense_5_loss/Sum_grad/floordivFloorDiv;training_1/SGD/gradients/loss_1/dense_5_loss/Sum_grad/Shape=training_1/SGD/gradients/loss_1/dense_5_loss/Sum_grad/Maximum*
T0**
_class 
loc:@loss_1/dense_5_loss/Sum*
_output_shapes
:
Ћ
=training_1/SGD/gradients/loss_1/dense_5_loss/Sum_grad/ReshapeReshape?training_1/SGD/gradients/loss_1/dense_5_loss/div_grad/Reshape_1Ctraining_1/SGD/gradients/loss_1/dense_5_loss/Sum_grad/DynamicStitch*
T0*
Tshape0**
_class 
loc:@loss_1/dense_5_loss/Sum*
_output_shapes
:
Б
:training_1/SGD/gradients/loss_1/dense_5_loss/Sum_grad/TileTile=training_1/SGD/gradients/loss_1/dense_5_loss/Sum_grad/Reshape>training_1/SGD/gradients/loss_1/dense_5_loss/Sum_grad/floordiv*

Tmultiples0*
T0**
_class 
loc:@loss_1/dense_5_loss/Sum*'
_output_shapes
:џџџџџџџџџ

training_1/SGD/gradients/AddNAddN=training_1/SGD/gradients/loss_1/dense_5_loss/div_grad/Reshape:training_1/SGD/gradients/loss_1/dense_5_loss/Sum_grad/Tile*
N*'
_output_shapes
:џџџџџџџџџ*
T0**
_class 
loc:@loss_1/dense_5_loss/div
д
;training_1/SGD/gradients/dense_5_1/Sigmoid_grad/SigmoidGradSigmoidGraddense_5_1/Sigmoidtraining_1/SGD/gradients/AddN*'
_output_shapes
:џџџџџџџџџ*
T0*$
_class
loc:@dense_5_1/Sigmoid
щ
;training_1/SGD/gradients/dense_5_1/BiasAdd_grad/BiasAddGradBiasAddGrad;training_1/SGD/gradients/dense_5_1/Sigmoid_grad/SigmoidGrad*
T0*$
_class
loc:@dense_5_1/BiasAdd*
data_formatNHWC*
_output_shapes
:

5training_1/SGD/gradients/dense_5_1/MatMul_grad/MatMulMatMul;training_1/SGD/gradients/dense_5_1/Sigmoid_grad/SigmoidGraddense_5_1/kernel/read*
T0*#
_class
loc:@dense_5_1/MatMul*'
_output_shapes
:џџџџџџџџџ*
transpose_a( *
transpose_b(

7training_1/SGD/gradients/dense_5_1/MatMul_grad/MatMul_1MatMuldense_4_1/Relu;training_1/SGD/gradients/dense_5_1/Sigmoid_grad/SigmoidGrad*
transpose_b( *
T0*#
_class
loc:@dense_5_1/MatMul*
_output_shapes

:*
transpose_a(
н
5training_1/SGD/gradients/dense_4_1/Relu_grad/ReluGradReluGrad5training_1/SGD/gradients/dense_5_1/MatMul_grad/MatMuldense_4_1/Relu*'
_output_shapes
:џџџџџџџџџ*
T0*!
_class
loc:@dense_4_1/Relu
у
;training_1/SGD/gradients/dense_4_1/BiasAdd_grad/BiasAddGradBiasAddGrad5training_1/SGD/gradients/dense_4_1/Relu_grad/ReluGrad*
_output_shapes
:*
T0*$
_class
loc:@dense_4_1/BiasAdd*
data_formatNHWC

5training_1/SGD/gradients/dense_4_1/MatMul_grad/MatMulMatMul5training_1/SGD/gradients/dense_4_1/Relu_grad/ReluGraddense_4_1/kernel/read*#
_class
loc:@dense_4_1/MatMul*'
_output_shapes
:џџџџџџџџџ2*
transpose_a( *
transpose_b(*
T0
ќ
7training_1/SGD/gradients/dense_4_1/MatMul_grad/MatMul_1MatMuldense_3_1/Relu5training_1/SGD/gradients/dense_4_1/Relu_grad/ReluGrad*
T0*#
_class
loc:@dense_4_1/MatMul*
_output_shapes

:2*
transpose_a(*
transpose_b( 
н
5training_1/SGD/gradients/dense_3_1/Relu_grad/ReluGradReluGrad5training_1/SGD/gradients/dense_4_1/MatMul_grad/MatMuldense_3_1/Relu*
T0*!
_class
loc:@dense_3_1/Relu*'
_output_shapes
:џџџџџџџџџ2
у
;training_1/SGD/gradients/dense_3_1/BiasAdd_grad/BiasAddGradBiasAddGrad5training_1/SGD/gradients/dense_3_1/Relu_grad/ReluGrad*
T0*$
_class
loc:@dense_3_1/BiasAdd*
data_formatNHWC*
_output_shapes
:2

5training_1/SGD/gradients/dense_3_1/MatMul_grad/MatMulMatMul5training_1/SGD/gradients/dense_3_1/Relu_grad/ReluGraddense_3_1/kernel/read*
T0*#
_class
loc:@dense_3_1/MatMul*'
_output_shapes
:џџџџџџџџџF*
transpose_a( *
transpose_b(
ќ
7training_1/SGD/gradients/dense_3_1/MatMul_grad/MatMul_1MatMuldense_2_1/Relu5training_1/SGD/gradients/dense_3_1/Relu_grad/ReluGrad*
T0*#
_class
loc:@dense_3_1/MatMul*
_output_shapes

:F2*
transpose_a(*
transpose_b( 
н
5training_1/SGD/gradients/dense_2_1/Relu_grad/ReluGradReluGrad5training_1/SGD/gradients/dense_3_1/MatMul_grad/MatMuldense_2_1/Relu*
T0*!
_class
loc:@dense_2_1/Relu*'
_output_shapes
:џџџџџџџџџF
у
;training_1/SGD/gradients/dense_2_1/BiasAdd_grad/BiasAddGradBiasAddGrad5training_1/SGD/gradients/dense_2_1/Relu_grad/ReluGrad*
T0*$
_class
loc:@dense_2_1/BiasAdd*
data_formatNHWC*
_output_shapes
:F

5training_1/SGD/gradients/dense_2_1/MatMul_grad/MatMulMatMul5training_1/SGD/gradients/dense_2_1/Relu_grad/ReluGraddense_2_1/kernel/read*
transpose_b(*
T0*#
_class
loc:@dense_2_1/MatMul*'
_output_shapes
:џџџџџџџџџd*
transpose_a( 
ќ
7training_1/SGD/gradients/dense_2_1/MatMul_grad/MatMul_1MatMuldense_1_1/Relu5training_1/SGD/gradients/dense_2_1/Relu_grad/ReluGrad*
T0*#
_class
loc:@dense_2_1/MatMul*
_output_shapes

:dF*
transpose_a(*
transpose_b( 
н
5training_1/SGD/gradients/dense_1_1/Relu_grad/ReluGradReluGrad5training_1/SGD/gradients/dense_2_1/MatMul_grad/MatMuldense_1_1/Relu*
T0*!
_class
loc:@dense_1_1/Relu*'
_output_shapes
:џџџџџџџџџd
у
;training_1/SGD/gradients/dense_1_1/BiasAdd_grad/BiasAddGradBiasAddGrad5training_1/SGD/gradients/dense_1_1/Relu_grad/ReluGrad*
T0*$
_class
loc:@dense_1_1/BiasAdd*
data_formatNHWC*
_output_shapes
:d

5training_1/SGD/gradients/dense_1_1/MatMul_grad/MatMulMatMul5training_1/SGD/gradients/dense_1_1/Relu_grad/ReluGraddense_1_1/kernel/read*
T0*#
_class
loc:@dense_1_1/MatMul*'
_output_shapes
:џџџџџџџџџ7*
transpose_a( *
transpose_b(
§
7training_1/SGD/gradients/dense_1_1/MatMul_grad/MatMul_1MatMuldense_1_input_15training_1/SGD/gradients/dense_1_1/Relu_grad/ReluGrad*
T0*#
_class
loc:@dense_1_1/MatMul*
_output_shapes

:7d*
transpose_a(*
transpose_b( 
`
training_1/SGD/AssignAdd/valueConst*
value	B	 R*
dtype0	*
_output_shapes
: 
А
training_1/SGD/AssignAdd	AssignAddSGD_1/iterationstraining_1/SGD/AssignAdd/value*#
_class
loc:@SGD_1/iterations*
_output_shapes
: *
use_locking( *
T0	
i
training_1/SGD/ConstConst*
valueB7d*    *
dtype0*
_output_shapes

:7d

training_1/SGD/Variable
VariableV2*
shape
:7d*
shared_name *
dtype0*
_output_shapes

:7d*
	container 
е
training_1/SGD/Variable/AssignAssigntraining_1/SGD/Variabletraining_1/SGD/Const**
_class 
loc:@training_1/SGD/Variable*
validate_shape(*
_output_shapes

:7d*
use_locking(*
T0

training_1/SGD/Variable/readIdentitytraining_1/SGD/Variable*
T0**
_class 
loc:@training_1/SGD/Variable*
_output_shapes

:7d
c
training_1/SGD/Const_1Const*
valueBd*    *
dtype0*
_output_shapes
:d

training_1/SGD/Variable_1
VariableV2*
dtype0*
_output_shapes
:d*
	container *
shape:d*
shared_name 
й
 training_1/SGD/Variable_1/AssignAssigntraining_1/SGD/Variable_1training_1/SGD/Const_1*
use_locking(*
T0*,
_class"
 loc:@training_1/SGD/Variable_1*
validate_shape(*
_output_shapes
:d

training_1/SGD/Variable_1/readIdentitytraining_1/SGD/Variable_1*
_output_shapes
:d*
T0*,
_class"
 loc:@training_1/SGD/Variable_1
k
training_1/SGD/Const_2Const*
valueBdF*    *
dtype0*
_output_shapes

:dF

training_1/SGD/Variable_2
VariableV2*
shared_name *
dtype0*
_output_shapes

:dF*
	container *
shape
:dF
н
 training_1/SGD/Variable_2/AssignAssigntraining_1/SGD/Variable_2training_1/SGD/Const_2*
_output_shapes

:dF*
use_locking(*
T0*,
_class"
 loc:@training_1/SGD/Variable_2*
validate_shape(

training_1/SGD/Variable_2/readIdentitytraining_1/SGD/Variable_2*
T0*,
_class"
 loc:@training_1/SGD/Variable_2*
_output_shapes

:dF
c
training_1/SGD/Const_3Const*
_output_shapes
:F*
valueBF*    *
dtype0

training_1/SGD/Variable_3
VariableV2*
_output_shapes
:F*
	container *
shape:F*
shared_name *
dtype0
й
 training_1/SGD/Variable_3/AssignAssigntraining_1/SGD/Variable_3training_1/SGD/Const_3*
use_locking(*
T0*,
_class"
 loc:@training_1/SGD/Variable_3*
validate_shape(*
_output_shapes
:F

training_1/SGD/Variable_3/readIdentitytraining_1/SGD/Variable_3*,
_class"
 loc:@training_1/SGD/Variable_3*
_output_shapes
:F*
T0
k
training_1/SGD/Const_4Const*
valueBF2*    *
dtype0*
_output_shapes

:F2

training_1/SGD/Variable_4
VariableV2*
dtype0*
_output_shapes

:F2*
	container *
shape
:F2*
shared_name 
н
 training_1/SGD/Variable_4/AssignAssigntraining_1/SGD/Variable_4training_1/SGD/Const_4*
use_locking(*
T0*,
_class"
 loc:@training_1/SGD/Variable_4*
validate_shape(*
_output_shapes

:F2

training_1/SGD/Variable_4/readIdentitytraining_1/SGD/Variable_4*
T0*,
_class"
 loc:@training_1/SGD/Variable_4*
_output_shapes

:F2
c
training_1/SGD/Const_5Const*
valueB2*    *
dtype0*
_output_shapes
:2

training_1/SGD/Variable_5
VariableV2*
dtype0*
_output_shapes
:2*
	container *
shape:2*
shared_name 
й
 training_1/SGD/Variable_5/AssignAssigntraining_1/SGD/Variable_5training_1/SGD/Const_5*
use_locking(*
T0*,
_class"
 loc:@training_1/SGD/Variable_5*
validate_shape(*
_output_shapes
:2

training_1/SGD/Variable_5/readIdentitytraining_1/SGD/Variable_5*
T0*,
_class"
 loc:@training_1/SGD/Variable_5*
_output_shapes
:2
k
training_1/SGD/Const_6Const*
valueB2*    *
dtype0*
_output_shapes

:2

training_1/SGD/Variable_6
VariableV2*
dtype0*
_output_shapes

:2*
	container *
shape
:2*
shared_name 
н
 training_1/SGD/Variable_6/AssignAssigntraining_1/SGD/Variable_6training_1/SGD/Const_6*
validate_shape(*
_output_shapes

:2*
use_locking(*
T0*,
_class"
 loc:@training_1/SGD/Variable_6

training_1/SGD/Variable_6/readIdentitytraining_1/SGD/Variable_6*
_output_shapes

:2*
T0*,
_class"
 loc:@training_1/SGD/Variable_6
c
training_1/SGD/Const_7Const*
valueB*    *
dtype0*
_output_shapes
:

training_1/SGD/Variable_7
VariableV2*
_output_shapes
:*
	container *
shape:*
shared_name *
dtype0
й
 training_1/SGD/Variable_7/AssignAssigntraining_1/SGD/Variable_7training_1/SGD/Const_7*
use_locking(*
T0*,
_class"
 loc:@training_1/SGD/Variable_7*
validate_shape(*
_output_shapes
:

training_1/SGD/Variable_7/readIdentitytraining_1/SGD/Variable_7*
T0*,
_class"
 loc:@training_1/SGD/Variable_7*
_output_shapes
:
k
training_1/SGD/Const_8Const*
dtype0*
_output_shapes

:*
valueB*    

training_1/SGD/Variable_8
VariableV2*
dtype0*
_output_shapes

:*
	container *
shape
:*
shared_name 
н
 training_1/SGD/Variable_8/AssignAssigntraining_1/SGD/Variable_8training_1/SGD/Const_8*
T0*,
_class"
 loc:@training_1/SGD/Variable_8*
validate_shape(*
_output_shapes

:*
use_locking(

training_1/SGD/Variable_8/readIdentitytraining_1/SGD/Variable_8*,
_class"
 loc:@training_1/SGD/Variable_8*
_output_shapes

:*
T0
c
training_1/SGD/Const_9Const*
valueB*    *
dtype0*
_output_shapes
:

training_1/SGD/Variable_9
VariableV2*
shape:*
shared_name *
dtype0*
_output_shapes
:*
	container 
й
 training_1/SGD/Variable_9/AssignAssigntraining_1/SGD/Variable_9training_1/SGD/Const_9*
T0*,
_class"
 loc:@training_1/SGD/Variable_9*
validate_shape(*
_output_shapes
:*
use_locking(

training_1/SGD/Variable_9/readIdentitytraining_1/SGD/Variable_9*
T0*,
_class"
 loc:@training_1/SGD/Variable_9*
_output_shapes
:
u
training_1/SGD/mulMulSGD_1/momentum/readtraining_1/SGD/Variable/read*
T0*
_output_shapes

:7d

training_1/SGD/mul_1MulSGD_1/lr/read7training_1/SGD/gradients/dense_1_1/MatMul_grad/MatMul_1*
T0*
_output_shapes

:7d
l
training_1/SGD/subSubtraining_1/SGD/multraining_1/SGD/mul_1*
T0*
_output_shapes

:7d
Ъ
training_1/SGD/AssignAssigntraining_1/SGD/Variabletraining_1/SGD/sub*
validate_shape(*
_output_shapes

:7d*
use_locking(*
T0**
_class 
loc:@training_1/SGD/Variable
m
training_1/SGD/addAdddense_1_1/kernel/readtraining_1/SGD/sub*
T0*
_output_shapes

:7d
О
training_1/SGD/Assign_1Assigndense_1_1/kerneltraining_1/SGD/add*
use_locking(*
T0*#
_class
loc:@dense_1_1/kernel*
validate_shape(*
_output_shapes

:7d
u
training_1/SGD/mul_2MulSGD_1/momentum/readtraining_1/SGD/Variable_1/read*
T0*
_output_shapes
:d

training_1/SGD/mul_3MulSGD_1/lr/read;training_1/SGD/gradients/dense_1_1/BiasAdd_grad/BiasAddGrad*
T0*
_output_shapes
:d
l
training_1/SGD/sub_1Subtraining_1/SGD/mul_2training_1/SGD/mul_3*
T0*
_output_shapes
:d
Ю
training_1/SGD/Assign_2Assigntraining_1/SGD/Variable_1training_1/SGD/sub_1*
use_locking(*
T0*,
_class"
 loc:@training_1/SGD/Variable_1*
validate_shape(*
_output_shapes
:d
k
training_1/SGD/add_1Adddense_1_1/bias/readtraining_1/SGD/sub_1*
_output_shapes
:d*
T0
И
training_1/SGD/Assign_3Assigndense_1_1/biastraining_1/SGD/add_1*!
_class
loc:@dense_1_1/bias*
validate_shape(*
_output_shapes
:d*
use_locking(*
T0
y
training_1/SGD/mul_4MulSGD_1/momentum/readtraining_1/SGD/Variable_2/read*
T0*
_output_shapes

:dF

training_1/SGD/mul_5MulSGD_1/lr/read7training_1/SGD/gradients/dense_2_1/MatMul_grad/MatMul_1*
_output_shapes

:dF*
T0
p
training_1/SGD/sub_2Subtraining_1/SGD/mul_4training_1/SGD/mul_5*
_output_shapes

:dF*
T0
в
training_1/SGD/Assign_4Assigntraining_1/SGD/Variable_2training_1/SGD/sub_2*
use_locking(*
T0*,
_class"
 loc:@training_1/SGD/Variable_2*
validate_shape(*
_output_shapes

:dF
q
training_1/SGD/add_2Adddense_2_1/kernel/readtraining_1/SGD/sub_2*
_output_shapes

:dF*
T0
Р
training_1/SGD/Assign_5Assigndense_2_1/kerneltraining_1/SGD/add_2*
use_locking(*
T0*#
_class
loc:@dense_2_1/kernel*
validate_shape(*
_output_shapes

:dF
u
training_1/SGD/mul_6MulSGD_1/momentum/readtraining_1/SGD/Variable_3/read*
T0*
_output_shapes
:F

training_1/SGD/mul_7MulSGD_1/lr/read;training_1/SGD/gradients/dense_2_1/BiasAdd_grad/BiasAddGrad*
T0*
_output_shapes
:F
l
training_1/SGD/sub_3Subtraining_1/SGD/mul_6training_1/SGD/mul_7*
T0*
_output_shapes
:F
Ю
training_1/SGD/Assign_6Assigntraining_1/SGD/Variable_3training_1/SGD/sub_3*
use_locking(*
T0*,
_class"
 loc:@training_1/SGD/Variable_3*
validate_shape(*
_output_shapes
:F
k
training_1/SGD/add_3Adddense_2_1/bias/readtraining_1/SGD/sub_3*
_output_shapes
:F*
T0
И
training_1/SGD/Assign_7Assigndense_2_1/biastraining_1/SGD/add_3*
use_locking(*
T0*!
_class
loc:@dense_2_1/bias*
validate_shape(*
_output_shapes
:F
y
training_1/SGD/mul_8MulSGD_1/momentum/readtraining_1/SGD/Variable_4/read*
T0*
_output_shapes

:F2

training_1/SGD/mul_9MulSGD_1/lr/read7training_1/SGD/gradients/dense_3_1/MatMul_grad/MatMul_1*
_output_shapes

:F2*
T0
p
training_1/SGD/sub_4Subtraining_1/SGD/mul_8training_1/SGD/mul_9*
T0*
_output_shapes

:F2
в
training_1/SGD/Assign_8Assigntraining_1/SGD/Variable_4training_1/SGD/sub_4*
use_locking(*
T0*,
_class"
 loc:@training_1/SGD/Variable_4*
validate_shape(*
_output_shapes

:F2
q
training_1/SGD/add_4Adddense_3_1/kernel/readtraining_1/SGD/sub_4*
_output_shapes

:F2*
T0
Р
training_1/SGD/Assign_9Assigndense_3_1/kerneltraining_1/SGD/add_4*
_output_shapes

:F2*
use_locking(*
T0*#
_class
loc:@dense_3_1/kernel*
validate_shape(
v
training_1/SGD/mul_10MulSGD_1/momentum/readtraining_1/SGD/Variable_5/read*
T0*
_output_shapes
:2

training_1/SGD/mul_11MulSGD_1/lr/read;training_1/SGD/gradients/dense_3_1/BiasAdd_grad/BiasAddGrad*
T0*
_output_shapes
:2
n
training_1/SGD/sub_5Subtraining_1/SGD/mul_10training_1/SGD/mul_11*
_output_shapes
:2*
T0
Я
training_1/SGD/Assign_10Assigntraining_1/SGD/Variable_5training_1/SGD/sub_5*
use_locking(*
T0*,
_class"
 loc:@training_1/SGD/Variable_5*
validate_shape(*
_output_shapes
:2
k
training_1/SGD/add_5Adddense_3_1/bias/readtraining_1/SGD/sub_5*
_output_shapes
:2*
T0
Й
training_1/SGD/Assign_11Assigndense_3_1/biastraining_1/SGD/add_5*
T0*!
_class
loc:@dense_3_1/bias*
validate_shape(*
_output_shapes
:2*
use_locking(
z
training_1/SGD/mul_12MulSGD_1/momentum/readtraining_1/SGD/Variable_6/read*
T0*
_output_shapes

:2

training_1/SGD/mul_13MulSGD_1/lr/read7training_1/SGD/gradients/dense_4_1/MatMul_grad/MatMul_1*
T0*
_output_shapes

:2
r
training_1/SGD/sub_6Subtraining_1/SGD/mul_12training_1/SGD/mul_13*
T0*
_output_shapes

:2
г
training_1/SGD/Assign_12Assigntraining_1/SGD/Variable_6training_1/SGD/sub_6*
use_locking(*
T0*,
_class"
 loc:@training_1/SGD/Variable_6*
validate_shape(*
_output_shapes

:2
q
training_1/SGD/add_6Adddense_4_1/kernel/readtraining_1/SGD/sub_6*
T0*
_output_shapes

:2
С
training_1/SGD/Assign_13Assigndense_4_1/kerneltraining_1/SGD/add_6*
T0*#
_class
loc:@dense_4_1/kernel*
validate_shape(*
_output_shapes

:2*
use_locking(
v
training_1/SGD/mul_14MulSGD_1/momentum/readtraining_1/SGD/Variable_7/read*
T0*
_output_shapes
:

training_1/SGD/mul_15MulSGD_1/lr/read;training_1/SGD/gradients/dense_4_1/BiasAdd_grad/BiasAddGrad*
_output_shapes
:*
T0
n
training_1/SGD/sub_7Subtraining_1/SGD/mul_14training_1/SGD/mul_15*
T0*
_output_shapes
:
Я
training_1/SGD/Assign_14Assigntraining_1/SGD/Variable_7training_1/SGD/sub_7*
use_locking(*
T0*,
_class"
 loc:@training_1/SGD/Variable_7*
validate_shape(*
_output_shapes
:
k
training_1/SGD/add_7Adddense_4_1/bias/readtraining_1/SGD/sub_7*
T0*
_output_shapes
:
Й
training_1/SGD/Assign_15Assigndense_4_1/biastraining_1/SGD/add_7*
T0*!
_class
loc:@dense_4_1/bias*
validate_shape(*
_output_shapes
:*
use_locking(
z
training_1/SGD/mul_16MulSGD_1/momentum/readtraining_1/SGD/Variable_8/read*
T0*
_output_shapes

:

training_1/SGD/mul_17MulSGD_1/lr/read7training_1/SGD/gradients/dense_5_1/MatMul_grad/MatMul_1*
T0*
_output_shapes

:
r
training_1/SGD/sub_8Subtraining_1/SGD/mul_16training_1/SGD/mul_17*
T0*
_output_shapes

:
г
training_1/SGD/Assign_16Assigntraining_1/SGD/Variable_8training_1/SGD/sub_8*,
_class"
 loc:@training_1/SGD/Variable_8*
validate_shape(*
_output_shapes

:*
use_locking(*
T0
q
training_1/SGD/add_8Adddense_5_1/kernel/readtraining_1/SGD/sub_8*
T0*
_output_shapes

:
С
training_1/SGD/Assign_17Assigndense_5_1/kerneltraining_1/SGD/add_8*
use_locking(*
T0*#
_class
loc:@dense_5_1/kernel*
validate_shape(*
_output_shapes

:
v
training_1/SGD/mul_18MulSGD_1/momentum/readtraining_1/SGD/Variable_9/read*
T0*
_output_shapes
:

training_1/SGD/mul_19MulSGD_1/lr/read;training_1/SGD/gradients/dense_5_1/BiasAdd_grad/BiasAddGrad*
_output_shapes
:*
T0
n
training_1/SGD/sub_9Subtraining_1/SGD/mul_18training_1/SGD/mul_19*
T0*
_output_shapes
:
Я
training_1/SGD/Assign_18Assigntraining_1/SGD/Variable_9training_1/SGD/sub_9*
validate_shape(*
_output_shapes
:*
use_locking(*
T0*,
_class"
 loc:@training_1/SGD/Variable_9
k
training_1/SGD/add_9Adddense_5_1/bias/readtraining_1/SGD/sub_9*
_output_shapes
:*
T0
Й
training_1/SGD/Assign_19Assigndense_5_1/biastraining_1/SGD/add_9*
use_locking(*
T0*!
_class
loc:@dense_5_1/bias*
validate_shape(*
_output_shapes
:
ъ
training_1/group_depsNoOp^loss_1/mul^metrics_1/acc/Mean^training_1/SGD/AssignAdd^training_1/SGD/Assign^training_1/SGD/Assign_1^training_1/SGD/Assign_2^training_1/SGD/Assign_3^training_1/SGD/Assign_4^training_1/SGD/Assign_5^training_1/SGD/Assign_6^training_1/SGD/Assign_7^training_1/SGD/Assign_8^training_1/SGD/Assign_9^training_1/SGD/Assign_10^training_1/SGD/Assign_11^training_1/SGD/Assign_12^training_1/SGD/Assign_13^training_1/SGD/Assign_14^training_1/SGD/Assign_15^training_1/SGD/Assign_16^training_1/SGD/Assign_17^training_1/SGD/Assign_18^training_1/SGD/Assign_19
У
init_2NoOp^SGD_1/iterations/Assign^SGD_1/lr/Assign^SGD_1/momentum/Assign^SGD_1/decay/Assign^training_1/SGD/Variable/Assign!^training_1/SGD/Variable_1/Assign!^training_1/SGD/Variable_2/Assign!^training_1/SGD/Variable_3/Assign!^training_1/SGD/Variable_4/Assign!^training_1/SGD/Variable_5/Assign!^training_1/SGD/Variable_6/Assign!^training_1/SGD/Variable_7/Assign!^training_1/SGD/Variable_8/Assign!^training_1/SGD/Variable_9/Assign
O
Placeholder_10Placeholder*
dtype0	*
_output_shapes
: *
shape: 
Є
	Assign_10AssignSGD_1/iterationsPlaceholder_10*
use_locking( *
T0	*#
_class
loc:@SGD_1/iterations*
validate_shape(*
_output_shapes
: 
_
Placeholder_11Placeholder*
dtype0*
_output_shapes

:7d*
shape
:7d
К
	Assign_11Assigntraining_1/SGD/VariablePlaceholder_11*
validate_shape(*
_output_shapes

:7d*
use_locking( *
T0**
_class 
loc:@training_1/SGD/Variable
W
Placeholder_12Placeholder*
shape:d*
dtype0*
_output_shapes
:d
К
	Assign_12Assigntraining_1/SGD/Variable_1Placeholder_12*
use_locking( *
T0*,
_class"
 loc:@training_1/SGD/Variable_1*
validate_shape(*
_output_shapes
:d
_
Placeholder_13Placeholder*
dtype0*
_output_shapes

:dF*
shape
:dF
О
	Assign_13Assigntraining_1/SGD/Variable_2Placeholder_13*
use_locking( *
T0*,
_class"
 loc:@training_1/SGD/Variable_2*
validate_shape(*
_output_shapes

:dF
W
Placeholder_14Placeholder*
dtype0*
_output_shapes
:F*
shape:F
К
	Assign_14Assigntraining_1/SGD/Variable_3Placeholder_14*
T0*,
_class"
 loc:@training_1/SGD/Variable_3*
validate_shape(*
_output_shapes
:F*
use_locking( 
_
Placeholder_15Placeholder*
dtype0*
_output_shapes

:F2*
shape
:F2
О
	Assign_15Assigntraining_1/SGD/Variable_4Placeholder_15*,
_class"
 loc:@training_1/SGD/Variable_4*
validate_shape(*
_output_shapes

:F2*
use_locking( *
T0
W
Placeholder_16Placeholder*
_output_shapes
:2*
shape:2*
dtype0
К
	Assign_16Assigntraining_1/SGD/Variable_5Placeholder_16*
use_locking( *
T0*,
_class"
 loc:@training_1/SGD/Variable_5*
validate_shape(*
_output_shapes
:2
_
Placeholder_17Placeholder*
dtype0*
_output_shapes

:2*
shape
:2
О
	Assign_17Assigntraining_1/SGD/Variable_6Placeholder_17*
use_locking( *
T0*,
_class"
 loc:@training_1/SGD/Variable_6*
validate_shape(*
_output_shapes

:2
W
Placeholder_18Placeholder*
dtype0*
_output_shapes
:*
shape:
К
	Assign_18Assigntraining_1/SGD/Variable_7Placeholder_18*
use_locking( *
T0*,
_class"
 loc:@training_1/SGD/Variable_7*
validate_shape(*
_output_shapes
:
_
Placeholder_19Placeholder*
shape
:*
dtype0*
_output_shapes

:
О
	Assign_19Assigntraining_1/SGD/Variable_8Placeholder_19*
use_locking( *
T0*,
_class"
 loc:@training_1/SGD/Variable_8*
validate_shape(*
_output_shapes

:
W
Placeholder_20Placeholder*
dtype0*
_output_shapes
:*
shape:
К
	Assign_20Assigntraining_1/SGD/Variable_9Placeholder_20*
use_locking( *
T0*,
_class"
 loc:@training_1/SGD/Variable_9*
validate_shape(*
_output_shapes
:
`
SGD_2/iterations/initial_valueConst*
_output_shapes
: *
value	B	 R *
dtype0	
t
SGD_2/iterations
VariableV2*
dtype0	*
_output_shapes
: *
	container *
shape: *
shared_name 
Т
SGD_2/iterations/AssignAssignSGD_2/iterationsSGD_2/iterations/initial_value*#
_class
loc:@SGD_2/iterations*
validate_shape(*
_output_shapes
: *
use_locking(*
T0	
y
SGD_2/iterations/readIdentitySGD_2/iterations*
T0	*#
_class
loc:@SGD_2/iterations*
_output_shapes
: 
[
SGD_2/lr/initial_valueConst*
valueB
 *ІD;*
dtype0*
_output_shapes
: 
l
SGD_2/lr
VariableV2*
shared_name *
dtype0*
_output_shapes
: *
	container *
shape: 
Ђ
SGD_2/lr/AssignAssignSGD_2/lrSGD_2/lr/initial_value*
_output_shapes
: *
use_locking(*
T0*
_class
loc:@SGD_2/lr*
validate_shape(
a
SGD_2/lr/readIdentitySGD_2/lr*
_output_shapes
: *
T0*
_class
loc:@SGD_2/lr
a
SGD_2/momentum/initial_valueConst*
dtype0*
_output_shapes
: *
valueB
 *    
r
SGD_2/momentum
VariableV2*
dtype0*
_output_shapes
: *
	container *
shape: *
shared_name 
К
SGD_2/momentum/AssignAssignSGD_2/momentumSGD_2/momentum/initial_value*
use_locking(*
T0*!
_class
loc:@SGD_2/momentum*
validate_shape(*
_output_shapes
: 
s
SGD_2/momentum/readIdentitySGD_2/momentum*
_output_shapes
: *
T0*!
_class
loc:@SGD_2/momentum
^
SGD_2/decay/initial_valueConst*
_output_shapes
: *
valueB
 *    *
dtype0
o
SGD_2/decay
VariableV2*
dtype0*
_output_shapes
: *
	container *
shape: *
shared_name 
Ў
SGD_2/decay/AssignAssignSGD_2/decaySGD_2/decay/initial_value*
validate_shape(*
_output_shapes
: *
use_locking(*
T0*
_class
loc:@SGD_2/decay
j
SGD_2/decay/readIdentitySGD_2/decay*
_class
loc:@SGD_2/decay*
_output_shapes
: *
T0

dense_5_target_2Placeholder*
dtype0*0
_output_shapes
:џџџџџџџџџџџџџџџџџџ*%
shape:џџџџџџџџџџџџџџџџџџ
s
dense_5_sample_weights_2Placeholder*
dtype0*#
_output_shapes
:џџџџџџџџџ*
shape:џџџџџџџџџ
k
)loss_2/dense_5_loss/Sum/reduction_indicesConst*
value	B :*
dtype0*
_output_shapes
: 
Ћ
loss_2/dense_5_loss/SumSumdense_5_1/Sigmoid)loss_2/dense_5_loss/Sum/reduction_indices*
T0*'
_output_shapes
:џџџџџџџџџ*
	keep_dims(*

Tidx0

loss_2/dense_5_loss/divRealDivdense_5_1/Sigmoidloss_2/dense_5_loss/Sum*
T0*'
_output_shapes
:џџџџџџџџџ
^
loss_2/dense_5_loss/ConstConst*
valueB
 *Пж3*
dtype0*
_output_shapes
: 
^
loss_2/dense_5_loss/sub/xConst*
valueB
 *  ?*
dtype0*
_output_shapes
: 
u
loss_2/dense_5_loss/subSubloss_2/dense_5_loss/sub/xloss_2/dense_5_loss/Const*
T0*
_output_shapes
: 

)loss_2/dense_5_loss/clip_by_value/MinimumMinimumloss_2/dense_5_loss/divloss_2/dense_5_loss/sub*
T0*'
_output_shapes
:џџџџџџџџџ
Є
!loss_2/dense_5_loss/clip_by_valueMaximum)loss_2/dense_5_loss/clip_by_value/Minimumloss_2/dense_5_loss/Const*
T0*'
_output_shapes
:џџџџџџџџџ
s
loss_2/dense_5_loss/LogLog!loss_2/dense_5_loss/clip_by_value*'
_output_shapes
:џџџџџџџџџ*
T0
{
loss_2/dense_5_loss/mulMuldense_5_target_2loss_2/dense_5_loss/Log*'
_output_shapes
:џџџџџџџџџ*
T0
m
+loss_2/dense_5_loss/Sum_1/reduction_indicesConst*
dtype0*
_output_shapes
: *
value	B :
Б
loss_2/dense_5_loss/Sum_1Sumloss_2/dense_5_loss/mul+loss_2/dense_5_loss/Sum_1/reduction_indices*
	keep_dims( *

Tidx0*
T0*#
_output_shapes
:џџџџџџџџџ
g
loss_2/dense_5_loss/NegNegloss_2/dense_5_loss/Sum_1*
T0*#
_output_shapes
:џџџџџџџџџ
m
*loss_2/dense_5_loss/Mean/reduction_indicesConst*
dtype0*
_output_shapes
: *
valueB 
А
loss_2/dense_5_loss/MeanMeanloss_2/dense_5_loss/Neg*loss_2/dense_5_loss/Mean/reduction_indices*#
_output_shapes
:џџџџџџџџџ*
	keep_dims( *

Tidx0*
T0

loss_2/dense_5_loss/mul_1Mulloss_2/dense_5_loss/Meandense_5_sample_weights_2*
T0*#
_output_shapes
:џџџџџџџџџ
c
loss_2/dense_5_loss/NotEqual/yConst*
valueB
 *    *
dtype0*
_output_shapes
: 

loss_2/dense_5_loss/NotEqualNotEqualdense_5_sample_weights_2loss_2/dense_5_loss/NotEqual/y*
T0*#
_output_shapes
:џџџџџџџџџ
{
loss_2/dense_5_loss/CastCastloss_2/dense_5_loss/NotEqual*

SrcT0
*#
_output_shapes
:џџџџџџџџџ*

DstT0
e
loss_2/dense_5_loss/Const_1Const*
valueB: *
dtype0*
_output_shapes
:

loss_2/dense_5_loss/Mean_1Meanloss_2/dense_5_loss/Castloss_2/dense_5_loss/Const_1*
	keep_dims( *

Tidx0*
T0*
_output_shapes
: 

loss_2/dense_5_loss/div_1RealDivloss_2/dense_5_loss/mul_1loss_2/dense_5_loss/Mean_1*
T0*#
_output_shapes
:џџџџџџџџџ
e
loss_2/dense_5_loss/Const_2Const*
valueB: *
dtype0*
_output_shapes
:

loss_2/dense_5_loss/Mean_2Meanloss_2/dense_5_loss/div_1loss_2/dense_5_loss/Const_2*
_output_shapes
: *
	keep_dims( *

Tidx0*
T0
Q
loss_2/mul/xConst*
valueB
 *  ?*
dtype0*
_output_shapes
: 
\

loss_2/mulMulloss_2/mul/xloss_2/dense_5_loss/Mean_2*
T0*
_output_shapes
: 
i
metrics_2/acc/ArgMax/dimensionConst*
_output_shapes
: *
valueB :
џџџџџџџџџ*
dtype0

metrics_2/acc/ArgMaxArgMaxdense_5_target_2metrics_2/acc/ArgMax/dimension*
T0*
output_type0	*#
_output_shapes
:џџџџџџџџџ*

Tidx0
k
 metrics_2/acc/ArgMax_1/dimensionConst*
valueB :
џџџџџџџџџ*
dtype0*
_output_shapes
: 
Ђ
metrics_2/acc/ArgMax_1ArgMaxdense_5_1/Sigmoid metrics_2/acc/ArgMax_1/dimension*#
_output_shapes
:џџџџџџџџџ*

Tidx0*
T0*
output_type0	
x
metrics_2/acc/EqualEqualmetrics_2/acc/ArgMaxmetrics_2/acc/ArgMax_1*
T0	*#
_output_shapes
:џџџџџџџџџ
l
metrics_2/acc/CastCastmetrics_2/acc/Equal*

SrcT0
*#
_output_shapes
:џџџџџџџџџ*

DstT0
]
metrics_2/acc/ConstConst*
dtype0*
_output_shapes
:*
valueB: 

metrics_2/acc/MeanMeanmetrics_2/acc/Castmetrics_2/acc/Const*
_output_shapes
: *
	keep_dims( *

Tidx0*
T0
4

group_depsNoOp^loss_2/mul^metrics_2/acc/Mean
g
init_3NoOp^SGD_2/iterations/Assign^SGD_2/lr/Assign^SGD_2/momentum/Assign^SGD_2/decay/Assign
P

save/ConstConst*
_output_shapes
: *
valueB Bmodel*
dtype0

save/StringJoin/inputs_1Const*<
value3B1 B+_temp_ff5a5829bbc24766b7e00351e98ceb05/part*
dtype0*
_output_shapes
: 
u
save/StringJoin
StringJoin
save/Constsave/StringJoin/inputs_1*
N*
_output_shapes
: *
	separator 
Q
save/num_shardsConst*
value	B :*
dtype0*
_output_shapes
: 
\
save/ShardedFilename/shardConst*
dtype0*
_output_shapes
: *
value	B : 
}
save/ShardedFilenameShardedFilenamesave/StringJoinsave/ShardedFilename/shardsave/num_shards*
_output_shapes
: 
Щ
save/SaveV2/tensor_namesConst*ќ
valueђBя4B	SGD/decayBSGD/iterationsBSGD/lrBSGD/momentumBSGD_1/decayBSGD_1/iterationsBSGD_1/lrBSGD_1/momentumBSGD_2/decayBSGD_2/iterationsBSGD_2/lrBSGD_2/momentumBdense_1/biasBdense_1/kernelBdense_1_1/biasBdense_1_1/kernelBdense_2/biasBdense_2/kernelBdense_2_1/biasBdense_2_1/kernelBdense_3/biasBdense_3/kernelBdense_3_1/biasBdense_3_1/kernelBdense_4/biasBdense_4/kernelBdense_4_1/biasBdense_4_1/kernelBdense_5/biasBdense_5/kernelBdense_5_1/biasBdense_5_1/kernelBtraining/SGD/VariableBtraining/SGD/Variable_1Btraining/SGD/Variable_2Btraining/SGD/Variable_3Btraining/SGD/Variable_4Btraining/SGD/Variable_5Btraining/SGD/Variable_6Btraining/SGD/Variable_7Btraining/SGD/Variable_8Btraining/SGD/Variable_9Btraining_1/SGD/VariableBtraining_1/SGD/Variable_1Btraining_1/SGD/Variable_2Btraining_1/SGD/Variable_3Btraining_1/SGD/Variable_4Btraining_1/SGD/Variable_5Btraining_1/SGD/Variable_6Btraining_1/SGD/Variable_7Btraining_1/SGD/Variable_8Btraining_1/SGD/Variable_9*
dtype0*
_output_shapes
:4
Ы
save/SaveV2/shape_and_slicesConst*{
valuerBp4B B B B B B B B B B B B B B B B B B B B B B B B B B B B B B B B B B B B B B B B B B B B B B B B B B B B *
dtype0*
_output_shapes
:4
	
save/SaveV2SaveV2save/ShardedFilenamesave/SaveV2/tensor_namessave/SaveV2/shape_and_slices	SGD/decaySGD/iterationsSGD/lrSGD/momentumSGD_1/decaySGD_1/iterationsSGD_1/lrSGD_1/momentumSGD_2/decaySGD_2/iterationsSGD_2/lrSGD_2/momentumdense_1/biasdense_1/kerneldense_1_1/biasdense_1_1/kerneldense_2/biasdense_2/kerneldense_2_1/biasdense_2_1/kerneldense_3/biasdense_3/kerneldense_3_1/biasdense_3_1/kerneldense_4/biasdense_4/kerneldense_4_1/biasdense_4_1/kerneldense_5/biasdense_5/kerneldense_5_1/biasdense_5_1/kerneltraining/SGD/Variabletraining/SGD/Variable_1training/SGD/Variable_2training/SGD/Variable_3training/SGD/Variable_4training/SGD/Variable_5training/SGD/Variable_6training/SGD/Variable_7training/SGD/Variable_8training/SGD/Variable_9training_1/SGD/Variabletraining_1/SGD/Variable_1training_1/SGD/Variable_2training_1/SGD/Variable_3training_1/SGD/Variable_4training_1/SGD/Variable_5training_1/SGD/Variable_6training_1/SGD/Variable_7training_1/SGD/Variable_8training_1/SGD/Variable_9*B
dtypes8
624			

save/control_dependencyIdentitysave/ShardedFilename^save/SaveV2*
T0*'
_class
loc:@save/ShardedFilename*
_output_shapes
: 

+save/MergeV2Checkpoints/checkpoint_prefixesPacksave/ShardedFilename^save/control_dependency*
T0*

axis *
N*
_output_shapes
:
}
save/MergeV2CheckpointsMergeV2Checkpoints+save/MergeV2Checkpoints/checkpoint_prefixes
save/Const*
delete_old_dirs(
z
save/IdentityIdentity
save/Const^save/control_dependency^save/MergeV2Checkpoints*
T0*
_output_shapes
: 
m
save/RestoreV2/tensor_namesConst*
valueBB	SGD/decay*
dtype0*
_output_shapes
:
h
save/RestoreV2/shape_and_slicesConst*
valueB
B *
dtype0*
_output_shapes
:

save/RestoreV2	RestoreV2
save/Constsave/RestoreV2/tensor_namessave/RestoreV2/shape_and_slices*
_output_shapes
:*
dtypes
2

save/AssignAssign	SGD/decaysave/RestoreV2*
use_locking(*
T0*
_class
loc:@SGD/decay*
validate_shape(*
_output_shapes
: 
t
save/RestoreV2_1/tensor_namesConst*#
valueBBSGD/iterations*
dtype0*
_output_shapes
:
j
!save/RestoreV2_1/shape_and_slicesConst*
valueB
B *
dtype0*
_output_shapes
:

save/RestoreV2_1	RestoreV2
save/Constsave/RestoreV2_1/tensor_names!save/RestoreV2_1/shape_and_slices*
_output_shapes
:*
dtypes
2	
І
save/Assign_1AssignSGD/iterationssave/RestoreV2_1*
_output_shapes
: *
use_locking(*
T0	*!
_class
loc:@SGD/iterations*
validate_shape(
l
save/RestoreV2_2/tensor_namesConst*
valueBBSGD/lr*
dtype0*
_output_shapes
:
j
!save/RestoreV2_2/shape_and_slicesConst*
_output_shapes
:*
valueB
B *
dtype0

save/RestoreV2_2	RestoreV2
save/Constsave/RestoreV2_2/tensor_names!save/RestoreV2_2/shape_and_slices*
_output_shapes
:*
dtypes
2

save/Assign_2AssignSGD/lrsave/RestoreV2_2*
use_locking(*
T0*
_class
loc:@SGD/lr*
validate_shape(*
_output_shapes
: 
r
save/RestoreV2_3/tensor_namesConst*!
valueBBSGD/momentum*
dtype0*
_output_shapes
:
j
!save/RestoreV2_3/shape_and_slicesConst*
valueB
B *
dtype0*
_output_shapes
:

save/RestoreV2_3	RestoreV2
save/Constsave/RestoreV2_3/tensor_names!save/RestoreV2_3/shape_and_slices*
_output_shapes
:*
dtypes
2
Ђ
save/Assign_3AssignSGD/momentumsave/RestoreV2_3*
T0*
_class
loc:@SGD/momentum*
validate_shape(*
_output_shapes
: *
use_locking(
q
save/RestoreV2_4/tensor_namesConst*
_output_shapes
:* 
valueBBSGD_1/decay*
dtype0
j
!save/RestoreV2_4/shape_and_slicesConst*
valueB
B *
dtype0*
_output_shapes
:

save/RestoreV2_4	RestoreV2
save/Constsave/RestoreV2_4/tensor_names!save/RestoreV2_4/shape_and_slices*
dtypes
2*
_output_shapes
:
 
save/Assign_4AssignSGD_1/decaysave/RestoreV2_4*
T0*
_class
loc:@SGD_1/decay*
validate_shape(*
_output_shapes
: *
use_locking(
v
save/RestoreV2_5/tensor_namesConst*%
valueBBSGD_1/iterations*
dtype0*
_output_shapes
:
j
!save/RestoreV2_5/shape_and_slicesConst*
valueB
B *
dtype0*
_output_shapes
:

save/RestoreV2_5	RestoreV2
save/Constsave/RestoreV2_5/tensor_names!save/RestoreV2_5/shape_and_slices*
_output_shapes
:*
dtypes
2	
Њ
save/Assign_5AssignSGD_1/iterationssave/RestoreV2_5*
validate_shape(*
_output_shapes
: *
use_locking(*
T0	*#
_class
loc:@SGD_1/iterations
n
save/RestoreV2_6/tensor_namesConst*
valueBBSGD_1/lr*
dtype0*
_output_shapes
:
j
!save/RestoreV2_6/shape_and_slicesConst*
valueB
B *
dtype0*
_output_shapes
:

save/RestoreV2_6	RestoreV2
save/Constsave/RestoreV2_6/tensor_names!save/RestoreV2_6/shape_and_slices*
_output_shapes
:*
dtypes
2

save/Assign_6AssignSGD_1/lrsave/RestoreV2_6*
use_locking(*
T0*
_class
loc:@SGD_1/lr*
validate_shape(*
_output_shapes
: 
t
save/RestoreV2_7/tensor_namesConst*#
valueBBSGD_1/momentum*
dtype0*
_output_shapes
:
j
!save/RestoreV2_7/shape_and_slicesConst*
valueB
B *
dtype0*
_output_shapes
:

save/RestoreV2_7	RestoreV2
save/Constsave/RestoreV2_7/tensor_names!save/RestoreV2_7/shape_and_slices*
dtypes
2*
_output_shapes
:
І
save/Assign_7AssignSGD_1/momentumsave/RestoreV2_7*
T0*!
_class
loc:@SGD_1/momentum*
validate_shape(*
_output_shapes
: *
use_locking(
q
save/RestoreV2_8/tensor_namesConst* 
valueBBSGD_2/decay*
dtype0*
_output_shapes
:
j
!save/RestoreV2_8/shape_and_slicesConst*
valueB
B *
dtype0*
_output_shapes
:

save/RestoreV2_8	RestoreV2
save/Constsave/RestoreV2_8/tensor_names!save/RestoreV2_8/shape_and_slices*
_output_shapes
:*
dtypes
2
 
save/Assign_8AssignSGD_2/decaysave/RestoreV2_8*
use_locking(*
T0*
_class
loc:@SGD_2/decay*
validate_shape(*
_output_shapes
: 
v
save/RestoreV2_9/tensor_namesConst*
_output_shapes
:*%
valueBBSGD_2/iterations*
dtype0
j
!save/RestoreV2_9/shape_and_slicesConst*
valueB
B *
dtype0*
_output_shapes
:

save/RestoreV2_9	RestoreV2
save/Constsave/RestoreV2_9/tensor_names!save/RestoreV2_9/shape_and_slices*
_output_shapes
:*
dtypes
2	
Њ
save/Assign_9AssignSGD_2/iterationssave/RestoreV2_9*
use_locking(*
T0	*#
_class
loc:@SGD_2/iterations*
validate_shape(*
_output_shapes
: 
o
save/RestoreV2_10/tensor_namesConst*
valueBBSGD_2/lr*
dtype0*
_output_shapes
:
k
"save/RestoreV2_10/shape_and_slicesConst*
valueB
B *
dtype0*
_output_shapes
:

save/RestoreV2_10	RestoreV2
save/Constsave/RestoreV2_10/tensor_names"save/RestoreV2_10/shape_and_slices*
dtypes
2*
_output_shapes
:

save/Assign_10AssignSGD_2/lrsave/RestoreV2_10*
_output_shapes
: *
use_locking(*
T0*
_class
loc:@SGD_2/lr*
validate_shape(
u
save/RestoreV2_11/tensor_namesConst*
dtype0*
_output_shapes
:*#
valueBBSGD_2/momentum
k
"save/RestoreV2_11/shape_and_slicesConst*
valueB
B *
dtype0*
_output_shapes
:

save/RestoreV2_11	RestoreV2
save/Constsave/RestoreV2_11/tensor_names"save/RestoreV2_11/shape_and_slices*
_output_shapes
:*
dtypes
2
Ј
save/Assign_11AssignSGD_2/momentumsave/RestoreV2_11*
_output_shapes
: *
use_locking(*
T0*!
_class
loc:@SGD_2/momentum*
validate_shape(
s
save/RestoreV2_12/tensor_namesConst*!
valueBBdense_1/bias*
dtype0*
_output_shapes
:
k
"save/RestoreV2_12/shape_and_slicesConst*
valueB
B *
dtype0*
_output_shapes
:

save/RestoreV2_12	RestoreV2
save/Constsave/RestoreV2_12/tensor_names"save/RestoreV2_12/shape_and_slices*
_output_shapes
:*
dtypes
2
Ј
save/Assign_12Assigndense_1/biassave/RestoreV2_12*
use_locking(*
T0*
_class
loc:@dense_1/bias*
validate_shape(*
_output_shapes
:d
u
save/RestoreV2_13/tensor_namesConst*#
valueBBdense_1/kernel*
dtype0*
_output_shapes
:
k
"save/RestoreV2_13/shape_and_slicesConst*
valueB
B *
dtype0*
_output_shapes
:

save/RestoreV2_13	RestoreV2
save/Constsave/RestoreV2_13/tensor_names"save/RestoreV2_13/shape_and_slices*
_output_shapes
:*
dtypes
2
А
save/Assign_13Assigndense_1/kernelsave/RestoreV2_13*
use_locking(*
T0*!
_class
loc:@dense_1/kernel*
validate_shape(*
_output_shapes

:7d
u
save/RestoreV2_14/tensor_namesConst*#
valueBBdense_1_1/bias*
dtype0*
_output_shapes
:
k
"save/RestoreV2_14/shape_and_slicesConst*
dtype0*
_output_shapes
:*
valueB
B 

save/RestoreV2_14	RestoreV2
save/Constsave/RestoreV2_14/tensor_names"save/RestoreV2_14/shape_and_slices*
_output_shapes
:*
dtypes
2
Ќ
save/Assign_14Assigndense_1_1/biassave/RestoreV2_14*
use_locking(*
T0*!
_class
loc:@dense_1_1/bias*
validate_shape(*
_output_shapes
:d
w
save/RestoreV2_15/tensor_namesConst*
dtype0*
_output_shapes
:*%
valueBBdense_1_1/kernel
k
"save/RestoreV2_15/shape_and_slicesConst*
dtype0*
_output_shapes
:*
valueB
B 

save/RestoreV2_15	RestoreV2
save/Constsave/RestoreV2_15/tensor_names"save/RestoreV2_15/shape_and_slices*
_output_shapes
:*
dtypes
2
Д
save/Assign_15Assigndense_1_1/kernelsave/RestoreV2_15*
_output_shapes

:7d*
use_locking(*
T0*#
_class
loc:@dense_1_1/kernel*
validate_shape(
s
save/RestoreV2_16/tensor_namesConst*!
valueBBdense_2/bias*
dtype0*
_output_shapes
:
k
"save/RestoreV2_16/shape_and_slicesConst*
_output_shapes
:*
valueB
B *
dtype0

save/RestoreV2_16	RestoreV2
save/Constsave/RestoreV2_16/tensor_names"save/RestoreV2_16/shape_and_slices*
_output_shapes
:*
dtypes
2
Ј
save/Assign_16Assigndense_2/biassave/RestoreV2_16*
validate_shape(*
_output_shapes
:F*
use_locking(*
T0*
_class
loc:@dense_2/bias
u
save/RestoreV2_17/tensor_namesConst*
dtype0*
_output_shapes
:*#
valueBBdense_2/kernel
k
"save/RestoreV2_17/shape_and_slicesConst*
dtype0*
_output_shapes
:*
valueB
B 

save/RestoreV2_17	RestoreV2
save/Constsave/RestoreV2_17/tensor_names"save/RestoreV2_17/shape_and_slices*
dtypes
2*
_output_shapes
:
А
save/Assign_17Assigndense_2/kernelsave/RestoreV2_17*
use_locking(*
T0*!
_class
loc:@dense_2/kernel*
validate_shape(*
_output_shapes

:dF
u
save/RestoreV2_18/tensor_namesConst*#
valueBBdense_2_1/bias*
dtype0*
_output_shapes
:
k
"save/RestoreV2_18/shape_and_slicesConst*
valueB
B *
dtype0*
_output_shapes
:

save/RestoreV2_18	RestoreV2
save/Constsave/RestoreV2_18/tensor_names"save/RestoreV2_18/shape_and_slices*
_output_shapes
:*
dtypes
2
Ќ
save/Assign_18Assigndense_2_1/biassave/RestoreV2_18*
use_locking(*
T0*!
_class
loc:@dense_2_1/bias*
validate_shape(*
_output_shapes
:F
w
save/RestoreV2_19/tensor_namesConst*%
valueBBdense_2_1/kernel*
dtype0*
_output_shapes
:
k
"save/RestoreV2_19/shape_and_slicesConst*
valueB
B *
dtype0*
_output_shapes
:

save/RestoreV2_19	RestoreV2
save/Constsave/RestoreV2_19/tensor_names"save/RestoreV2_19/shape_and_slices*
dtypes
2*
_output_shapes
:
Д
save/Assign_19Assigndense_2_1/kernelsave/RestoreV2_19*#
_class
loc:@dense_2_1/kernel*
validate_shape(*
_output_shapes

:dF*
use_locking(*
T0
s
save/RestoreV2_20/tensor_namesConst*!
valueBBdense_3/bias*
dtype0*
_output_shapes
:
k
"save/RestoreV2_20/shape_and_slicesConst*
valueB
B *
dtype0*
_output_shapes
:

save/RestoreV2_20	RestoreV2
save/Constsave/RestoreV2_20/tensor_names"save/RestoreV2_20/shape_and_slices*
_output_shapes
:*
dtypes
2
Ј
save/Assign_20Assigndense_3/biassave/RestoreV2_20*
T0*
_class
loc:@dense_3/bias*
validate_shape(*
_output_shapes
:2*
use_locking(
u
save/RestoreV2_21/tensor_namesConst*
_output_shapes
:*#
valueBBdense_3/kernel*
dtype0
k
"save/RestoreV2_21/shape_and_slicesConst*
_output_shapes
:*
valueB
B *
dtype0

save/RestoreV2_21	RestoreV2
save/Constsave/RestoreV2_21/tensor_names"save/RestoreV2_21/shape_and_slices*
dtypes
2*
_output_shapes
:
А
save/Assign_21Assigndense_3/kernelsave/RestoreV2_21*
T0*!
_class
loc:@dense_3/kernel*
validate_shape(*
_output_shapes

:F2*
use_locking(
u
save/RestoreV2_22/tensor_namesConst*#
valueBBdense_3_1/bias*
dtype0*
_output_shapes
:
k
"save/RestoreV2_22/shape_and_slicesConst*
dtype0*
_output_shapes
:*
valueB
B 

save/RestoreV2_22	RestoreV2
save/Constsave/RestoreV2_22/tensor_names"save/RestoreV2_22/shape_and_slices*
_output_shapes
:*
dtypes
2
Ќ
save/Assign_22Assigndense_3_1/biassave/RestoreV2_22*
validate_shape(*
_output_shapes
:2*
use_locking(*
T0*!
_class
loc:@dense_3_1/bias
w
save/RestoreV2_23/tensor_namesConst*%
valueBBdense_3_1/kernel*
dtype0*
_output_shapes
:
k
"save/RestoreV2_23/shape_and_slicesConst*
valueB
B *
dtype0*
_output_shapes
:

save/RestoreV2_23	RestoreV2
save/Constsave/RestoreV2_23/tensor_names"save/RestoreV2_23/shape_and_slices*
_output_shapes
:*
dtypes
2
Д
save/Assign_23Assigndense_3_1/kernelsave/RestoreV2_23*
use_locking(*
T0*#
_class
loc:@dense_3_1/kernel*
validate_shape(*
_output_shapes

:F2
s
save/RestoreV2_24/tensor_namesConst*!
valueBBdense_4/bias*
dtype0*
_output_shapes
:
k
"save/RestoreV2_24/shape_and_slicesConst*
_output_shapes
:*
valueB
B *
dtype0

save/RestoreV2_24	RestoreV2
save/Constsave/RestoreV2_24/tensor_names"save/RestoreV2_24/shape_and_slices*
_output_shapes
:*
dtypes
2
Ј
save/Assign_24Assigndense_4/biassave/RestoreV2_24*
use_locking(*
T0*
_class
loc:@dense_4/bias*
validate_shape(*
_output_shapes
:
u
save/RestoreV2_25/tensor_namesConst*
_output_shapes
:*#
valueBBdense_4/kernel*
dtype0
k
"save/RestoreV2_25/shape_and_slicesConst*
valueB
B *
dtype0*
_output_shapes
:

save/RestoreV2_25	RestoreV2
save/Constsave/RestoreV2_25/tensor_names"save/RestoreV2_25/shape_and_slices*
_output_shapes
:*
dtypes
2
А
save/Assign_25Assigndense_4/kernelsave/RestoreV2_25*
validate_shape(*
_output_shapes

:2*
use_locking(*
T0*!
_class
loc:@dense_4/kernel
u
save/RestoreV2_26/tensor_namesConst*
_output_shapes
:*#
valueBBdense_4_1/bias*
dtype0
k
"save/RestoreV2_26/shape_and_slicesConst*
dtype0*
_output_shapes
:*
valueB
B 

save/RestoreV2_26	RestoreV2
save/Constsave/RestoreV2_26/tensor_names"save/RestoreV2_26/shape_and_slices*
_output_shapes
:*
dtypes
2
Ќ
save/Assign_26Assigndense_4_1/biassave/RestoreV2_26*
_output_shapes
:*
use_locking(*
T0*!
_class
loc:@dense_4_1/bias*
validate_shape(
w
save/RestoreV2_27/tensor_namesConst*%
valueBBdense_4_1/kernel*
dtype0*
_output_shapes
:
k
"save/RestoreV2_27/shape_and_slicesConst*
_output_shapes
:*
valueB
B *
dtype0

save/RestoreV2_27	RestoreV2
save/Constsave/RestoreV2_27/tensor_names"save/RestoreV2_27/shape_and_slices*
_output_shapes
:*
dtypes
2
Д
save/Assign_27Assigndense_4_1/kernelsave/RestoreV2_27*
use_locking(*
T0*#
_class
loc:@dense_4_1/kernel*
validate_shape(*
_output_shapes

:2
s
save/RestoreV2_28/tensor_namesConst*!
valueBBdense_5/bias*
dtype0*
_output_shapes
:
k
"save/RestoreV2_28/shape_and_slicesConst*
valueB
B *
dtype0*
_output_shapes
:

save/RestoreV2_28	RestoreV2
save/Constsave/RestoreV2_28/tensor_names"save/RestoreV2_28/shape_and_slices*
dtypes
2*
_output_shapes
:
Ј
save/Assign_28Assigndense_5/biassave/RestoreV2_28*
validate_shape(*
_output_shapes
:*
use_locking(*
T0*
_class
loc:@dense_5/bias
u
save/RestoreV2_29/tensor_namesConst*#
valueBBdense_5/kernel*
dtype0*
_output_shapes
:
k
"save/RestoreV2_29/shape_and_slicesConst*
valueB
B *
dtype0*
_output_shapes
:

save/RestoreV2_29	RestoreV2
save/Constsave/RestoreV2_29/tensor_names"save/RestoreV2_29/shape_and_slices*
_output_shapes
:*
dtypes
2
А
save/Assign_29Assigndense_5/kernelsave/RestoreV2_29*
use_locking(*
T0*!
_class
loc:@dense_5/kernel*
validate_shape(*
_output_shapes

:
u
save/RestoreV2_30/tensor_namesConst*#
valueBBdense_5_1/bias*
dtype0*
_output_shapes
:
k
"save/RestoreV2_30/shape_and_slicesConst*
valueB
B *
dtype0*
_output_shapes
:

save/RestoreV2_30	RestoreV2
save/Constsave/RestoreV2_30/tensor_names"save/RestoreV2_30/shape_and_slices*
_output_shapes
:*
dtypes
2
Ќ
save/Assign_30Assigndense_5_1/biassave/RestoreV2_30*
use_locking(*
T0*!
_class
loc:@dense_5_1/bias*
validate_shape(*
_output_shapes
:
w
save/RestoreV2_31/tensor_namesConst*%
valueBBdense_5_1/kernel*
dtype0*
_output_shapes
:
k
"save/RestoreV2_31/shape_and_slicesConst*
valueB
B *
dtype0*
_output_shapes
:

save/RestoreV2_31	RestoreV2
save/Constsave/RestoreV2_31/tensor_names"save/RestoreV2_31/shape_and_slices*
_output_shapes
:*
dtypes
2
Д
save/Assign_31Assigndense_5_1/kernelsave/RestoreV2_31*
use_locking(*
T0*#
_class
loc:@dense_5_1/kernel*
validate_shape(*
_output_shapes

:
|
save/RestoreV2_32/tensor_namesConst**
value!BBtraining/SGD/Variable*
dtype0*
_output_shapes
:
k
"save/RestoreV2_32/shape_and_slicesConst*
valueB
B *
dtype0*
_output_shapes
:

save/RestoreV2_32	RestoreV2
save/Constsave/RestoreV2_32/tensor_names"save/RestoreV2_32/shape_and_slices*
_output_shapes
:*
dtypes
2
О
save/Assign_32Assigntraining/SGD/Variablesave/RestoreV2_32*
use_locking(*
T0*(
_class
loc:@training/SGD/Variable*
validate_shape(*
_output_shapes

:7d
~
save/RestoreV2_33/tensor_namesConst*,
value#B!Btraining/SGD/Variable_1*
dtype0*
_output_shapes
:
k
"save/RestoreV2_33/shape_and_slicesConst*
valueB
B *
dtype0*
_output_shapes
:

save/RestoreV2_33	RestoreV2
save/Constsave/RestoreV2_33/tensor_names"save/RestoreV2_33/shape_and_slices*
_output_shapes
:*
dtypes
2
О
save/Assign_33Assigntraining/SGD/Variable_1save/RestoreV2_33*
use_locking(*
T0**
_class 
loc:@training/SGD/Variable_1*
validate_shape(*
_output_shapes
:d
~
save/RestoreV2_34/tensor_namesConst*,
value#B!Btraining/SGD/Variable_2*
dtype0*
_output_shapes
:
k
"save/RestoreV2_34/shape_and_slicesConst*
_output_shapes
:*
valueB
B *
dtype0

save/RestoreV2_34	RestoreV2
save/Constsave/RestoreV2_34/tensor_names"save/RestoreV2_34/shape_and_slices*
dtypes
2*
_output_shapes
:
Т
save/Assign_34Assigntraining/SGD/Variable_2save/RestoreV2_34**
_class 
loc:@training/SGD/Variable_2*
validate_shape(*
_output_shapes

:dF*
use_locking(*
T0
~
save/RestoreV2_35/tensor_namesConst*
_output_shapes
:*,
value#B!Btraining/SGD/Variable_3*
dtype0
k
"save/RestoreV2_35/shape_and_slicesConst*
valueB
B *
dtype0*
_output_shapes
:

save/RestoreV2_35	RestoreV2
save/Constsave/RestoreV2_35/tensor_names"save/RestoreV2_35/shape_and_slices*
_output_shapes
:*
dtypes
2
О
save/Assign_35Assigntraining/SGD/Variable_3save/RestoreV2_35*
validate_shape(*
_output_shapes
:F*
use_locking(*
T0**
_class 
loc:@training/SGD/Variable_3
~
save/RestoreV2_36/tensor_namesConst*,
value#B!Btraining/SGD/Variable_4*
dtype0*
_output_shapes
:
k
"save/RestoreV2_36/shape_and_slicesConst*
valueB
B *
dtype0*
_output_shapes
:

save/RestoreV2_36	RestoreV2
save/Constsave/RestoreV2_36/tensor_names"save/RestoreV2_36/shape_and_slices*
dtypes
2*
_output_shapes
:
Т
save/Assign_36Assigntraining/SGD/Variable_4save/RestoreV2_36*
use_locking(*
T0**
_class 
loc:@training/SGD/Variable_4*
validate_shape(*
_output_shapes

:F2
~
save/RestoreV2_37/tensor_namesConst*,
value#B!Btraining/SGD/Variable_5*
dtype0*
_output_shapes
:
k
"save/RestoreV2_37/shape_and_slicesConst*
valueB
B *
dtype0*
_output_shapes
:

save/RestoreV2_37	RestoreV2
save/Constsave/RestoreV2_37/tensor_names"save/RestoreV2_37/shape_and_slices*
_output_shapes
:*
dtypes
2
О
save/Assign_37Assigntraining/SGD/Variable_5save/RestoreV2_37*
use_locking(*
T0**
_class 
loc:@training/SGD/Variable_5*
validate_shape(*
_output_shapes
:2
~
save/RestoreV2_38/tensor_namesConst*
dtype0*
_output_shapes
:*,
value#B!Btraining/SGD/Variable_6
k
"save/RestoreV2_38/shape_and_slicesConst*
valueB
B *
dtype0*
_output_shapes
:

save/RestoreV2_38	RestoreV2
save/Constsave/RestoreV2_38/tensor_names"save/RestoreV2_38/shape_and_slices*
dtypes
2*
_output_shapes
:
Т
save/Assign_38Assigntraining/SGD/Variable_6save/RestoreV2_38*
validate_shape(*
_output_shapes

:2*
use_locking(*
T0**
_class 
loc:@training/SGD/Variable_6
~
save/RestoreV2_39/tensor_namesConst*,
value#B!Btraining/SGD/Variable_7*
dtype0*
_output_shapes
:
k
"save/RestoreV2_39/shape_and_slicesConst*
valueB
B *
dtype0*
_output_shapes
:

save/RestoreV2_39	RestoreV2
save/Constsave/RestoreV2_39/tensor_names"save/RestoreV2_39/shape_and_slices*
_output_shapes
:*
dtypes
2
О
save/Assign_39Assigntraining/SGD/Variable_7save/RestoreV2_39*
T0**
_class 
loc:@training/SGD/Variable_7*
validate_shape(*
_output_shapes
:*
use_locking(
~
save/RestoreV2_40/tensor_namesConst*,
value#B!Btraining/SGD/Variable_8*
dtype0*
_output_shapes
:
k
"save/RestoreV2_40/shape_and_slicesConst*
_output_shapes
:*
valueB
B *
dtype0

save/RestoreV2_40	RestoreV2
save/Constsave/RestoreV2_40/tensor_names"save/RestoreV2_40/shape_and_slices*
_output_shapes
:*
dtypes
2
Т
save/Assign_40Assigntraining/SGD/Variable_8save/RestoreV2_40*
T0**
_class 
loc:@training/SGD/Variable_8*
validate_shape(*
_output_shapes

:*
use_locking(
~
save/RestoreV2_41/tensor_namesConst*,
value#B!Btraining/SGD/Variable_9*
dtype0*
_output_shapes
:
k
"save/RestoreV2_41/shape_and_slicesConst*
valueB
B *
dtype0*
_output_shapes
:

save/RestoreV2_41	RestoreV2
save/Constsave/RestoreV2_41/tensor_names"save/RestoreV2_41/shape_and_slices*
_output_shapes
:*
dtypes
2
О
save/Assign_41Assigntraining/SGD/Variable_9save/RestoreV2_41*
use_locking(*
T0**
_class 
loc:@training/SGD/Variable_9*
validate_shape(*
_output_shapes
:
~
save/RestoreV2_42/tensor_namesConst*,
value#B!Btraining_1/SGD/Variable*
dtype0*
_output_shapes
:
k
"save/RestoreV2_42/shape_and_slicesConst*
valueB
B *
dtype0*
_output_shapes
:

save/RestoreV2_42	RestoreV2
save/Constsave/RestoreV2_42/tensor_names"save/RestoreV2_42/shape_and_slices*
dtypes
2*
_output_shapes
:
Т
save/Assign_42Assigntraining_1/SGD/Variablesave/RestoreV2_42*
use_locking(*
T0**
_class 
loc:@training_1/SGD/Variable*
validate_shape(*
_output_shapes

:7d

save/RestoreV2_43/tensor_namesConst*.
value%B#Btraining_1/SGD/Variable_1*
dtype0*
_output_shapes
:
k
"save/RestoreV2_43/shape_and_slicesConst*
valueB
B *
dtype0*
_output_shapes
:

save/RestoreV2_43	RestoreV2
save/Constsave/RestoreV2_43/tensor_names"save/RestoreV2_43/shape_and_slices*
_output_shapes
:*
dtypes
2
Т
save/Assign_43Assigntraining_1/SGD/Variable_1save/RestoreV2_43*,
_class"
 loc:@training_1/SGD/Variable_1*
validate_shape(*
_output_shapes
:d*
use_locking(*
T0

save/RestoreV2_44/tensor_namesConst*.
value%B#Btraining_1/SGD/Variable_2*
dtype0*
_output_shapes
:
k
"save/RestoreV2_44/shape_and_slicesConst*
valueB
B *
dtype0*
_output_shapes
:

save/RestoreV2_44	RestoreV2
save/Constsave/RestoreV2_44/tensor_names"save/RestoreV2_44/shape_and_slices*
_output_shapes
:*
dtypes
2
Ц
save/Assign_44Assigntraining_1/SGD/Variable_2save/RestoreV2_44*
_output_shapes

:dF*
use_locking(*
T0*,
_class"
 loc:@training_1/SGD/Variable_2*
validate_shape(

save/RestoreV2_45/tensor_namesConst*.
value%B#Btraining_1/SGD/Variable_3*
dtype0*
_output_shapes
:
k
"save/RestoreV2_45/shape_and_slicesConst*
valueB
B *
dtype0*
_output_shapes
:

save/RestoreV2_45	RestoreV2
save/Constsave/RestoreV2_45/tensor_names"save/RestoreV2_45/shape_and_slices*
_output_shapes
:*
dtypes
2
Т
save/Assign_45Assigntraining_1/SGD/Variable_3save/RestoreV2_45*
_output_shapes
:F*
use_locking(*
T0*,
_class"
 loc:@training_1/SGD/Variable_3*
validate_shape(

save/RestoreV2_46/tensor_namesConst*.
value%B#Btraining_1/SGD/Variable_4*
dtype0*
_output_shapes
:
k
"save/RestoreV2_46/shape_and_slicesConst*
dtype0*
_output_shapes
:*
valueB
B 

save/RestoreV2_46	RestoreV2
save/Constsave/RestoreV2_46/tensor_names"save/RestoreV2_46/shape_and_slices*
_output_shapes
:*
dtypes
2
Ц
save/Assign_46Assigntraining_1/SGD/Variable_4save/RestoreV2_46*,
_class"
 loc:@training_1/SGD/Variable_4*
validate_shape(*
_output_shapes

:F2*
use_locking(*
T0

save/RestoreV2_47/tensor_namesConst*.
value%B#Btraining_1/SGD/Variable_5*
dtype0*
_output_shapes
:
k
"save/RestoreV2_47/shape_and_slicesConst*
dtype0*
_output_shapes
:*
valueB
B 

save/RestoreV2_47	RestoreV2
save/Constsave/RestoreV2_47/tensor_names"save/RestoreV2_47/shape_and_slices*
_output_shapes
:*
dtypes
2
Т
save/Assign_47Assigntraining_1/SGD/Variable_5save/RestoreV2_47*
use_locking(*
T0*,
_class"
 loc:@training_1/SGD/Variable_5*
validate_shape(*
_output_shapes
:2

save/RestoreV2_48/tensor_namesConst*
_output_shapes
:*.
value%B#Btraining_1/SGD/Variable_6*
dtype0
k
"save/RestoreV2_48/shape_and_slicesConst*
valueB
B *
dtype0*
_output_shapes
:

save/RestoreV2_48	RestoreV2
save/Constsave/RestoreV2_48/tensor_names"save/RestoreV2_48/shape_and_slices*
dtypes
2*
_output_shapes
:
Ц
save/Assign_48Assigntraining_1/SGD/Variable_6save/RestoreV2_48*
_output_shapes

:2*
use_locking(*
T0*,
_class"
 loc:@training_1/SGD/Variable_6*
validate_shape(

save/RestoreV2_49/tensor_namesConst*.
value%B#Btraining_1/SGD/Variable_7*
dtype0*
_output_shapes
:
k
"save/RestoreV2_49/shape_and_slicesConst*
valueB
B *
dtype0*
_output_shapes
:

save/RestoreV2_49	RestoreV2
save/Constsave/RestoreV2_49/tensor_names"save/RestoreV2_49/shape_and_slices*
_output_shapes
:*
dtypes
2
Т
save/Assign_49Assigntraining_1/SGD/Variable_7save/RestoreV2_49*
use_locking(*
T0*,
_class"
 loc:@training_1/SGD/Variable_7*
validate_shape(*
_output_shapes
:

save/RestoreV2_50/tensor_namesConst*
_output_shapes
:*.
value%B#Btraining_1/SGD/Variable_8*
dtype0
k
"save/RestoreV2_50/shape_and_slicesConst*
valueB
B *
dtype0*
_output_shapes
:

save/RestoreV2_50	RestoreV2
save/Constsave/RestoreV2_50/tensor_names"save/RestoreV2_50/shape_and_slices*
dtypes
2*
_output_shapes
:
Ц
save/Assign_50Assigntraining_1/SGD/Variable_8save/RestoreV2_50*
T0*,
_class"
 loc:@training_1/SGD/Variable_8*
validate_shape(*
_output_shapes

:*
use_locking(

save/RestoreV2_51/tensor_namesConst*.
value%B#Btraining_1/SGD/Variable_9*
dtype0*
_output_shapes
:
k
"save/RestoreV2_51/shape_and_slicesConst*
valueB
B *
dtype0*
_output_shapes
:

save/RestoreV2_51	RestoreV2
save/Constsave/RestoreV2_51/tensor_names"save/RestoreV2_51/shape_and_slices*
_output_shapes
:*
dtypes
2
Т
save/Assign_51Assigntraining_1/SGD/Variable_9save/RestoreV2_51*
use_locking(*
T0*,
_class"
 loc:@training_1/SGD/Variable_9*
validate_shape(*
_output_shapes
:

save/restore_shardNoOp^save/Assign^save/Assign_1^save/Assign_2^save/Assign_3^save/Assign_4^save/Assign_5^save/Assign_6^save/Assign_7^save/Assign_8^save/Assign_9^save/Assign_10^save/Assign_11^save/Assign_12^save/Assign_13^save/Assign_14^save/Assign_15^save/Assign_16^save/Assign_17^save/Assign_18^save/Assign_19^save/Assign_20^save/Assign_21^save/Assign_22^save/Assign_23^save/Assign_24^save/Assign_25^save/Assign_26^save/Assign_27^save/Assign_28^save/Assign_29^save/Assign_30^save/Assign_31^save/Assign_32^save/Assign_33^save/Assign_34^save/Assign_35^save/Assign_36^save/Assign_37^save/Assign_38^save/Assign_39^save/Assign_40^save/Assign_41^save/Assign_42^save/Assign_43^save/Assign_44^save/Assign_45^save/Assign_46^save/Assign_47^save/Assign_48^save/Assign_49^save/Assign_50^save/Assign_51
-
save/restore_allNoOp^save/restore_shard"<
save/Const:0save/Identity:0save/restore_all (5 @F8"ј
trainable_variablesрн
@
dense_1/kernel:0dense_1/kernel/Assigndense_1/kernel/read:0
:
dense_1/bias:0dense_1/bias/Assigndense_1/bias/read:0
@
dense_2/kernel:0dense_2/kernel/Assigndense_2/kernel/read:0
:
dense_2/bias:0dense_2/bias/Assigndense_2/bias/read:0
@
dense_3/kernel:0dense_3/kernel/Assigndense_3/kernel/read:0
:
dense_3/bias:0dense_3/bias/Assigndense_3/bias/read:0
@
dense_4/kernel:0dense_4/kernel/Assigndense_4/kernel/read:0
:
dense_4/bias:0dense_4/bias/Assigndense_4/bias/read:0
@
dense_5/kernel:0dense_5/kernel/Assigndense_5/kernel/read:0
:
dense_5/bias:0dense_5/bias/Assigndense_5/bias/read:0
@
SGD/iterations:0SGD/iterations/AssignSGD/iterations/read:0
(
SGD/lr:0SGD/lr/AssignSGD/lr/read:0
:
SGD/momentum:0SGD/momentum/AssignSGD/momentum/read:0
1
SGD/decay:0SGD/decay/AssignSGD/decay/read:0
U
training/SGD/Variable:0training/SGD/Variable/Assigntraining/SGD/Variable/read:0
[
training/SGD/Variable_1:0training/SGD/Variable_1/Assigntraining/SGD/Variable_1/read:0
[
training/SGD/Variable_2:0training/SGD/Variable_2/Assigntraining/SGD/Variable_2/read:0
[
training/SGD/Variable_3:0training/SGD/Variable_3/Assigntraining/SGD/Variable_3/read:0
[
training/SGD/Variable_4:0training/SGD/Variable_4/Assigntraining/SGD/Variable_4/read:0
[
training/SGD/Variable_5:0training/SGD/Variable_5/Assigntraining/SGD/Variable_5/read:0
[
training/SGD/Variable_6:0training/SGD/Variable_6/Assigntraining/SGD/Variable_6/read:0
[
training/SGD/Variable_7:0training/SGD/Variable_7/Assigntraining/SGD/Variable_7/read:0
[
training/SGD/Variable_8:0training/SGD/Variable_8/Assigntraining/SGD/Variable_8/read:0
[
training/SGD/Variable_9:0training/SGD/Variable_9/Assigntraining/SGD/Variable_9/read:0
F
dense_1_1/kernel:0dense_1_1/kernel/Assigndense_1_1/kernel/read:0
@
dense_1_1/bias:0dense_1_1/bias/Assigndense_1_1/bias/read:0
F
dense_2_1/kernel:0dense_2_1/kernel/Assigndense_2_1/kernel/read:0
@
dense_2_1/bias:0dense_2_1/bias/Assigndense_2_1/bias/read:0
F
dense_3_1/kernel:0dense_3_1/kernel/Assigndense_3_1/kernel/read:0
@
dense_3_1/bias:0dense_3_1/bias/Assigndense_3_1/bias/read:0
F
dense_4_1/kernel:0dense_4_1/kernel/Assigndense_4_1/kernel/read:0
@
dense_4_1/bias:0dense_4_1/bias/Assigndense_4_1/bias/read:0
F
dense_5_1/kernel:0dense_5_1/kernel/Assigndense_5_1/kernel/read:0
@
dense_5_1/bias:0dense_5_1/bias/Assigndense_5_1/bias/read:0
F
SGD_1/iterations:0SGD_1/iterations/AssignSGD_1/iterations/read:0
.

SGD_1/lr:0SGD_1/lr/AssignSGD_1/lr/read:0
@
SGD_1/momentum:0SGD_1/momentum/AssignSGD_1/momentum/read:0
7
SGD_1/decay:0SGD_1/decay/AssignSGD_1/decay/read:0
[
training_1/SGD/Variable:0training_1/SGD/Variable/Assigntraining_1/SGD/Variable/read:0
a
training_1/SGD/Variable_1:0 training_1/SGD/Variable_1/Assign training_1/SGD/Variable_1/read:0
a
training_1/SGD/Variable_2:0 training_1/SGD/Variable_2/Assign training_1/SGD/Variable_2/read:0
a
training_1/SGD/Variable_3:0 training_1/SGD/Variable_3/Assign training_1/SGD/Variable_3/read:0
a
training_1/SGD/Variable_4:0 training_1/SGD/Variable_4/Assign training_1/SGD/Variable_4/read:0
a
training_1/SGD/Variable_5:0 training_1/SGD/Variable_5/Assign training_1/SGD/Variable_5/read:0
a
training_1/SGD/Variable_6:0 training_1/SGD/Variable_6/Assign training_1/SGD/Variable_6/read:0
a
training_1/SGD/Variable_7:0 training_1/SGD/Variable_7/Assign training_1/SGD/Variable_7/read:0
a
training_1/SGD/Variable_8:0 training_1/SGD/Variable_8/Assign training_1/SGD/Variable_8/read:0
a
training_1/SGD/Variable_9:0 training_1/SGD/Variable_9/Assign training_1/SGD/Variable_9/read:0
F
SGD_2/iterations:0SGD_2/iterations/AssignSGD_2/iterations/read:0
.

SGD_2/lr:0SGD_2/lr/AssignSGD_2/lr/read:0
@
SGD_2/momentum:0SGD_2/momentum/AssignSGD_2/momentum/read:0
7
SGD_2/decay:0SGD_2/decay/AssignSGD_2/decay/read:0"ю
	variablesрн
@
dense_1/kernel:0dense_1/kernel/Assigndense_1/kernel/read:0
:
dense_1/bias:0dense_1/bias/Assigndense_1/bias/read:0
@
dense_2/kernel:0dense_2/kernel/Assigndense_2/kernel/read:0
:
dense_2/bias:0dense_2/bias/Assigndense_2/bias/read:0
@
dense_3/kernel:0dense_3/kernel/Assigndense_3/kernel/read:0
:
dense_3/bias:0dense_3/bias/Assigndense_3/bias/read:0
@
dense_4/kernel:0dense_4/kernel/Assigndense_4/kernel/read:0
:
dense_4/bias:0dense_4/bias/Assigndense_4/bias/read:0
@
dense_5/kernel:0dense_5/kernel/Assigndense_5/kernel/read:0
:
dense_5/bias:0dense_5/bias/Assigndense_5/bias/read:0
@
SGD/iterations:0SGD/iterations/AssignSGD/iterations/read:0
(
SGD/lr:0SGD/lr/AssignSGD/lr/read:0
:
SGD/momentum:0SGD/momentum/AssignSGD/momentum/read:0
1
SGD/decay:0SGD/decay/AssignSGD/decay/read:0
U
training/SGD/Variable:0training/SGD/Variable/Assigntraining/SGD/Variable/read:0
[
training/SGD/Variable_1:0training/SGD/Variable_1/Assigntraining/SGD/Variable_1/read:0
[
training/SGD/Variable_2:0training/SGD/Variable_2/Assigntraining/SGD/Variable_2/read:0
[
training/SGD/Variable_3:0training/SGD/Variable_3/Assigntraining/SGD/Variable_3/read:0
[
training/SGD/Variable_4:0training/SGD/Variable_4/Assigntraining/SGD/Variable_4/read:0
[
training/SGD/Variable_5:0training/SGD/Variable_5/Assigntraining/SGD/Variable_5/read:0
[
training/SGD/Variable_6:0training/SGD/Variable_6/Assigntraining/SGD/Variable_6/read:0
[
training/SGD/Variable_7:0training/SGD/Variable_7/Assigntraining/SGD/Variable_7/read:0
[
training/SGD/Variable_8:0training/SGD/Variable_8/Assigntraining/SGD/Variable_8/read:0
[
training/SGD/Variable_9:0training/SGD/Variable_9/Assigntraining/SGD/Variable_9/read:0
F
dense_1_1/kernel:0dense_1_1/kernel/Assigndense_1_1/kernel/read:0
@
dense_1_1/bias:0dense_1_1/bias/Assigndense_1_1/bias/read:0
F
dense_2_1/kernel:0dense_2_1/kernel/Assigndense_2_1/kernel/read:0
@
dense_2_1/bias:0dense_2_1/bias/Assigndense_2_1/bias/read:0
F
dense_3_1/kernel:0dense_3_1/kernel/Assigndense_3_1/kernel/read:0
@
dense_3_1/bias:0dense_3_1/bias/Assigndense_3_1/bias/read:0
F
dense_4_1/kernel:0dense_4_1/kernel/Assigndense_4_1/kernel/read:0
@
dense_4_1/bias:0dense_4_1/bias/Assigndense_4_1/bias/read:0
F
dense_5_1/kernel:0dense_5_1/kernel/Assigndense_5_1/kernel/read:0
@
dense_5_1/bias:0dense_5_1/bias/Assigndense_5_1/bias/read:0
F
SGD_1/iterations:0SGD_1/iterations/AssignSGD_1/iterations/read:0
.

SGD_1/lr:0SGD_1/lr/AssignSGD_1/lr/read:0
@
SGD_1/momentum:0SGD_1/momentum/AssignSGD_1/momentum/read:0
7
SGD_1/decay:0SGD_1/decay/AssignSGD_1/decay/read:0
[
training_1/SGD/Variable:0training_1/SGD/Variable/Assigntraining_1/SGD/Variable/read:0
a
training_1/SGD/Variable_1:0 training_1/SGD/Variable_1/Assign training_1/SGD/Variable_1/read:0
a
training_1/SGD/Variable_2:0 training_1/SGD/Variable_2/Assign training_1/SGD/Variable_2/read:0
a
training_1/SGD/Variable_3:0 training_1/SGD/Variable_3/Assign training_1/SGD/Variable_3/read:0
a
training_1/SGD/Variable_4:0 training_1/SGD/Variable_4/Assign training_1/SGD/Variable_4/read:0
a
training_1/SGD/Variable_5:0 training_1/SGD/Variable_5/Assign training_1/SGD/Variable_5/read:0
a
training_1/SGD/Variable_6:0 training_1/SGD/Variable_6/Assign training_1/SGD/Variable_6/read:0
a
training_1/SGD/Variable_7:0 training_1/SGD/Variable_7/Assign training_1/SGD/Variable_7/read:0
a
training_1/SGD/Variable_8:0 training_1/SGD/Variable_8/Assign training_1/SGD/Variable_8/read:0
a
training_1/SGD/Variable_9:0 training_1/SGD/Variable_9/Assign training_1/SGD/Variable_9/read:0
F
SGD_2/iterations:0SGD_2/iterations/AssignSGD_2/iterations/read:0
.

SGD_2/lr:0SGD_2/lr/AssignSGD_2/lr/read:0
@
SGD_2/momentum:0SGD_2/momentum/AssignSGD_2/momentum/read:0
7
SGD_2/decay:0SGD_2/decay/AssignSGD_2/decay/read:0*
serving_default
/
input&
dense_1_input:0џџџџџџџџџ72
income(
dense_5/Sigmoid:0џџџџџџџџџtensorflow/serving/predict