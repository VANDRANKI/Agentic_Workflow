# Full Length Article 

## RE (La, Nd and Yb) doped $\mathrm{CeO}_{2}$ abrasive particles for chemical mechanical polishing of dielectric materials: Experimental and computational analysis

Jie Cheng ${ }^{\mathrm{a}, \mathrm{b}}$, Shuo Huang ${ }^{\mathrm{c}}$, Yang $\mathrm{Li}^{\mathrm{d}}$, Tongqing Wang ${ }^{\mathrm{a}}$, Lile Xie ${ }^{\mathrm{a}}$, Xinchun $\mathrm{Lu}^{\mathrm{a}, *}$<br>${ }^{a}$ State Key Lab of Tribology, Tsinghua University, Beijing 100084, China<br>${ }^{\mathrm{b}}$ Laser Micro/Nano Fabrication Laboratory, School of Mechanical and Vehicular Engineering, Beijing Institute of Technology, Beijing 100081, China<br>${ }^{c}$ Applied Materials Physics, Department of Materials Science and Engineering, Royal Institute of Technology, Stockholm SE-100 44, Sweden<br>${ }^{d}$ Department of Chemistry, Tsinghua University, Beijing 100084, China

## A R T I C L E I N F O

Keywords:
Ceria $\left(\mathrm{CeO}_{2}\right)$
Incipient impregnation
Surface doping
Chemical mechanical polishing (CMP)
Lanthanide elements
Density functional theory (DFT)


#### Abstract

$\mathrm{Ce}^{3+}$ in $\mathrm{CeO}_{2}$, rather than $\mathrm{Ce}^{4+}$, is believed to provide assistance to the breaking up of $\mathrm{Si}-\mathrm{O}$ bond during chemical mechanical polishing (CMP) of silica. In the paper, lanthanide metals ( $\mathrm{La}, \mathrm{Nd}$ and Yb ) doped $\mathrm{CeO}_{2}$ nanoparticles were synthesized by modified incipient impregnation method in order to improve the content of $\mathrm{Ce}^{3+}$ in $\mathrm{CeO}_{2}$ as polishing. X-ray photoelectron spectroscopy (XPS) experiments and density function theory (DFT) calculation demonstrate this approach could achieve surface doping of $\mathrm{CeO}_{2}$ nanoparticles, and facilitates the formation of oxygen vacancy and $\mathrm{Ce}^{3+}$ content. CMP experiments show that the polishing rate and the surface quality of silica wafer are obviously improved by using the doped $\mathrm{CeO}_{2}$ as abrasive particles. Especially for $\mathrm{Nd} / \mathrm{CeO}_{2}$, content of $\mathrm{Ce}^{3+}$ increases from 0.146 to 0.235 , the polishing rate of silica is accelerated by $29.6 \%$ in alkaline slurries, and a better surface quality $(\mathrm{Sa}=9.6 \AA$ ) is obtained.


## 1. Introduction

Chemical mechanical planarization (CMP) is the enabling technology mainly applied to achieve both local and global planarity of semiconductor devices. Continuous technology advances have led to an increasing importance of CMP technique. The new device architectures and the relevant scaling challenges result in strict tolerance in defectivity, the non-uniformity and the material removal variation during CMP so as to meet performance and yield targets. Ceria $\left(\mathrm{CeO}_{2}\right)$, as one of the most widely used abrasive particle in CMP slurry, has gained wide application in the traditional dielectric polishing processes of integrated circuit (IC), such as the CMP of shallow trench isolation (STI) and inter-level dielectric (ILD) [1,2]. The ceria based-slurry is often cable of achieving a high ratio of oxide (e.g. $\mathrm{SiO}_{2}$ ) material removal rate to nitride (e.g. $\mathrm{Si}_{3} \mathrm{~N}_{4}$ ) removal, which is important to minimize the nitride loss in the crucial region in STI [3,4]. Apart from this, the cerialbased slurry could obtain a high removal efficiency of dielectric at a low dosage in slurry ( $\leq 1 \mathrm{wt} \%$ ), while for colloidal $\mathrm{SiO}_{2}$ abrasives the dosage could be $\geq 10 \mathrm{wt} \%$ to achieve identical material removal rate (MRR) [5-7]. Emerging technologies such as fin field-effect transistor (FinFET) have proposed more rigorous control for the CMP of dielectrics. Under this condition, ceria, as the most applicable abrasive particle, gains continuous emphasis on improving its performance in
the CMP of dielectric materials.
$\mathrm{CeO}_{2}$ abrasives could realize the material removal of dielectrics under the effect of both mechanical abrasion and chemical reaction on the surface layer. It is widely believed that $\mathrm{CeO}_{2}$ has a great affinity toward the silicon oxide, which helps in breaking the bonds on $\mathrm{SiO}_{2}$ surface. The surface of $\mathrm{SiO}_{2}$ in water is terminated with $\mathrm{Si}-\mathrm{OH}$ while that of $\mathrm{CeO}_{2}$ is $\mathrm{Ce}-\mathrm{OH}$. After the proton abstraction of $\mathrm{Si}-\mathrm{OH}, \mathrm{Si}-\mathrm{O}^{-}$ will react with $\mathrm{Ce}-\mathrm{OH}$ to form $\mathrm{Si}-\mathrm{O}-\mathrm{Ce}$ bonds. Since the $\mathrm{Si}-\mathrm{O}-\mathrm{Ce}$ bonds are stronger than $\mathrm{Si}-\mathrm{O}-\mathrm{Si}$ bonds, the surface layer of $\mathrm{SiO}_{2}$ is removed by the coupling of mechanical and chemical phenomena $[3,8,9]$. With regard to $\mathrm{Si}_{3} \mathrm{~N}_{4}$, the material removal mechanism is similar, but more complex [10,11]. The actual MRR of dielectric materials depends on not only the additives in the slurry [4], but also the pH values of the slurry [1] and the characteristics of the $\mathrm{CeO}_{2}$ particles, which will notably affect the physicochemical properties between the $\mathrm{CeO}_{2}$ particle and the dielectric material surface [12-14]. Therefore, one way is to improve the CMP performance of dielectrics is to achieve surface modification of $\mathrm{CeO}_{2}$ abrasive particles. Common methods include grafting functional groups to $\mathrm{CeO}_{2}$ surface and synthesizing $\mathrm{CeO}_{2^{-}}$ X core-shell composite particles [6,14-16].

