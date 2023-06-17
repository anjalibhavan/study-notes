# Linear Algebra

Created: July 29, 2021 12:27 AM

## Important definitions

- What is vector space?
    
    A vector space is a set such that the following properties hold on it: additive/multiplicative identity, commutativity, closure, distributive, associativity, additive inverse.
    
- What is matrix multiplication?
    
    In which  $c_{ij} = a_{il}b_{lj}$ 
    
- What is Hadamard multiplication?
    
    Also called element-wise multiplication. In which  $c_{ij} = a_{ij}b_{ij}$
    
- What is span?
    
    The set of all linear combinations of a vector space $V$.
    
- What is basis?
    
    A set of linearly independent vectors in a vector space $V$that span $V$.
    
- What is dimension?
    
    The dimension of a vector space is the length of any basis of the space.
    
- What is subspace?
    
    A subset  $U$  of a vector space  $V$  is a subspace if  $U \in V$ To check if a space is subspace of another, it must be closed under vector addition and scalar multiplication, and must include 0.
    
- What is linear map?
    
    A linear map from $V$ to $W$ is a function $T: V \to W$ with additivity (like vector addition) and homogeneity (like scalar multiplication) properties.
    
- What is null space?
    
    Null space of a linear map $T = \{v \in V : Tv = 0 \}$
    
- What is invariant subspace?
    
    A subspace $U$ is invariant under a linear transformation $T$ if $u \in U \implies Tu \in U$. 
    
- What is outer product?
    
    It's the fucking cross product. The outer product u ⊗ v is equivalent to a matrix multiplication $UV^T$ ,  provided that u is represented as a m × 1 column vector and v as a n × 1 column vector (which makes v^T  a row vector)
    
- What is convex function?
    
    Convexity is a term that pertains to both sets and functions. For functions, there are different
    degrees of convexity, and how convex a function is tells us a lot about its minima: do they exist, are they unique, how quickly can we find them using optimization algorithms, etc.
    A set X is convex if tx + (1 - t)y $\in$ X for all x and y $\in$ X  and all t $\in$ [0, 1].
    
- What is inverse of a matrix?
    
    A square matrix A is called invertible if there is a square matrix B of the same size such that AB = BA = I, and we call B an inverse of A.
    
- What is eigendecomposition?
    
    It is a decomposition of a matrix given by $A = PDP^{-1}$. P is the matrix comprising of all eigenvectors of A, and D is a diagonal matrix comprising of all eigenvalues of A. The fact that this decomposition is always possible for a square matrix A as long as P is a square matrix is known in this work as the eigen decomposition theorem.
    
- What is SVD?
    
    Stands for Singular Value Decomposition. Given by $A = U\Sigma V^{T}$. Instead of transpose it is conjugate but for real values both are same. The inverse calculated using this is given by $A^{-1} = V\Sigma ^{-1} U^{T}$ is called the **pseudoinverse*,*** and generalizes inverses to non square matrices. Used in PCA.
    
- What is orthonormal vectors?
    
    A set of vectors S is orthonormal if every vector in S has magnitude 1 and the set of vectors are mutually orthogonal.
    

## Geometric interpretations

- Of determinant?
    
    A determinant can be geometrically seen as how much the area changes due to a transformation given by that matrix.
    
- Of a matrix?
    
    A matrix can be interpreted as a transformation. Its columns are where the unit vectors would land. So multiplying A by B means applying transformation A on B, such that the result is where B would land under the new coordinates specified by A's columns.
    
- Of dot product?
    
    Geometrically dot product can be seen as projecting one vector on the other and multiplying their lengths.
    
- Of cross product?
- Of non-square matrices?
    
    Non-square matrices can be seen as transformation between dimensions - a 3x2 matrix means that 2 dimensional unit vectors are being transformed into 3 dimensional space, coordinates given by each column.
    
- Of eigenvectors?
    
    Almost all vectors change direction, when they are multiplied by a matrix. However, certain exceptional, resulting vectors are in the same direction as the vectors that are the result of the multiplication. These are the eigenvectors.
    
    In other words, multiply an eigenvector by a matrix, and the resulting vector of that multiplication is equal to a multiplication of the original eigenvector with λ
    , the eigenvalue:
    

## Miscellaneous points to remember

- How to calculate inverse?
    
    First calculate minor matrix, then put in signs to make cofactor matrix, then transpose to get adjoint. [https://www.mathsisfun.com/algebra/matrix-inverse-minors-cofactors-adjugate.html](https://www.mathsisfun.com/algebra/matrix-inverse-minors-cofactors-adjugate.html)
    
- Difference between metric and norm?
    
    the axioms for metrics are satisfied under this definition and follow directly from
    the axioms for norms. Therefore any normed space is also a metric space.
    
    metrics can be defined on pretty much anything, while the notion of a norm applies only to vector spaces: the very definition of a norm requires that the things measured by the norm could be added and scaled. If you have a norm, you can define a metric by saying that the distance between a and b is the size of a−b
    
    d(a,b)=∥a−b∥
    
    On the other hand, if you have a metric you can't usually define a norm.
    
- Different types of norms?
    1. L2 (also called Euclidean distance): sum up squares, then square root
    2. L1 (also called Manhattan distance): Sum of mod
    3. L-infinity: max of mod values
    4. L0: all nonzero elements of vector
- Conditions a function must satisfy to be called a norm?
    1. Triangle inequality: p(x + y) ≤ p(x) + p(y)
    2. Homogeneity: p(sx) = |s|p(x)
    3. positive definiteness: p(x) = 0 iff x = 0.
- Proof that a matrix can have only one inverse?
    
    To prove that A has at most one inverse, suppose B and B’ are inverses of A. Then
    B = BI = B(AB') = (BA)B' = IB' = B'
    
- Difference between gram matrix (A^TA) and covariance matrix (AA^T)?
    
    *XXT* represents the similarity matrix, e.g., if *X* is row normalized, each entry represents pairwise cosine similarity. *XTX* is the covariance matrix if we have *X* is mean-normalized (has 0 mean columns), since Σ=*E*[*XTX*], when we have *E*[*X*]=0. Both matrices have same eigenvalues and the eigenvectors of one matrix can be obtained from the other one's by simple linear transformation.
    
- Difference between Jacobian and gradient?
    
    Gradient is applied on one function; Jacobian is a matrix containing gradients of multiple functions
    
- How to check linear independence?
    
    If Gram matrix (A^TA) has nonzero determinant.
    

## Matrix Algebra

Read some identities here: 

[](https://www.math.uwaterloo.ca/~hwolkowi/matrixcookbook.pdf)

- Derivative of a matrix?
    
    Can be found by derivative of each element.  
    
- Derivative of determinant?
    
    $\frac{\partial det(Y)}{\partial x} = det(Y)Tr(Y^{-1} \frac{\partial Y}{\partial x})$
    
- Derivative of inverse?
    
    $\frac{\partial X^{-1}}{\partial x} = -X^{-1}\frac{\partial X^{-1}}{\partial x}X^{-1}$
    
- Derivative of transpose?
    
     $\partial X^T = (\partial X)^T$
    
- Derivative of trace?
    
    $I$.
    
- Other derivatives:
    
    $\frac{\partial a^TXb}{\partial X} = ab^T$
    
    $\frac{\partial a^TX^Tb}{\partial X} = ba^T$
    
- How to find basis of column span?
    
    Convert matrix to Reduced Row Echelon Form (RREF). Then number of linearly independent columns gives rank, and those columns themselves are the basis.