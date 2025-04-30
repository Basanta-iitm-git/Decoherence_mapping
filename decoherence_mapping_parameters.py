from qutip import jmat

# Nuclear spin system with hyperfine and quadrupole parameters
class nuclear:
    def __init__(self, name):
        self.name = name
        
        if self.name == 'NV_14N':
            self.A_xx = 2.7    # MHz
            self.A_yy = 2.7    # MHz
            self.A_zz = 2.14   # MHz
            self.A_xy = 0      # MHz
            self.A_yx = 0      # MHz
            self.A_xz = 0      # MHz
            self.A_zx = 0      # MHz
            self.A_yz = 0      # MHz
            self.A_zy = 0      # MHz
            self.Q_xx = 0      # MHz
            self.Q_yy = 0      # MHz
            self.Q_zz = 0      # MHz
            self.Q_xy = 0      # MHz
            self.Q_yx = 0      # MHz
            self.Q_xz = 0      # MHz
            self.Q_zx = 0      # MHz
            self.Q_yz = 0      # MHz
            self.Q_zy = 0      # MHz
            self.g = 3.0766    # MHz/T
            self.Iz = jmat(3,'z')
            self.Iy = jmat(3,'y')
            self.Ix = jmat(3,'x')
            self.dimension = 7
        
        elif self.name == 'NV_15N':
            self.A_xx = 3.65   # MHz
            self.A_yy = 3.65   # MHz
            self.A_zz = 3.03   # MHz
            self.A_xy = 0      # MHz
            self.A_yx = 0      # MHz
            self.A_xz = 0      # MHz
            self.A_zx = 0      # MHz
            self.A_yz = 0      # MHz
            self.A_zy = 0      # MHz
            self.Q_xx = 0      # MHz
            self.Q_yy = 0      # MHz
            self.Q_zz = 0      # MHz
            self.Q_xy = 0      # MHz
            self.Q_yx = 0      # MHz
            self.Q_xz = 0      # MHz
            self.Q_zx = 0      # MHz
            self.Q_yz = 0      # MHz
            self.Q_zy = 0      # MHz
            self.g = 4.3156    # MHz/T
            self.Iz = jmat(1/2,'z')
            self.Iy = jmat(1/2,'y')
            self.Ix = jmat(1/2,'x')
            self.dimension = 2

        elif self.name == 'NV_13C':
            self.A_xx = 0.5    # MHz
            self.A_yy = 0.5    # MHz
            self.A_zz = 0.5    # MHz
            self.A_xy = 0      # MHz
            self.A_yx = 0      # MHz
            self.A_xz = 0      # MHz
            self.A_zx = 0      # MHz
            self.A_yz = 0      # MHz
            self.A_zy = 0      # MHz
            self.Q_xx = 0      # MHz
            self.Q_yy = 0      # MHz
            self.Q_zz = 0      # MHz
            self.Q_xy = 0      # MHz
            self.Q_yx = 0      # MHz
            self.Q_xz = 0      # MHz
            self.Q_zx = 0      # MHz
            self.Q_yz = 0      # MHz
            self.Q_zy = 0      # MHz
            self.g = 10.7084   # MHz/T
            self.Iz = jmat(1/2,'z')
            self.Iy = jmat(1/2,'y')
            self.Ix = jmat(1/2,'x')
            self.dimension = 2

        elif self.name == 'VB_14N1':
            self.A_xx = 46.944   # MHz
            self.A_yy = 90.025   # MHz
            self.A_zz = 48.158   # MHz
            self.A_xy = 0        # MHz
            self.A_yx = 0        # MHz
            self.A_xz = 0        # MHz
            self.A_zx = 0        # MHz
            self.A_yz = 0        # MHz
            self.A_zy = 0        # MHz
            self.Q_xx = -0.46    # MHz
            self.Q_yy = 0.98     # MHz
            self.Q_zz = -0.52    # MHz
            self.Q_xy = 0        # MHz
            self.Q_yx = 0        # MHz
            self.Q_xz = 0        # MHz
            self.Q_zx = 0        # MHz
            self.Q_yz = 0        # MHz
            self.Q_zy = 0        # MHz
            self.g = 3.0766      # MHz/T
            self.Iz = jmat(1,'z')
            self.Iy = jmat(1,'y')
            self.Ix = jmat(1,'x')
            self.dimension = 3

        elif self.name == 'VB_14N2':
            self.A_xx = 79.406   # MHz
            self.A_yy = 58.170   # MHz
            self.A_zz = 48.159   # MHz
            self.A_xy = -18.391  # MHz
            self.A_yx = -18.391  # MHz
            self.A_xz = 0        # MHz
            self.A_zx = 0        # MHz
            self.A_yz = 0        # MHz
            self.A_zy = 0        # MHz
            self.Q_xx = 0.62     # MHz
            self.Q_yy = -0.1     # MHz
            self.Q_zz = -0.52    # MHz
            self.Q_xy = -0.623   # MHz
            self.Q_yx = -0.623    # MHz
            self.Q_xz = 0        # MHz
            self.Q_zx = 0        # MHz
            self.Q_yz = 0        # MHz
            self.Q_zy = 0        # MHz
            self.g = 3.0766      # MHz/T
            self.Iz = jmat(1,'z')
            self.Iy = jmat(1,'y')
            self.Ix = jmat(1,'x')
            self.dimension = 3

        elif self.name == 'VB_14N3':
            self.A_xx = 79.406   # MHz
            self.A_yy = 58.170   # MHz
            self.A_zz = 48.159   # MHz
            self.A_xy = 18.391   # MHz
            self.A_yx = 18.391   # MHz
            self.A_xz = 0        # MHz
            self.A_zx = 0        # MHz
            self.A_yz = 0        # MHz
            self.A_zy = 0        # MHz
            self.Q_xx = 0.62     # MHz
            self.Q_yy = -0.1     # MHz
            self.Q_zz = -0.52    # MHz
            self.Q_xy = 0.623    # MHz
            self.Q_yx = 0.623    # MHz
            self.Q_xz = 0        # MHz
            self.Q_zx = 0        # MHz
            self.Q_yz = 0        # MHz
            self.Q_zy = 0        # MHz
            self.g = 3.0766      # MHz/T
            self.Iz = jmat(1,'z')
            self.Iy = jmat(1,'y')
            self.Ix = jmat(1,'x')
            self.dimension = 3

        elif self.name == 'None':
            self.A_xx = 0      # MHz
            self.A_yy = 0      # MHz
            self.A_zz = 0      # MHz
            self.A_xy = 0      # MHz
            self.A_yx = 0      # MHz
            self.A_xz = 0      # MHz
            self.A_zx = 0      # MHz
            self.A_yz = 0      # MHz
            self.A_zy = 0      # MHz
            self.Q_xx = 0      # MHz
            self.Q_yy = 0      # MHz
            self.Q_zz = 0      # MHz
            self.Q_xy = 0      # MHz
            self.Q_yx = 0      # MHz
            self.Q_xz = 0      # MHz
            self.Q_zx = 0      # MHz
            self.Q_yz = 0      # MHz
            self.Q_zy = 0      # MHz
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
            self.E = 0 
            self.g = -28025       # MHz/T
            self.Sz = jmat(1/2,'z')
            self.Sy = jmat(1/2,'y')
            self.Sx = jmat(1/2,'x')
            self.dimension = 2

        elif self.name == 'NV-':
            self.D = 2878         # MHz
            self.E = 0 
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
            self.E = 0 
            self.g = 0
            self.Sz = jmat(0,'z')
            self.Sy = jmat(0,'y')
            self.Sx = jmat(0,'x')
            self.dimension = 0