Cerium has unique valence transition properties. In $\mathrm{CeO}_{2}$ lattice, there is coexistence of $\mathrm{Ce}^{3+}$ and $\mathrm{Ce}^{4+}$ oxidation states and presence of intrinsic oxygen vacancies [17]. It has been proposed that $\mathrm{Ce}^{3+}$, instead

[^0]
[^0]:    ${ }^{\text {a }}$ Corresponding author.
    E-mail address: xclu@tsinghua.edu.cn (X. Lu).

of $\mathrm{Ce}^{4+}$ in $\mathrm{CeO}_{2}$ abrasive particles, provides assistance to the breaking up of $\mathrm{Si}-\mathrm{O}$ bond during CMP, leading to a high removal rate of silica [1,18,19]. Approaches to improve $\mathrm{Ce}^{3+}$ content in $\mathrm{CeO}_{2}$ include reducing the particle size [20], lowering the $\mathrm{CeO}_{2}$ content in polishing slurry [18], and introduction of dopants [21,22]. Trivalent dopants, mainly the rare-earth elements, could substitute $\mathrm{Ce}^{4+}$, release more oxygen vacancies and cause partial reduction of neighboring $\mathrm{Ce}^{4+}$ to $\mathrm{Ce}^{3+}[23,24]$. It has been reported that lanthanum impurities have been found on commercial $\mathrm{CeO}_{2}$ abrasive particles [25]. Some lanthanide elements have been successfully used as the dopants in $\mathrm{CeO}_{2}$ nanoparticles for catalytic applications and oxygen sensors [21,26,27].

Inspired by this idea, we proposed a new strategy to increase the $\mathrm{Ce}^{3+}$ fraction on the surface of $\mathrm{CeO}_{2}$ nanoparticles, so as to improve the polishing rate of silica when $\mathrm{CeO}_{2}$ was used as abrasive. Typical lanthanide elements RE (RE = lanthanum-La, neodymium-Nd and ytter-bium-Yb) were chosen as the dopants. RE doped $\mathrm{CeO}_{2}$ nanoparticles (marked as $\mathrm{RE} / \mathrm{CeO}_{2}$ ) were prepared by modified incipient impregnation method, which was ideal to realize surface doping with fixed dopant load, and not change the original crystal structure of $\mathrm{CeO}_{2}$. The concentration of $\mathrm{Ce}^{3+}$ in $\mathrm{CeO}_{2}$ was calculated by X-ray photoelectron spectroscopy (XPS) experiments and verified by first-principles calculation based on density functional theory (DFT). The polishing effects of silica using $\mathrm{RE} / \mathrm{CeO}_{2}$ as abrasives were verified by CMP experiments. The findings in the manuscript provide a novel approach to improve polishing rate of silica in CMP application when $\mathrm{CeO}_{2}$ is used as nanoabrasive particles.

## 2. Experimental and methods

### 2.1. Preparation of lanthanide elements doped $\mathrm{CeO}_{2}$ nanoparticles

$\mathrm{CeO}_{2}$ nanoparticles ( $99.95 \%$ in purity), with primary diameter less than 50 nm , was purchased from Sigma-Aldrich Corporation. Lanthanide nitrates were used as precursors: $\mathrm{La}\left(\mathrm{NO}_{3}\right)_{2} \cdot 6 \mathrm{H}_{2} \mathrm{O}(99.99 \%)$ and $\mathrm{Yb}\left(\mathrm{NO}_{3}\right)_{2} \cdot 5 \mathrm{H}_{2} \mathrm{O}$ (99.9\%) from Aladdin Bio-Chem Technology Co. and $\mathrm{Nd}\left(\mathrm{NO}_{3}\right)_{2} \cdot 6 \mathrm{H}_{2} \mathrm{O}$ ( $99.9 \%$ ) from MACKLIN Biochemical Co.. The process of the preparation of $\mathrm{RE} / \mathrm{CeO}_{2}$ nanoparticles by modified incipient impregnation method is shown in Fig. 1. The impregnation volume of $\mathrm{CeO}_{2}$ was measured to be $0.280 \mathrm{~g} / 1 \mathrm{~g}$. The load of dopant was set to be $5 \%$ in this paper. As a typical procedure, 5 g of the pristine $\mathrm{CeO}_{2}$ was impregnated with the nitrate solution at the desired mass ratio. Then they were fully mixed to get a uniform paste. After aging for 12 h and drying at $120^{\circ} \mathrm{C}$ for 12 h , the paste was calcined in muffle furnace at a heating rate of $5^{\circ} \mathrm{C} / \mathrm{min}$, maintained at $400^{\circ} \mathrm{C}$ for 2 h and then naturally cooled down to room temperature. Subsequently, the doped $\mathrm{CeO}_{2}$ powders were ground in agate mortar. The calcination temperature was determined by the decomposition temperatures of nitrates which were measured by a thermo-gravimetric apparatus (TGA/DSC1, Mettler Toledo), with a heating rate of $10^{\circ} \mathrm{C} / \mathrm{min}$. The prepared sample was denoted as $\mathrm{RE} / \mathrm{CeO}_{2}(\mathrm{RE}=\mathrm{La}, \mathrm{Nd}$ and Yb$)$.
![img-0.jpeg](images\img-0.jpeg)

Fig. 1. Flow chart of the preparation of $\mathrm{RE} / \mathrm{CeO}_{2}$ by improved incipient impregnation method. $\mathrm{RE}=\mathrm{La}, \mathrm{Nd}$ or Yb . Doping load is $5 \%$.

### 2.2. Characterization of $\mathrm{RE} / \mathrm{CeO}_{2}$ nanoparticles

The lattice structure of $\mathrm{CeO}_{2}$ particles was meausured by X-Ray diffraction spectroscopy (XRD, D8ADVANCE, Bruker). Data were processed by Jade 5.0 software. The particle morphology and element distribution were characterized using transmission electron microscopy (TEM, JEM-2010F, JEOL) equipped with energy dispersive spectroscopy (EDS) system. The valence states of Cerium $\left(\mathrm{Ce}^{3+} / \mathrm{Ce}^{4+}\right)$ were characterized using X-ray photoelectron spectroscopy (XPS, PHI Quantera II, Ulvac-Phi). The fraction of $\mathrm{Ce}^{3+}$ was calculated based on the deconvolution of Ce 3d spin-orbit doublet using XPSPEAK software.

