from qutip import jmat

# Nuclear spin system with hyperfine and quadrupole parameters
class nuclear:
    def __init__(self, name):
        self.name = name
        
        if self.name == '14N':
            self.A_perp = 2.7
            self.A_par = 2.14  # MHz
            self.Q = 5.01      # MHz
            self.g = 3.0766    # MHz/T
            self.Iz = jmat(3,'z')
            self.Iy = jmat(3,'y')
            self.Ix = jmat(3,'x')
            self.dimension = 7

        elif self.name == '14N11':
            self.A_xx = 46.944
            self.A_yy = 90.025
            self.A_zz = 48.158
            self.A_xy = 0.00
            self.Q_xx = -0.46
            self.Q_yy = 0.98
            self.Q_zz = -0.52
            self.Q_xy = 0.00
            self.g = 3.0766
            self.Iz = jmat(1,'z')
            self.Iy = jmat(1,'y')
            self.Ix = jmat(1,'x')
            self.dimension = 3

        elif self.name == '14N12':
            self.A_xx = 79.406
            self.A_yy = 58.170
            self.A_zz = 48.159
            self.A_xy = -18.391
            self.Q_xx = 0.62
            self.Q_yy = -0.1
            self.Q_zz = -0.52
            self.Q_xy = -0.623
            self.g = 3.0766
            self.Iz = jmat(1,'z')
            self.Iy = jmat(1,'y')
            self.Ix = jmat(1,'x')
            self.dimension = 3

        elif self.name == '14N13':
            self.A_xx = 79.406
            self.A_yy = 58.170
            self.A_zz = 48.159
            self.A_xy = 18.391
            self.Q_xx = 0.62
            self.Q_yy = -0.1
            self.Q_zz = -0.52
            self.Q_xy = 0.623
            self.g = 3.0766
            self.Iz = jmat(1,'z')
            self.Iy = jmat(1,'y')
            self.Ix = jmat(1,'x')
            self.dimension = 3

        elif self.name == '15N':
            self.A_perp = 3.65
            self.A_par = 3.03
            self.Q = 0
            self.g = 4.3156
            self.Iz = jmat(1/2,'z')
            self.Iy = jmat(1/2,'y')
            self.Ix = jmat(1/2,'x')
            self.dimension = 2

        elif self.name == '13C':
            self.A_perp = 0.5
            self.A_par = 0.5
            self.Q = 0
            self.g = 10.7084
            self.Iz = jmat(1/2,'z')
            self.Iy = jmat(1/2,'y')
            self.Ix = jmat(1/2,'x')
            self.dimension = 2

        elif self.name == 'None':
            self.A_perpx = 0
            self.A_perpy = 0
            self.A_par = 0
            self.A_XY = 0
            self.Q = 0
            self.g = 0
            self.Iz = jmat(0,'z')
            self.Iy = jmat(0,'y')
            self.Ix = jmat(0,'x')
            self.dimension = 0


# Electronic spin system with Zeeman and zero-field splitting parameters
class electronic:
    def __init__(self, name):
        self.name = name

        if self.name == 'electron':
            self.D = 0            # MHz
            self.g = -28025       # MHz/T
            self.Sz = jmat(1/2,'z')
            self.Sy = jmat(1/2,'y')
            self.Sx = jmat(1/2,'x')
            self.dimension = 2

        elif self.name == 'NV-':
            self.D = 2878         # MHz
            self.g = -28025       # MHz/T
            self.Sz = jmat(1,'z')
            self.Sy = jmat(1,'y')
            self.Sx = jmat(1,'x')
            self.dimension = 3

        elif self.name == 'VB-':
            self.D = 3450         # MHz (formerly 3476)
            self.E = 0            # MHz (strain-induced splitting)
            self.g = -28025       # MHz/T
            self.Sz = jmat(1,'z')
            self.Sy = jmat(1,'y')
            self.Sx = jmat(1,'x')
            self.dimension = 3

        elif self.name == 'None':
            self.D = 0
            self.g = 0
            self.Sz = jmat(0,'z')
            self.Sy = jmat(0,'y')
            self.Sx = jmat(0,'x')
            self.dimension = 0