The Zeta potential of pristine $\mathrm{CeO}_{2}$ nanoparticles was measured by a laser zeta potential analyzer (Nano ZS90, Malvern). The Zeta potential of PECVD silica thin film surface was measured by a surface charge analysis (SurPASS 3, Anton Parr). CMP experiments were carried out by polishing a 2 in. $\mathrm{SiO}_{2}$ blanket wafer made by plasma enhanced chemical vapor deposition, on a CMP machine (Universal-150, Tianjin Hwatsing Technology Co.). The head/platen rotational speed was $100 / 100 \mathrm{rpm}$, the slurry flow rate was $100 \mathrm{ml} / \mathrm{min}$, and the down pressure was 2 psi . The polishing time was 1.5 min and before each polishing an ex-situ conditioning of the pad was carried out for 30 s . The pad used was Politex from Dow Chemical Co.. The MRR of $\mathrm{SiO}_{2}$ was calculated by measuring the film thickness (Resmap, Creative Design Engineering). In the measurement, the edge exclusion was 5 mm and 81 dots were measured within the wafer. The topography of polished $\mathrm{SiO}_{2}$ surface was measured by a surface profilometer (Talysurf PGI, Taylor-hobson).

### 2.3. Ab initio calculations

The density functional calculations were carried out with the Vienna ab initio simulation package (VASP) [28,29]. The electron wave functions were described with the projector augmented wave (PAW) method [30]. Plane waves were included up to an energetic cut off of 500 eV . The exchange-correlation effects were treated with the generalized gradient approximation (GGA) in the form of Perdew, Burke and Ernzerhof (PBE) [31]. The effective Hubbard parameter $U$ was employed to account for the strong on-site Coulomb repulsion amongst the localized $4 f$ orbital for the lanthanide series elements [32]. In this study, $U=5 \mathrm{eV}$ was applied to the $4 f$ states of Ce and dopants, and in addition, $U=5.5 \mathrm{eV}$ was applied to the $2 p$ states of O [33]. A $2 \times 2 \times 2$ supercell of the cubic fluorite structure with 96 atoms was used as initial structural model. The Brillouin zone integrations were performed with a $2 \times 2 \times 2$ Monkhorst-Pack grid [34]. The structure optimizations were pursued until the force on each atom was less than $0.02 \mathrm{eV} / \AA$. The equilibrium volume was extracted from the Birch-Murnaghane equation of state fitted to the ab initio total energies for different volumes.

## 3. Results and discussions

### 3.1. RE-doped (RE = La, Nd or Yb) $\mathrm{CeO}_{2}$ by incipient impregnation method

The results of thermogravimetry experiments are shown in Fig. 2, which could be used to determine the calcination temperature of doped $\mathrm{CeO}_{2}$ prepared by incipient impregnation method. The weight loss curves (TG) and derivative weight loss curves (DTG) refer to left Y axis and right Y axis, respectively. To avoid the influence of carrier and doping load on the decomposition temperature, nitride impregnated $\mathrm{CeO}_{2}$ nanoparticles, instead of nitrates powder, were used as the samples [35]. In the DTG curves, the peak within lower temperature range ( $\leq 100^{\circ} \mathrm{C}$ ) indicates the loss of crystal water. The peaks at higher temperature range indicate the decomposition of nitrates. The decomposition temperature of $\mathrm{Yb}\left(\mathrm{NO}_{3}\right)_{2} \cdot 5 \mathrm{H}_{2} \mathrm{O}$ is comparatively lower at ca. $160^{\circ} \mathrm{C}$, and that for $\mathrm{La}\left(\mathrm{NO}_{3}\right)_{2} \cdot 6 \mathrm{H}_{2} \mathrm{O}$ and $\mathrm{Nd}\left(\mathrm{NO}_{3}\right)_{2} \cdot 6 \mathrm{H}_{2} \mathrm{O}$ is at ca. $400^{\circ} \mathrm{C}$. Therefore, the calcination temperature of nitrates impregnated $\mathrm{CeO}_{2}$ was set at $400^{\circ} \mathrm{C}$, to ensure the thorough decomposition of nitrates and

![img-1.jpeg](images\img-1.jpeg)

Fig. 2. Thermogravimetry (TG-DTG) curves of the $\mathrm{RE}\left(\mathrm{NO}_{3}\right)_{2} \mathrm{nH}_{2} \mathrm{O}$ impregnated $\mathrm{CeO}_{2} . \mathrm{RE}=\mathrm{La}, \mathrm{Nd}$ or Yb . RE load is $5 \%$.
to avoid further growth/agglomeration of the $\mathrm{CeO}_{2}$ nanoparticles.
Fig. 3(a) and (b) shows the crystalline phase information of the prepared $\mathrm{RE} / \mathrm{CeO}_{2}$ particles ( $\mathrm{RE}=\mathrm{La}, \mathrm{Nd}$ or Yb ) by XRD. For comparison, the XRD patterns of lanthanide oxides prepared by direct calcination from lanthanide nitrides at the same temperature $\left(400^{\circ} \mathrm{C}\right)$ are shown in Fig. 3(c). The XRD patterns of doped $\mathrm{CeO}_{2}$ particles remain typical pattern of fluorite structure and correspond well with the standard data of JCPDS No. 65-5923 [36]. However the lanthanide oxides are almost amorphous. Thus, it is safe to say that the doping process does not introduce a secondary phase and the $\mathrm{RE} / \mathrm{CeO}_{2}$ particles remain the intrinsic lattice structure of $\mathrm{CeO}_{2}$. The only change observed after doping is the sharpening and weakening of the diffraction peaks, which is caused by the increase of lattice imperfections under the introduction of dopants, as is clearly shown in Fig. 2(b). According to the Debye-Scherrer equation [37], the grain size could be calculated based on the broadening of the diffraction peak and the Bragg angle. The calculated average particle size based on three main crystallographic plane ( 111 ), (2 20 ) and (3 11 ) is shown in Table 1. The doping process does not cause growth of the grain size, with a uniform diameter of ca. 20 nm . Due to the lattice distortion under the introduction of dopants, the lattice constant of $\mathrm{RE} / \mathrm{CeO}_{2}$ increases compared with pristine $\mathrm{CeO}_{2}$ (Table 1), which can be directly correlated with crystal radii of dopants. The crystal radii (with 8 ligands) of $\mathrm{La}^{3+}, \mathrm{Nd}^{3+}$ and $\mathrm{Yb}^{3+}$ are $1.29 \mathrm{~nm}, 1.24 \mathrm{~nm}$ and 1.13 nm , respectively [38], and all of them are larger than that of $\mathrm{Ce}^{4+}(0.97 \mathrm{~nm})$ [39]. Therefore, the introduction of dopants will cause slight lattice expansion of $\mathrm{CeO}_{2}$. It is worth mentioning that the lattice constant is also affected by the content of $\mathrm{Ce}^{3+}$ (with the crystal radius of 1.27 nm ), which will be discussed hereinafter.

The TEM and EDS mapping images of the $\mathrm{RE} / \mathrm{CeO}_{2}$ nanoparticles are shown in Fig. 4, which provide information of particle morphology and the element distribution. The shape of the $\mathrm{RE} / \mathrm{CeO}_{2}$ particle is nearspherical, and the doping elements uniformly distribute on the RE/ $\mathrm{CeO}_{2}$ nanoparticles, indicating that the doping is uniform without formation of secondary phases, coinciding well with the XRD results. The element distribution across single particle, with $\mathrm{Yb} / \mathrm{CeO}_{2}$ particle as an example, is shown in Fig. 5. In Fig. 5(b), the element intensities along Y axis were normalized for better clarity. It is noticeable that there are "teeth like" sharps on the curve of Yb element, which appear at the boundary of the nanoparticle. The appearance of the sharps indicates that the dopant element (Yb) concentrates at the surface of $\mathrm{CeO}_{2}$, instead of diffuses into the bulk of the particle. Therefore, it is safe to say that the doping method applied in this study could effectively achieve uniform surface doping on the $\mathrm{CeO}_{2}$ nanoparticles.
![img-2.jpeg](images\img-2.jpeg)

Fig. 3. XRD patterns of (a) $\mathrm{RE} / \mathrm{CeO}_{2}$; (b) enlarged drawing of (1 11 ) and (2 0 0) crystallographic planes in (a); (c) as calcined lanthanide metal oxides.

### 3.2. Influence of doping on oxygen vacancy and $\mathrm{Ce}^{2+} / \mathrm{Ce}^{4+}$ content

Fig. 6 shows the atomic structures and the electronic density of states (DOS) of the $\mathrm{CeO}_{2}$ with and without defects, respectively. For the pristine $\mathrm{CeO}_{2}$, the highest occupied valance band is mainly determined by the $\mathrm{O} 2 p$ states, with some contributions from the $\mathrm{Ce} 4 f$ and $5 d$ states, whereas the characteristic narrow peak above the Fermi level primarily consists of the $\mathrm{Ce} 4 f$ states. The width of $\mathrm{O} 2 p$ states is -4.0 eV , and the energy gap between $\mathrm{O} 2 p$ states and $\mathrm{Ce} 4 f$ states is -2.5 eV , which are in reasonable agreement with the experimental [40] and other DFT calculations [41]. The insulator feature is reproduced when an O vacancy

Table 1
Properties of the doped $\mathrm{CeO}_{2}$ nanoparticles by both experiments and DFT numerical calculation.

| Lattice | $\mathrm{CeO}_{2}$ | $\mathrm{La} / \mathrm{CeO}_{2}$ | $\mathrm{Nd} / \mathrm{CeO}_{2}$ | $\mathrm{Yb} / \mathrm{CeO}_{2}$ |
| :--: | :--: | :--: | :--: | :--: |
| Average size ( $\AA$ ) by XRD | 198 | 188 | 194 | 197 |
| Lattice constant ( $\AA$ ) by XRD | 5.41051 | 5.42264 | 5.41734 | 5.41750 |
| Lattice constant ( $\AA$ ) by DFT | 5.42751 | 5.43696 | 5.43151 | 5.42595 |
| O vacancy formation energy (eV) by DFT | 3.27 | 1.10 | 1.00 | $-1.26$ |
| Concentration of $\mathrm{Ce}^{3+}$ by XPS | 0.146 | 0.194 | 0.235 | 0.264 |

is introduced to the pristine $\mathrm{CeO}_{2}$. Similar results are found for the doped system considered here. Particularly, the DOS is found to be almost unchanged for the $\mathrm{La} / \mathrm{CeO}_{2}$ with and without an O vacancy. Previous work indicated that the electrons that occupy the new gap states are exactly localized on two Ce cations neighboring the O vacancy, and make the two $\mathrm{Ce}^{4+}$ cations reduced to $\mathrm{Ce}^{3+}$ [23,42]. Since O vacancy is directly related to the formation of $\mathrm{Ce}^{3+}$, a lower O vacancy formation energy is indicative of favorable formation of $\mathrm{Ce}^{3+}$ in $\mathrm{CeO}_{2}$. In general, the formation energy of an O vacancy ( $E_{\text {vac }}$ ) can be calculated by
$E_{\text {vac }}=E\left(\right.$ cell $\left._{\text {vac }}\right)+1 / 2 E\left(\mathrm{O}_{2}\right) \cdot E($ cell $)$
where $E\left(\right.$ cell $_{\text {vac }}$ ) and $E($ cell $)$ represent the energies of the supercells with and without an O vacancy, respectively, and $E\left(\mathrm{O}_{2}\right)$ denotes the energy of the ground state of oxygen molecule. A positive $E_{\text {vac }}$ value indicates energy is needed to create an O vacancy. From Table 1, the calculated $E_{\text {vac }}$ for the pristine $\mathrm{CeO}_{2}$ is 3.27 eV per vacancy, in line with other theoretical results [43]. For the $\mathrm{La} / \mathrm{CeO}_{2}, \mathrm{Nd} / \mathrm{CeO}_{2}$ and $\mathrm{Yb} / \mathrm{CeO}_{2}$, the $E_{\text {vac }}$ is largely reduced to $1.10 \mathrm{eV}, 1.00 \mathrm{eV}$ and -1.26 eV , respectively. Notice that a positive to negative transition of the $E_{\text {vac }}$ is predicted for the $\mathrm{Yb} / \mathrm{CeO}_{2}$, indicating that the creation of O vacancy is spontaneous under this condition. Such a large reduction in the O vacancy formation energy suggests that the lanthanide elements ( $\mathrm{La}, \mathrm{Nd}$ and Yb ) could facilitate the formation of O vacancies in $\mathrm{CeO}_{2}$ and also the associated change from $\mathrm{Ce4}^{+}$to $\mathrm{Ce3}^{+}$[44].
XPS data in Fig. 7(a-c) clearly show the existence of dopants in the $\mathrm{RE} / \mathrm{CeO}_{2}$ nanoparticles. Semi-quantitative calculation of $\mathrm{Ce}^{3+}$ content
in the $\mathrm{RE} / \mathrm{CeO}_{2}$ nanoparticles could be conducted by peak deconvolution of XPS spectra. The Ce 3d spectrum of $\mathrm{CeO}_{2}$ is composed of spi-n-orbit split $3 \mathrm{~d}_{3 / 2}$ at high bending energy and $3 \mathrm{~d}_{5 / 2}$ at low binding energy. The spin-orbit split is ca. 18.3 eV . Ten deconvolution peaks could be identified in the Ce 3d spectrum, which is in keeping with the literature [20]. The ten peaks are labeled as $\mathrm{u}_{,} \mathrm{u}_{0}, \mathrm{u}^{\prime}, \mathrm{u}^{\prime \prime}, \mathrm{u}^{\prime \prime \prime}$ and $\mathrm{v}_{,} \mathrm{v}_{0}$, $\mathrm{v}^{\prime}, \mathrm{v}^{\prime \prime}, \mathrm{v}^{\prime \prime \prime}$, as are schematically illustrated in Fig. 4(d). Deconvolution parameters used in this paper is shown in Table 2. By measuring the area of the each peak, the concentration of $\mathrm{Ce}^{3+}$ could be calculated according to the following equations:
$\mathrm{C}\left(\mathrm{Ce}^{3+}\right)=\mathrm{A}\left(\mathrm{Ce}^{3+}\right) /\left[\mathrm{A}\left(\mathrm{Ce}^{3+}\right)+\mathrm{A}\left(\mathrm{Ce}^{3+}\right)\right]$
$\mathrm{A}\left(\mathrm{Ce}^{3+}\right)=\mathrm{A}\left(\mathrm{u}^{\prime}\right)+\mathrm{A}\left(\mathrm{u}_{0}\right)+\mathrm{A}\left(\mathrm{v}^{\prime}\right)+\mathrm{A}\left(\mathrm{v}_{0}\right)$
$\mathrm{A}\left(\mathrm{Ce}^{4+}\right)=\mathrm{A}\left(\mathrm{u}^{\prime}\right)+\mathrm{A}\left(\mathrm{u}^{\prime \prime}\right)+\mathrm{A}\left(\mathrm{u}^{\prime \prime \prime}\right)+\mathrm{A}\left(\mathrm{v}\right)+\mathrm{A}\left(\mathrm{v}^{\prime \prime}\right)+\mathrm{A}\left(\mathrm{v}^{\prime \prime \prime}\right)$
where C and A represent concentration and area, respectively. Therefore, the content of $\mathrm{Ce}^{3+}$ in $\mathrm{CeO}_{2}$ is calculated based on the fraction of area $\left(\mathrm{Ce}^{3+}\right)$ in the total area $\left(\mathrm{Ce}^{3+}\right.$ and $\left.\mathrm{Ce}^{4+}\right)$. The calculated concentration of $\mathrm{Ce}^{3+}$ in all the $\mathrm{CeO}_{2}$ samples is shown in Table 1. The concentration of $\mathrm{Ce}^{3+}$ in pristine $\mathrm{CeO}_{2}$ is only 0.146 . The concentration of $\mathrm{Ce}^{3+}$ significantly increases with the introduction of $\mathrm{RE}(\mathrm{RE}=\mathrm{La}$, Nd and Yb ) dopants for all the doped $\mathrm{CeO}_{2}$ samples. The most obvious growth lies in the $\mathrm{Yb} / \mathrm{CeO}_{2}$ sample, with the content of $\mathrm{Ce}^{3+}$ up to 0.264. The calculation of $\mathrm{Ce}^{3+}$ content is in line with the DFT calculation of the O vacancy formation energy in $\mathrm{CeO}_{2}$, as has been shown in Table 2. A higher content of $\mathrm{Ce}^{3+}$ cation leads to larger lattice strain and subsequent expansion of the lattice constant of ceria, because the crystal radius of $\mathrm{Ce}^{3+}$ is significantly larger than that of $\mathrm{Ce}^{4+}$, as has been aforementioned. Therefore, the lattice expansion after doping is under the effect of both the dopants (with large radii) and the increase of $\mathrm{Ce}^{3+}$ content in the $\mathrm{RE} / \mathrm{CeO}_{2}$ nanoparticles.

### 3.3. CMP of silica using $\mathrm{RE} / \mathrm{CeO}_{2}$ abrasive particles

Zeta potentials of abrasive particles and wafer surface determine the electrostatic interactions between them. If the abrasive particles and wafer surface are oppositely charged, the electrostatic attraction usually accelerates the polishing rate of the wafer material. Fig. 8 compares the Zeta potential of pristine $\mathrm{CeO}_{2}$ nanoparticles and PECVD silica surface. Electrostatic repulsion takes place when the pH value of the slurry is higher than 6.5 or lower than 3.2. Conversely, electrostatic
![img-3.jpeg](images\img-3.jpeg)

Fig. 4. The transmission electron microscopy (TEM) and energy disperse spectroscopy (EDS) mapping images of the as prepared $\mathrm{RE} / \mathrm{CeO}_{2}$ particles: (a) $\mathrm{La} / \mathrm{CeO}_{2}$; (b) $\mathrm{Nd} / \mathrm{CeO}_{2}$; (c) $\mathrm{Yb} / \mathrm{CeO}_{2}$. RE load is $5 \%$.

![img-4.jpeg](images\img-4.jpeg)

Fig. 5. (a) The transmission electron microscopy (TEM) image of $\mathrm{Nd} / \mathrm{CeO}_{2}$ nanoparticles and (b) the element distribution profile of Line 1 indicated in (a).
![img-5.jpeg](images\img-5.jpeg)

Fig. 6. Starting configurations for doped $\mathrm{CeO}_{2}$ : (a) $\mathrm{CeO}_{2}$; (b) $\mathrm{CeO}_{2}$ with one oxygen vacancy placed nearest neighbor to the dopant; (c) $\mathrm{CeO}_{2}$ with one dopant; (d) $\mathrm{CeO}_{2}$ with one dopant and one oxygen vacancy placed nearest neighbor to the dopant. $\mathrm{Ce}, \mathrm{O}$ and dopant are marked as yellow, brown and blue, respectively. (d-h) the density of states (DOS) of $\mathrm{CeO}_{2}$ including dopants and oxygen vacancy.
attraction occurs when the pH value is between 3.2 and 6.5 .
This explains the reason why the MRR of silica is obviously lower when the pH value is 9.5 , compared with that when the pH value is 5 , the results of which are shown in the CMP experimental results in Fig. 9. Fig. 10 illustrates the MRR of silica during polishing with different $\mathrm{CeO}_{2}$ as abrasive particles. Overall speaking, MRR of $\mathrm{SiO}_{2}$ is higher in acidic slurries (at pH 5 ) than that in alkaline slurries (at pH 9.5 ), mainly due to the different electrostatic interactions between abrasive and the wafer surface. When $\mathrm{RE} / \mathrm{CeO}_{2}$ is used in acidic slurries, no enhancement of MRR of $\mathrm{SiO}_{2}$ could be observed. On the contrary, a significantly improved MRR of $\mathrm{SiO}_{2}$ is introduced when $\mathrm{RE} / \mathrm{CeO}_{2}$ is used in the alkaline slurries at pH 9.5 . The doped $\mathrm{CeO}_{2}$ as polishing abrasive particles could achieve an increase of $\mathrm{SiO}_{2}$ removal rate at $20.9 \%, 29.6 \%$ and $4.3 \%$ for $\mathrm{La} / \mathrm{CeO}_{2}, \mathrm{Nd} / \mathrm{CeO}_{2}$ and $\mathrm{Yb} / \mathrm{CeO}_{2}$, respectively. $\mathrm{Yb} / \mathrm{CeO}_{2}$ shows the most increased $\mathrm{Ce}^{3+}$ content (0.363) compared with $\mathrm{La} / \mathrm{CeO}_{2}$ and $\mathrm{Nd} / \mathrm{CeO}_{2}$, but the promotion in the polishing rate of silica is not prominent (only $4.3 \%$ ). Therefore, the chemical interaction between $\mathrm{Ce}^{3+}$ and dielectric surface is only one of the influencing factors during CMP, others such as electrostatic interactions and physical properties of abrasive particles should also be taken into account.

Surface topography after polishing is crucial to evaluate the CMP effect. The topography of $\mathrm{SiO}_{2}$ wafer after CMP is shown in Fig. 10. Commercial $\mathrm{CeO}_{2}$ abrasive particle (No. 2815) was used for
comparison. Results show that the surface roughness (Sa) of $\mathrm{SiO}_{2}$ after CMP by using $\mathrm{RE} / \mathrm{CeO}_{2}$ nanoparticles is ca. $10 \AA$, which shows improvement compared with that of the No. 2815 commercial $\mathrm{CeO}_{2}$ abrasive (Sa of ca. $14 \AA$ ). Therefore, the RE-doped $\mathrm{CeO}_{2}$ nanoparticles ( $\mathrm{RE}=\mathrm{La}, \mathrm{Nd}$ or Yb ) exhibit improved properties when used as abrasive particles in alkaline slurry for the CMP of silica, with both the accelerated polishing rate and better surface quality after polishing.

## 4. Conclusions

To improve the CMP performance of $\mathrm{CeO}_{2}$ as abrasive particles, Lanthanide metals ( $\mathrm{La}, \mathrm{Nd}$ and Yb ) doped ceria nanoparticles were prepared by modified incipient impregnation method. Surface doping of $\mathrm{CeO}_{2}$ nanoparticles could be achieved without affecting the original morphology as abrasive particle, which is proved by TEM/EDS analysis. XPS experiments and DFT numerical calculation indicate that the introduction of dopants ( $\mathrm{La}, \mathrm{Nd}$ and Yb ) could facilitate the formation of oxygen vacancy and transition from $\mathrm{Ce}^{4+}$ to $\mathrm{Ce}^{3+}$ in $\mathrm{CeO}_{2}$. The fraction of $\mathrm{Ce}^{3+}$ in the doped ceria is significantly increased, which is one of the decisive factors for improving the material removal rate of $\mathrm{SiO}_{2}$ during polishing. The $\mathrm{Ce}^{3+}$ content in ceria increases from 0.146 to 0.194 , 0.235 , and 0.264 for the $\mathrm{La} / \mathrm{CeO}_{2}, \mathrm{Nd} / \mathrm{CeO}_{2}$ and $\mathrm{Yb} / \mathrm{CeO}_{2}$, respectively. At the same time, the polishing rate of silica in alkaline slurries is improved by $20.9 \%, 29.6 \%$ and $4.3 \%$ when $\mathrm{La} / \mathrm{CeO}_{2}, \mathrm{Nd} / \mathrm{CeO}_{2}$ and $\mathrm{Yb} /$

![img-6.jpeg](images\img-6.jpeg)

Fig. 7. X-ray photoelectron spectroscopy (XPS) results of $\mathrm{CeO}_{2}$ particles: (a), (b) and (c) show different binding energy ranges; (d) an illustration of the $\mathrm{Ce} 3 \mathrm{~d}_{3 / 2}$, and $3 \mathrm{~d}_{5 / 2}$ spin-orbit doublet spectrum and the peak deconvolution.

Table 2
Peak deconvolution parameters for the Ce 3d X-ray photoelectron spectroscopy (XPS) spectrum in Fig. 7(d).

|  | $\mathrm{Ce}^{3+}$ |  |  |  | $\mathrm{Ce}^{4+}$ |  |  |  |  |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  | $v_{0}$ | $v^{\prime}$ | $u_{0}$ | $u^{\prime}$ | $v$ | $v^{\prime \prime}$ | $v^{\prime \prime \prime}$ | $u$ | $u^{\prime \prime}$ | $u^{\prime \prime \prime}$ |
| Binding energy (eV) | 800.9 | 884.9 | 899.6 | 903.3 | 882.1 | 888.5 | 897.9 | 900.6 | 907.2 | 916.2 |
| FWHM (eV) | 2.0 | 2.9 | 2.5 | 2.9 | 2.5 | 2.8 | 2.0 | 2.2 | 2.3 | 2.5 |

![img-7.jpeg](images\img-7.jpeg)

Fig. 8. Zeta potential of pristine $\mathrm{CeO}_{2}$ nanoparticles and silica surface as a function of slurry pH values.
![img-8.jpeg](images\img-8.jpeg)

Fig. 9. The material removal rate (MRR) of silica dielectric during chemical mechanical polishing (CMP) by using different $\mathrm{CeO}_{2}$ abrasive particles. The slurry contains $0.25 \mathrm{wt} \%$ abrasive particles.

![img-9.jpeg](images\img-9.jpeg)

Fig. 10. Surface topography of silica dielectric after polishing by using different $\mathrm{CeO}_{2}$ abrasive particles: (a) $\mathrm{La} / \mathrm{CeO}_{2}$; (b) Nd/ $\mathrm{CeO}_{2} ;(c) \mathrm{Yb} / \mathrm{CeO}_{2} ;(d)$ pristine $\mathrm{CeO}_{2}$; (e) commercial No. $1815 \mathrm{CeO}_{2}$. (f) Within wafer uniformity after polishing.
$\mathrm{CeO}_{2}$ is used as abrasive particles during CMP. Based on overall consideration, $\mathrm{Nd} / \mathrm{CeO}_{2}$ is the most promising candidate among them as modified $\mathrm{CeO}_{2}$ abrasive particles, with a increased content of $\mathrm{Ce}^{3+}$ of 0.235 , improved $\mathrm{SiO}_{2}$ polishing rate of silica at $29.6 \%$, and a better surface quality after polishing ( $\mathrm{Sa}=9.3 \AA$ ).

## Declaration of Competing Interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

## Acknowledgement

The authors greatly appreciate financial support from the National Natural Science Foundation of China (No. 51705278) and Postdoctoral Science Foundation of China (No. 2018T110093).

## Appendix A. Supplementary material

Supplementary data to this article can be found online at https:// doi.org/10.1016/j.apsusc.2019.144668.

## References

[1] R. Srinivasan, P.V. Dandu, S.V. Babu, Shallow trench isolation chemical mechanical planarization: a review, ECS J. Solid State Sci. 4 (2015) P5029-P5039.
[2] L. Peedikakkandy, L. Kalita, P. Kavle, A. Kadam, Y. Gujar, M. Arcot, P. Bhargava, Preparation of spherical ceria coated silica nanoparticle abrasives for CMP application, Appl. Surf. Sci. 357 (2015) 1306-1312.
[3] M. Oh, J. Nho, S. Cho, J. Lee, R.K. Singh, Polishing behaviors of ceria abrasives on silicon dioxide and silicon nitride CMP, Powder Technol. 206 (2011) 239-245.
[4] J. Park, T. Katoh, W. Lee, H. Jeon, U. Paik, Surfactant effect on oxide-to-nitride removal selectivity of nano-abrasive ceria slurry for chemical mechanical polishing, Jpn. J. Appl. Phys. 42 (2003) 5420.
[5] H. Lee, H. Jeong, Analysis of removal mechanism on oxide CMP using mixed abrasive slurry, Int. J. Precis. Eng. Manage. 16 (2015) 603-607.
[6] S. Lee, Z. Lu, S.V. Babu, E. Matijević, Chemical mechanical polishing of thermal oxide films using silica particles coated with ceria, J. Mater. Res. 17 (2002) $2744-2749$.
[7] P.D. Veera, S. Peddeti, S.V. Babu, Selective chemical mechanical polishing of silicon dioxide over silicon nitride for shallow trench isolation using ceria slurries, J. Electrochem. Soc. 156 (2009) H936-H943.
[8] A. Rajendran, Y. Takahashi, M. Koyama, M. Kubo, A. Miyamoto, Tight-binding quantum chemical molecular dynamics simulation of mechano-chemical reactions during chemical-mechanical polishing process of SiO2 surface by CeO2 particle, Appl. Surf. Sci. 244 (2005) 34-38.
[9] P.W. Carter, T.P. Johns, Interfacial reactivity between ceria and silicon dioxide and silicon nitride surfaces, Electrochem. Solid State Lett. 8 (2005) G218-G221.
[10] Y.Z. Hu, R.J. Gutmann, T.P. Chow, Silicon nitride chemical mechanical polishing mechanisms, J. Electrochem. Soc. 145 (1998) 3919-3925.
[11] S. Kim, H. Sohn, U. Paik, T. Katoh, J. Park, A reverse selectivity ceria slurry for the damascene gate chemical mechanical planarization process, Jpn. J. Appl. Phys. 43 (2004) 7434.
[12] R. Manivannan, S. Ramanathan, The effect of hydrogen peroxide on polishing removal rate in CMP with various abrasives, Appl. Surf. Sci. 255 (2009) 3764-3768.
[13] S. Armini, C.M. Whelan, K. Maex, J.L. Hernandez, A.M. Moispour, Composite polymer-core silica-shell abrasive particles during oxide CMP: a defectivity study, J. Electrochem. Soc. 154 (2007) H667.
[14] Z. Zhang, L. Yu, W. Liu, Z. Song, Surface modification of ceria nanoparticles and their chemical mechanical polishing behavior on glass substrate, Appl. Surf. Sci. 256 (2010) 3856-3861.
[15] S. Patil, S.C. Kuiry, S. Seal, R. Vanfleet, Synthesis of nanocrystalline ceria particles for high temperature oxidation resistant coating, J. Nanopart. Res. 4 (2002) $433-438$.
[16] Y. Chen, R. Long, Polishing behavior of $\mathrm{PS} / \mathrm{CeO} 2$ hybrid microspheres with controlled shell thickness on silicon dioxide CMP, Appl. Surf. Sci. 257 (2011) 8679-8685.
[17] P. Dutta, S. Pal, M.S. Seehra, Y. Shi, E.M. Eyring, R.D. Ernst, Concentration of $\mathrm{Ce} 3+$ and oxygen vacancies in cerium oxide nanoparticles, Chem. Mater. 18 (2006) 5144-5146.
[18] L. Wang, K. Zhang, Z. Song, S. Feng, Ceria concentration effect on chemical mechanical polishing of optical glass, Appl. Surf. Sci. 253 (2007) 4951-4954.
[19] H. Doi, M. Suzuki, K. Kinuta, Effects of $\mathrm{Ce} 3+$ on removal rate of ceria slurries in chemical mechanical polishing for SiO2, in: International Confenrence on Planarization and CMP Technology International Confenrence on Planarization and CMP Technology, IEEE, 2014.
[20] S. Deshpande, S. Patil, S.V. Kochihhatla, S. Seal, Size dependency variation in lattice parameter and valency states in nanocrystalline cerium oxide, Appl. Phys. Lett. 87 (2005) 223-278.
[21] J.R. Mcbride, K.C. Hass, B.D. Poindexter, W.H. Weber, Raman and x-ray studies of Ce1-@ESeO2-y, where RE=La, Pr, Nd, Eu, Gd, and Th, J. Appl. Phys. 76 (1994) 2435-2441.
[22] S. Patil, S. Seal, Y. Guo, A. Schulte, Role of trivalent La and Nd dopants in lattice distortion and oxygen vacancy generation in cerium oxide nanoparticles, Appl. Phys. Lett. 88 (2006) 243110.
[23] Z. Yang, T.K. Woo, K. Hermansson, Effects of Zr doping on stoichiometric and reduced ceria: A first-principles study, J. Chem. Phys. 124 (2006) 224704.
[24] I. Uslu, A. Aytimur, M.K. Öztürk, S. Koçyigit, Synthesis and characterization of neodymium doped ceria nanocrystalline ceramic structures, Ceram. Int. 38 (2012) 4943-4951.
[25] S.R. Gillies, J. Bentley, C.B. Carter, Electron energy-loss spectroscopic study of the surface of ceria abrasives, Appl. Surf. Sci. 241 (2005) 61-67.

[26] T. Mori, J. Drennan, J. Lee, J. Li, T. Ikegami, Oxide ionic conductivity and microstructures of Sm-or La-doped CeO2-based systems, Solid State Ion. 154 (2002) 461-466.
[27] A.K. Lucid, P.R. Keating, J.P. Allen, G.W. Watson, Structure and reducibility of CeO2 doped with trivalent cations, J. Phys. Chem. C 120 (2016) 23430-23440.
[28] G. Kresse, J. Furthmüller, Efficient iterative schemes for ab initio total-energy calculations using a plane-wave basis set, Phys. Rev. B 54 (1996) 11169.
[29] G. Kresse, J. Furthmüller, Efficiency of ab-initio total energy calculations for metals and semiconductors using a plane-wave basis set, Compos. Mater. Sci. 6 (1996) $15-50$.
[30] P.E. Blöchl, Projector augmented-wave method, Phys. Rev. B 50 (1994) 17953.
[31] J.P. Perdew, K. Burke, M. Ernzerhof, Generalized gradient approximation made simple, Phys. Rev. Lett. 77 (1996) 3865.
[32] S.L. Dudarev, G.A. Botton, S.Y. Savrasov, C.J. Humphreys, A.P. Sutton, Electron-energy-loss spectra and the structural stability of nickel oxide: An LSDA + U study, Phys. Rev. B 57 (1998) 1505.
[33] P.R. Keating, D.O. Scanlon, B.J. Morgan, N.M. Galea, G.W. Watson, Analysis of intrinsic defects in CeO2 using a Koopmans-like GGA + U approach, J. Phys. Chem. C 116 (2012) 2443-2452.
[34] H.J. Monkhorst, J.D. Pack, Special points for Brillouin-zone integrations, Phys. Rev. B 13 (1976) 5188.
[35] Q. Song, B. He, Q. Yao, Z. Meng, C. Chen, Influence of diffusion on thermogravimetric analysis of carbon black oxidation, Energy Fuel 20 (2006) 1895-1900.
[36] Y. Liu, Y. Ding, L. Zhang, P. Gao, Y. Lei, CeO 2 nanofibers for in situ O 2 and CO sensing in harsh environments, RSC Adv. 2 (2012) 5193-5198.
[37] M. Dastpak, M. Farahmandjoo, T.P. Firoozabadi, Synthesis and preparation of magnetic Fe-doped CeO2 nanoparticles prepared by simple sol-gel method, J. Supercond. Nov. Magn. 29 (2016) 2925-2929.
[38] Y.Q. Jia, Crystal radii and effective ionic radii of the rare earth ions, J. Solid State Chem. 95 (1991) 184-187.
[39] S.J. Patwe, A.K. Tyagi, Solubility of Ce4+ and Sr2+ in the pyrochlore lattice of Gd22r207 for simulation of Pu and alkaline earth metal, Ceram. Int. 32 (2006) $545-548$.
[40] E. Wulloud, B. Delley, W. Schneider, Y. Baer, Spectroscopic evidence for localized and extended F-symmetry states in CeO2, Phys. Rev. Lett. 53 (1984) 202.
[41] Z. Yang, T.K. Woo, M. Baudin, K. Hermansson, Atomic and electronic structure of unreduced and reduced CeO 2 surfaces: A first-principles study, J. Chem. Phys. 120 (2004) 7741-7749.
[42] M. Nolan, S. Grigoleit, D.C. Sayle, S.C. Parker, G.W. Watson, Density functional theory studies of the structure and electronic structure of pure and defective low index surfaces of ceria, Surf. Sci. 576 (2005) 217-229.
[43] G.E. Murgida, V. Ferrari, M.V. Ganduglia-Pirovano, A.M. Llois, Ordering of oxygen vacancies and excess charge localization in bulk ceria: A DFT + U study, Phys. Rev. B 90 (2014) 115120.
[44] M. Nolan, S.C. Parker, G.W. Watson, The electronic structure of oxygen vacancy defects at the low index surfaces of ceria, Surf. Sci. 595 (2005) 223-232.

