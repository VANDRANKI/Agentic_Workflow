# SUNY POLYTECHNIC INSTITUTE 

MAXIMIZING THE CHEMICAL REMOVAL OF CERIA ABRASIVES IN CMP FOR

SILICON OXIDE AND METAL POLISHING

A Thesis
By
Christopher M. Netzband
Department of Nanoscale Science

Submitted in partial fulfillment of the requirements for the degree of
Doctor of Philosophy
Nanoscale Science

# SUNY POLYTECHNIC INSTITUTE 

The dissertation submitted by Christopher Netzband $\qquad$ under the title, "Maximizing the Chemical Removal of Ceria Abrasives in CMP for Silicon Oxide and Metal Polishing has been read by the undersigned. It is hereby recommended for acceptance to the Faculty of the University in partial fulfillment of the requirements for the degree of Doctor of Philosophy.

## Dissertation Committee Members

![img-0.jpeg](images\img-0.jpeg)

As chair of the student's dissertation committee, I confirm that all required edits have been made and the thesis document is accepted in final, approved condition.

## Rerelam 4 Bum

(Dissertation Committee Chair)
Date

Recommendation submitted on behalf of SUNY Polytechnic Colleges of Nanoscale Sciences and Engineering by:

## MMMMMMM

Dean of College, SUNY Polytechnic Institute

Date

## F. Shadi Shakedipour-Sandvik

Dean of Graduate Studies
SUNY Polytechnic Institute

#### Abstract

Cerium oxide or ceria has garnered a wide range of applications due to its redox active nature. This redox activity is due to oxygen vacancies on the surface of the ceria creating a layer of mixed oxide with the unstable oxide $\mathrm{Ce}_{2} \mathrm{O}_{3}\left(\mathrm{Ce}^{3+}\right)$ present at the same time as the bulk oxide $\mathrm{CeO}_{2}\left(\mathrm{Ce}^{4+}\right)$. Possible applications for ceria include water splitting, oxidation of carbon monoxide, oxidation of reactive oxygen species and polishing of glass films. In recent years, ceria nanoparticles have been used for polishing thermal silicon oxide during the early steps of semiconductor fabrication in a process referred to as chemical mechanical planarization (CMP). The advantage of these particles is their ability to abrade an oxide surface chemically using the aforementioned redox properties, as well as mechanically. To meet the needs of manufacturing, mainly removal rate and surface roughness, the particles used must have well controlled physical properties such as size and shape for mechanical removal and ratio of cerium oxidation state for chemical removal. This study encompasses three parts following the design of ceria slurries, their implementation in the existing silicon oxide polish and applying these findings to create novel slurries for polishing metals.


To design ceria slurry, the ratio of $\mathrm{Ce}^{3+} / \mathrm{Ce}^{4+}$ on the surface of abrasive was maximized by altering the slurries' chemical environment. Maximizing this ratio increases the proportion of active $\mathrm{Ce}^{3+}$ sites which participate in removal reactions. The effect of chemical environment on the $\mathrm{Ce}^{3+} / \mathrm{Ce}^{4+}$ ratio was determined through XPS analysis of the Ce 3d spectrum. The knowledge gained in this first section informed the design of ceria slurries for the following two parts to maximize their effectiveness. The second part of this thesis applies this knowledge to create ceria

slurries that polished thermal oxide with higher material removal rate (MRR) and lower postpolish roughness than slurries that are currently being used in industry. The basis of ceria polishing is known as the tooth-comb model. In this model oxygen at $\mathrm{Ce}^{3+}$ sites will undergo a condensation reaction with oxygen on the surface to be polished. As the particle leaves this will rip material off of the wafer surface. While the tooth-comb model was proposed for polishing silica, the final part of this thesis seeks to generalize it to encompass polishing any oxide given the correct conditions. To demonstrate this, I created ceria slurries to polish metals relevant to the semiconductor industry (copper, tungsten and ruthenium) with polishing metrics that equal or exceed those of industry standard slurries.

# Acknowledgements 

I would first like to extend a special thank you to my advisor, Dr. Kathleen Dunn, whose guidance and knowledge has helped me immensely throughout my time at SUNY Polytechnic Institute. Since the time I first joined her lab, she has taught me many things about materials science, metrology, technical writing and my future career path. Her help has had profound impacts on both me and my future and I can't thank her enough for all she has done. Thank you, Dr. Dunn.

I could not have completed this work without the help of the members of my group, Cu Club and fellow graduate students. Thank you, Kevin, Mami, Niaz, Jenny, Katie and Wilkie for both your assistance and more importantly, friendship during my time here. I would also like to thank Miguel, Steve, and the rest of the Metrology department for their support during my research.

I would also like to extend my appreciation to Dr.'s Carpenter, Thiel, Borst and Hatzistergos for accepting my invitation to be on my defense committee. I have a great deal of respect for you and for the work that you have done. Thank you for allowing me the opportunity of having you on my committee.

To my parents, Michael and Lila, and my brother Cody, thank you for your love and support throughout the years, I would not have accomplished a fraction of what I have today without

you. I will always be grateful for what you have done for me and will love you with all of my heart.

Finally, I would like to thank my wife Rachel. Your constant support, affection and encouragement has helped me become a better scientist and person. I cannot imagine what I would be like without you and I will love you for the rest of my life.

# Table of Contents 

Abstract ..... iii
Acknowledgements ..... v
Table of Contents ..... vii
List of Tables ..... x
List of Figures ..... xi
I. General Introduction ..... 1
A. Chemistry of Cerium ..... 1
B. Applications of Ceria ..... 5
C. Design of the Semiconductor CMP Process ..... 6
D. History of Semiconductor CMP ..... 18
E. Ceria CMP Removal Mechanism ..... 21
II. Characterization Methods ..... 29
A. Scanning Electron Microscopy ..... 29
B. X-Ray Photoelectron Spectroscopy ..... 31
C. pH ..... 36
D. Ellipsometry ..... 36
E. Atomic Force Microscopy ..... 37
F. Profilometry ..... 40
G. Mass Removal ..... 41

III. Design of Ceria Slurry for CMP Applications ..... 42
A. Introduction ..... 42

1. Determination of Chemical Effects with XPS ..... 45
B. Materials and Methods ..... 60
2. Materials ..... 60
3. Procedure ..... 60
C. Results and Discussion ..... 61
4. Effect of particle size ..... 61
5. Effect of pH ..... 64
6. Effect of peroxide ..... 66
7. Effect of surfactant ..... 70
D. Conclusions ..... 71
IV. Improved Ceria Slurry for Thermal Silicon Oxide Polishing ..... 72
A. Introduction ..... 72
B. Materials and Methods ..... 76
8. Materials ..... 76
9. Procedures ..... 77
C. Results and discussion ..... 82
10. Effect of peroxide ..... 82
11. Effect of pH ..... 84

3. Effect of particle size ..... 87
4. Effect of Surfactants ..... 89
5. Selectivity measurements ..... 92
D. Conclusions ..... 94
V. Improved Ceria Slurry for Metal Polishing ..... 95
A. Introduction ..... 95
B. Materials and Methods ..... 104
6. Materials ..... 104
7. Procedures ..... 105
C. Results and discussion ..... 106
8. Ruthenium polishing ..... 106
9. Tungsten polishing ..... 113
10. Copper polishing ..... 118
D. Conclusions ..... 123
VI. A Final Summary ..... 125
VII. References ..... 128

# List of Tables 

Table 3.1. Physical properties of ceria particles with different synthesis methods ..... 44
Table 3.2 List of peaks by binding energy and type. Colors ..... 48
Table 3.3 Chemicals used during ceria abrasive slurry trials ..... 60
Table 3.4 Average size and $\mathrm{Ce}^{3+} \%$ of as-received ceria powders ..... 64
Table 4.1 Chemicals used during ceria polishing experiments ..... 76
Table 5.1 Parameters for effective polishing through the tooth-comb mechanism ..... 101
Table 5.2 Chemicals used during metal polishing experiments ..... 104
Table 5.3 Hardness of different metal CMP materials using the common Mohs scale along with approximate Vickers scale values. ..... 115

# List of Figures 

Figure 1.1. Crystal structure for a) fluorite $\mathrm{CeO}_{2}$, b) hexagonal $\mathrm{Ce}_{2} \mathrm{O}_{3}$, c) monoclinic $\mathrm{Ce}_{2} \mathrm{O}_{3}$ and d) bixbyite $\mathrm{Ce}_{2} \mathrm{O}_{3}$ 2

Figure 1.2. Schematic of a CMP polishing setup, with major components labeled. $\qquad$ 7

Figure 1.3. a) Top-down and b) Cross-sectional Optical Images of a Chem-Pol ${ }^{\mathrm{TM}}$ polishing pad. 8
Figure 1.4. Schematic representation of the complex nature of CMP. $\qquad$ 9

Figure 1.5. SEM cross section a) of a type II pad (above line) with a type I subpad (below line) and b) a top down SEM image of the type II pore structure [32] $\qquad$ 11

Figure 1.6. SEM cross sections of a) a type III pad [30] and b) a type IV pad [36] $\qquad$ 12

Figure 1.7. Polishing pads before and after break-in $\qquad$ 13

Figure 1.8. Pad glazing followed by surface recovery due to conditioning. $\qquad$ 14

Figure 1.9. Diamonds of different a) size, b) depth, c) orientation and d) shape on a conditioner along with an e) SEM image of a conditioner pad [39] $\qquad$ 15

Figure 1.10. Optical images of diamonds placed on a conditioner pad in a) spiral [40] and b) ring patterns [41]. $\qquad$ 16

Figure 1.11. a) Optical image of a microreplicated diamond conditioner. b) SEM image of the cutting surface with a repeating pyramidal motif of ceramic that diamond is CVD coated onto. 17

Figure 1.12. 1997 SEM images of DRAM a) without and b) with CMP [55] $\qquad$ 20

Figure 1.13. Schematic representation of the mechanical polishing process in CMP. $\qquad$ 23

Figure 1.14 Filling of ceria oxygen vacancies in water. $\qquad$ 24

Figure 1.15. Schematic representation of the chemical polishing process of ceria in CMP. $\qquad$ 26

Figure 2.1. SEM images before a) and after b) image correction. $\qquad$ 30

Figure 2.2. Diagram of an XPS photoelectron emission $\qquad$ 32

Figure 2.3. Schematic of an XPS hemispherical detector ..... 34
Figure 2.4. Schematic of the ellipsometry process ..... 37
Figure 2.5. SEM image of the cantilever a) and tip b) of a Bruker TESPA-V2 AFM Probe [10]. ..... 39
Figure 3.1. Theoretical spectra of $\mathrm{Ce}^{4+}$ (blue) and $\mathrm{Ce}^{3+}$ (red) ..... 47
Figure 3.2. Diagram of cerium 3d orbital splitting in $\mathrm{Ce}^{4+}$ ..... 49
Figure 3.3. Schematic diagram of a shake-up energy transfer. ..... 51
Figure 3.4. Schematic diagram of the shake-off energy transfer ..... 52
Figure 3.5. Schematic diagrams of a shake-down electron transfer ..... 54
Figure 3.6. XPS spectra of the $\mathrm{CeO}_{2}$ film initially a) and after 2400 s etching b). ..... 55
Figure 3.7. The importance of realistic fitting in XPS analysis. a) Fitting a ceria peak without constraints and (b) with proper constraints ..... 58
Figure 3.8. SEM images of a) $\mathrm{Ce} 1(68 \mathrm{~nm})$ and b) $\mathrm{Ce} 2(20 \mathrm{~nm})$ at a magnification of 150 kx . The final image c) $\mathrm{Ce} 3(6 \mathrm{~nm})$ was obtained at a magnification of 450 kx . ..... 62
Figure 3.9. XPS analysis of as-received ceria abrasives a) $\mathrm{Ce1}$ b) $\mathrm{Ce} 2 \mathrm{c}$ ) $\mathrm{Ce} 3$ ..... 63
Figure 3.10. Effect of pH on the $\mathrm{Ce}^{3+}$ concentration of different ceria particles. ..... 65
Figure 3.11. Effect of $\mathrm{H}_{2} \mathrm{O}_{2}$ on the $\mathrm{Ce}^{3+}$ concentration of different ceria particles ..... 67
Figure 3.12. Catalase mimetic activity of ceria ..... 69
Figure 3.13. Effect of surfactants on the $\mathrm{Ce}^{3+}$ concentration both a) without $\mathrm{H}_{2} \mathrm{O}_{2}$ and b) with 0.5 wt. $\% \mathrm{H}_{2} \mathrm{O}_{2}$ at $0.5 \mathrm{wt} . \%$ surfactants ..... 71
Figure 4.1. SEM images [5], of "chatter mark" defects due to STI CMP ..... 73
Figure 4.2. Effect of $\mathrm{H}_{2} \mathrm{O}_{2}$ concentration on the a) MRR of ceria slurries and the b) post-polish oxide surface (Rz and RRMS) ..... 83

Figure 4.3. Effect of slurry pH on the a) MRR of ceria slurries and the b) post-polish oxide surface (Rz and RRMS) ..... 85
Figure 4.4. Optical images of the surface of a thermal oxide coupon post-polish with a) a pH 4 ceria slurry and b) a pH 8 ceria slurry. ..... 86
Figure 4.5. Effect of abrasive size on the a) MRR of ceria slurries and the b) post-polish oxide surface ( $\mathrm{R}_{\mathrm{Z}}$ and $\mathrm{R}_{\mathrm{RMS}}$ ) ..... 88
Figure 4.6. Effect of surfactant on the a) MRR of ceria slurries and the b) post-polish oxide surface (Rz and RRMS) ..... 90
Figure 4.7. Conceptual depiction of ceria particles (blue) covered in a) micellular or b) linear surfactants (orange) ..... 91
Figure 4.8. Comparison between the MRR of 68 nm ceria with 5 nm micellular surfactants to 80 nm silica. ..... 92
Figure 4.9. Effect of slurry improvements on the selectivity of oxide to nitride MRR ..... 93
Figure 5.1. Schematic representation of a metal CMP process ..... 97
Figure 5.2. a)\&d) SEM image of a copper wire that has undergone galvanic corrosion with STEM b) and EELS c) images of the interface. ..... 98
Figure 5.3. Schematic of metal CMP cycle ..... 100
Figure 5.4. SEM images of a) 68 nm ceria particles and b) a mix of 80 nm and 30 nm silica particles ..... 107
Figure 5.5. Performance comparison polishing ruthenium films with silica and ceria slurries having equal abrasive content by weight ..... 108
Figure 5.6. Effect of $\mathrm{H}_{2} \mathrm{O}_{2}$ on $\mathrm{Ce}^{3+} \%$ at different ceria concentrations ..... 109

Figure 5.7. Performance comparison polishing ruthenium films with $1.0 \mathrm{wt} . \%$ silica or ceria slurries having decreasing abrasive content. ..... 111
Figure 5.8. Performance comparison polishing ruthenium films using the reduced-concentration ( $0.1 \mathrm{wt} . \%$ ) ceria benchmark slurry or increasing concentration of silica abrasives ..... 112
Figure 5.9. Tungsten MRR using $1.0 \mathrm{wt} . \%$ ceria slurry at three different pH values: a) 4 , b) 2 and c) 1.8 ..... 114
Figure 5.10. Effect of abrasive concentrations on tungsten MRR at pH 1.8 ..... 116
Figure 5.11. Roughness of a tungsten foil after being polished by a) ceria or b) silica abrasives. ..... 117
Figure 5.12. Complexation of copper oxide with glycine. ..... 118
Figure 5.13. Passivation of a copper oxide surface with the inhibitor BTA. ..... 119
Figure 5.14. XPS analysis of slurry containing $1.0 \mathrm{wt} . \% \mathrm{CeO}_{2}$ and $0.5 \mathrm{wt} . \% \mathrm{H}_{2} \mathrm{O}_{2}$ both a) without and b) with the addition of 0.01 M BTA and glycine. ..... 120
Figure 5.15. Performance comparison of ceria and silica abrasives on the polishing of copper using the $\mathrm{H}_{2} \mathrm{O}_{2} /$ glycine/BTA system ..... 121
Figure 5.16. Performance metrics comparison for polishing of copper using only $\mathrm{H}_{2} \mathrm{O}_{2}$, without glycine and BTA ..... 122

# I. General Introduction 

## A. Chemistry of Cerium

Cerium is the most abundant lanthanide in the Earth's crust at 66 ppm [1]. Though it has almost equal abundance to copper [2], the average extraction per year for the former is $\sim 240,000 \mathrm{MT}$ whereas the latter is $>10$ million MT [3], [4]. One of the leading causes for low cerium extraction is the presence of radioactive materials, mainly radium and thorium, in the ore. Despite this low extracted quantity, cerium is a very useful element for many applications due to its unique electronic structure.

A key feature of lanthanides is the increase in binding energy of the 4 f orbitals above that of the 5 d and 6 s orbitals. This effect is minimal in cerium, with all three orbitals having similar energy [5]. The significance of this unique configuration can be most easily demonstrated by comparing the electronic structure of cerium, $[\mathrm{Xe}] 4 \mathrm{f}^{4} 5 \mathrm{~d}^{1} 6 \mathrm{~s}^{2}$, to that of the next lanthanide praseodymium, $[\mathrm{Xe}] 4 \mathrm{f}^{4} 6 \mathrm{~s}^{2}$. The $\mathrm{Pr}^{3+}$ state, $[\mathrm{Xe}] 4 \mathrm{f}^{2}$ is the only stable ionic form of Pr due to the strong binding of the remaining 4 f electrons. Cerium also contains a $3+$ ionic state, $\mathrm{Ce}^{3+}$, in the form $[\mathrm{Xe}] 4 \mathrm{f}^{4}$, but the lower binding energy of the 4 f state in cerium gives rise to a more stable ionic state, $\mathrm{Ce}^{4+}$ with the electron configuration $[\mathrm{Xe}] 4 \mathrm{f}^{0}$.

While most cerium compounds can be composed of only one of these two electronic states, cerium oxide, commonly called ceria, may contain either. Bulk ceria at room temperature is found in the $\mathrm{Ce}^{4+}$ state as the dioxide $\mathrm{CeO}_{2}$ with a fluorite crystal structure (fig. 1.1a). The less common $\mathrm{Ce}^{3+}$ state forms the sesquioxide $\mathrm{Ce}_{2} \mathrm{O}_{3} / \mathrm{CeO}_{1.5}$. The sesquioxide is pyrophoric at room temperature; as such, it does not occur naturally in a bulk form. The crystal structure of this

oxide can be hexagonal, monoclinic or bixbyite; with the latter being the most likely of the three (fig. 1.1b, c and d)[6].
![img-1.jpeg](images\img-1.jpeg)

Figure 1.1. Crystal structure for a) fluorite $\mathrm{CeO}_{2}$, b) hexagonal $\mathrm{Ce}_{2} \mathrm{O}_{3}$, c) monoclinic $\mathrm{Ce}_{2} \mathrm{O}_{3}$ and d) bixbyite $\mathrm{Ce}_{2} \mathrm{O}_{3}$. Ceria can switch between the fluorite and bixbyite structures by creating or filling oxygen vacancies. Oxygen and cerium are represented by red spheres and yellow spheres respectively. All structures visualized using the software VESTA[7].

The existence of a monoclinic structure of $\mathrm{Ce}_{2} \mathrm{O}_{3}$ is purely based on theoretical calculations and has never been observed experimentally. Both the hexagonal and bixbyite structures can be formed upon heating, while only the bixbyite structure can be produced at room temperature.

This room temperature formation arises from the relation between the bixbyite and fluorite crystal structures. A bixbyite unit cell is composed of a cube of eight fluorite unit cells where each cell has lost $1 / 4$ of their anionic interstitial atoms, in this case oxygen. The bonds subsequently rearrange to accommodate these vacancies resulting in an expansion of the original fluorite lattice by $4-9 \%$.

Consequently, the bixbyite $\mathrm{Ce}_{2} \mathrm{O}_{3} / \mathrm{CeO}_{1.5}$ is equivalent to $\mathrm{CeO}_{2}$ with oxygen vacancies (which occur naturally due to entropic considerations). Assuming oxygen vacancies at the surface of ceria will create a mixed oxide of $\mathrm{CeO}_{2-\mathrm{x}}$ with $0<\mathrm{x}<0.5$, the measured change in lattice volume as the dioxide $(\mathrm{x}=0)$ is converted to a sesquioxide $(\mathrm{x}=0.5)$ is $\sim 7 \%$ [8]. This expansion matches the $4-9 \%$ volume expansion corresponding to a structural change from fluorite to bixbyite as opposed to a change from fluorite to hexagonal, which results in no expansion of the lattice [6]. Thermodynamically, the pure dioxide cannot exist in nature because these surface defects create areas of mixed oxidation state. Chemical reactions between ceria and other materials occur at these oxygen vacancy sites. While the total number of vacancy sites is difficult to calculate, the ratio of $\mathrm{Ce}^{3+}$ to $\mathrm{Ce}^{4+}\left(\mathrm{Ce}^{3+}\right.$ \%) is easier to determine experimentally and can be used to compare the reactivity of different ceria samples. A ceria sample with a higher $\mathrm{Ce}^{3+} \%$ will have more oxygen vacancies and be more reactive.

The oxidation state of cerium and the associated vacancy concentration in a ceria sample depends on crystallinity and particle size, and can be can be increased or decreased through redox chemistry [9]. Ceria crystallinity is determined by the synthesis conditions, with higher synthesis temperatures resulting in more crystalline material [10]. This highly crystalline ceria

will have fewer defects and oxygen vacancies on its surface and therefore a lower $\mathrm{Ce}^{3+} \%$. The effect of particle size is closely related to the stress on the particle surface. This surface stress is greater for smaller particles, and can be relieved through the formation of oxygen vacancies. As a result, the $\mathrm{Ce}^{3+} \%$ on the surface of a small particle is greater than that of a large particle [11]. This property only becomes noticeable when the particles are $<100 \mathrm{~nm}$ in diameter.

Since both chemical and physical characteristics of ceria are linked to the particle size, it is convenient to discuss these properties by sorting the ceria into three distinct size groups. The largest particles, calcined ceria, are created by subjecting cerium compounds to high temperatures in oxygen [10]. During a typical ceria calcination, a micrometer sized cerium precursor such as cerium carbonate is baked at temperatures up to $1000^{\circ} \mathrm{C}$. At this stage, the ceria particles can range in size from multiple microns down to hundreds of nanometers. Following synthesis, the particles are crushed, dispersed in a solution and filtered to obtain multiple narrow size distribution batches within the range given above. The particles range from 1000 down to 250 nm in diameter with a highly faceted surface.

The next two classifications of particles are synthesized through various wet chemical methods. Colloidal ceria particles range in size from 250 to 10 nm , while particles below 10 nm are referred to as nanoceria regardless of the preparation method [12]. The size and properties of synthesized particles in wet chemical methods can be affected by many factors such as temperature [13], pH [14], concentration [15] and additives [16].

After synthesis, ceria can interact with reducing or oxidizing agents to change between its $\mathrm{Ce}^{4+}$ and $\mathrm{Ce}^{3+}$ states following equation $1.1[17]$.

$$
C e^{4+}+e^{-} \leftrightarrow C e^{3+} E^{\circ}=+1.61
$$

As this conversion occurs, the change in oxidation state causes an expansion in the lattice at the ceria surface. To accommodate this expansion more oxygen vacancies form, creating more active sites for chemical reactions.

# B. Applications of Ceria 

The first recorded use of ceria was in 1891 by Carl Auer von Welsbach [18], when its redox properties were harnessed to catalyze the combustion of thorium oxide in gas mantles. In the years following 1891, the consumption of thorium rose significantly. Due to the greater abundance of cerium than thorium in lanthanide ore, there was a large unused supply of cerium that many inventors attempted to create new applications for [5]. One such application was the creation of better lighter flints by mixing cerium with iron to form the material ferrocerium [19]. An improved version of this material, mischmetal, was created by adding magnesium and other lanthanides and is still used today as a lighter flint [20].

In the 1930's the Royal Astronomical Society of Vancouver reported the use of a paste containing ground ceria as the abrasive for polishing glass telescope lenses [21]. This "optician's rouge" replaced the more common iron and zinc oxides, "jeweler's rouge", used at the time due to the production of a smoother finish and faster polishing rate. Ceria has also found an application in the automobile industry. The Clean Air Act of 1970 led to the invention of

catalytic converters to reduce carbon and nitrogen oxide generation [22]. A typical catalytic converter contains platinum group metals deposited onto a honeycomb aluminum scaffold to increase the surface area of the catalytic metal. In the 1980's ceria particles were imbedded onto surface of the platinum group metals to both improve the breakdown of oxides and store or release oxygen to increase the efficiency of catalysis [23]. More recently, ceria's interconvertibility (equation 1.1) has been researched for use in fuel cells [24], water splitting [25] and biomedical applications as an antioxidant [26], [27]. The most common use of ceria today is in the polishing of silicon oxides during the shallow trench isolation (STI) step of semiconductor manufacturing [28]. This polishing is referred to as chemical mechanical planarization/polishing (CMP) and is a natural extension of ceria's use as "optician's rouge" discussed previously.

# C. Design of the Semiconductor CMP Process 

CMP, detailed in figure 1.2, is a technique whereby irregular surfaces of a wafer due to depositions are polished to a flat surface to ease the deposition of subsequent material.

![img-2.jpeg](images\img-2.jpeg)

Figure 1.2. Schematic of a CMP polishing setup, with major components labeled. See text for detailed description of operation.

In this technique a wafer (blue) is held by a polishing head and pressed against a urethane pad (grey speckled fill). Both the head and the platen on which the pad is mounted are rotating while the head oscillates along the radius of the platen. During polishing a solution containing various chemicals and small particles called a slurry is fed onto the pad. The particles act as abrasives to mechanically remove material. The chemicals change the structure or composition of the wafer surface to either chemically remove material directly or make mechanical material removal easier [29]. These are respectively, the chemical and mechanical removal aspects of CMP. The polishing pad has holes of different sizes and shapes to maintain uniform pressure and improve slurry retention time (fig. 1.3) [30]. These structures are maintained throughout the polishing process by pressing a conditioner (brown speckled fill) made of sinter diamonds onto the pad surface.

![img-3.jpeg](images\img-3.jpeg)

Figure 1.3. a) Top-down and b) Cross-sectional Optical Images of a Chem-Pol ${ }^{\mathrm{TM}}$ polishing pad. Images provided by the manufacturer [31]. The surface of this polishing pad has large, deep, ellipsoidal holes at the surface under which is a series of smaller spherical micropores.

The topic of this thesis is the design of CMP slurries to improve polishing, but there are many other factors that must be taken into account when designing a CMP process (fig. 1.4).

![img-4.jpeg](images\img-4.jpeg)

Figure 1.4. Schematic representation of the complex nature of CMP. Due to the interconnected nature of CMP properties, accurate model of the process is nearly impossible. Blue boxes indicate properties that can be controlled by the user while green boxes are those that are not controlled directly. Arrows show how the properties are related with the direction of the arrow mirroring the direction of effect.

More than half of these factors can be controlled by the user. Within the user's control are the instrument settings, the choice of polishing pad, the use of a conditioner, and the slurry design. The instrument settings include oscillation speed, rotation speed, downforce and contact area. As the oscillation and rotational speeds increase, polishing speed increases, and slurry retention time decreases. Downforce and contact area are inversely related. They affect removal rate and roughness through their relationship with pressure (equation 1.2).

$$
p=\frac{F}{A}
$$

Both the feed rate of the slurry and the platen temperature can be controlled, but the properties they affect are very interrelated and it is therefore much harder to determine their impact.

Moving to the effect of polishing pads on CMP, there are four different types of polishing pads to choose from. Type I pads are made of polyester felts impregnated with polyurethane [32]. This pad material is ineffective at polishing and is instead used as the backing material or subpad for other pad types (figure 1.5a). Type II pads are made of a material known as poromeric [32]. This material is similar to the type I pad but the impregnation is performed on polyester fabric instead of felt. Poromeric is more commonly used as artificial leather for shoes [33]. The first polishing pads used in the semiconductor industry were made of real leather [34]. Type II pads are the pads of choice for final polishing due to their soft nature and large open pore structure (figure 1.5). These pads have a low polishing rate but result in a much lower defect count than the harder pad types.

![img-5.jpeg](images\img-5.jpeg)

Figure 1.5. SEM cross section a) of a type II pad (above line) with a type I subpad (below line) and b) a top down SEM image of the type II pore structure [32]. Type II pads are characterized by large, deep, vertical pores on a bed of uniform micropores. End of life of these pads occurs when the micropores are fully exposed.

Once the large pores have been worn away, the polishing properties of the pad changes as the underlying micropores are exposed. This change in polishing is undesirable and reversing it is a major factor in the short lifetime of type II pads [35].

The final two pad types, III and IV, are both hard pads made of polymer sheets [36]. A type III pad has a filler of either small abrasives or voids to make it porous while a type IV pad is solid (figure 1.6).

![img-6.jpeg](images\img-6.jpeg)

Figure 1.6. SEM cross sections of a) a type III pad [30] and b) a type IV pad [36]. End of life for these pads occurs when the polymer sheet has been fully removed.

These pads have long lifetimes and can withstand high pressure. This allows them to achieve high material removal at the expense of creating many defects during polishing. The type III pad is the most commonly used pad for CMP with the Dow ${ }^{\circledR}$ IC1000 ${ }^{\mathrm{TM}}$ type III pad being the most commonly used polishing pad for all levels of CMP since its invention in 1998 [37].

The third controllable property is the extent of conditioning. A conditioner is a disk whose surface is coated in small diamonds that are attached through sintering [35]. By pressing this disk onto a rotating pad, it mechanically abrades the pad surface and recovers the surface qualities needed for proper CMP. The conditioning process encompasses conditioning time, pressure and conditioner design. The pressure necessary to condition a pad is determined by pad type with softer pads requiring less pressure than harder ones. Conditioning time can be broken down into two stages. When a pad is first placed onto the platen, the pores are encased in a film that must be removed through an initial break-in conditioning step (fig. 1.7). This film creates unintended

asperities on the pad that can cause excess defects on the wafer surface during polishing along with non-uniform material removal as they are worn away.
![img-7.jpeg](images\img-7.jpeg)

Figure 1.7. Polishing pads before and after break-in. By removing the film covering the pores, the polishing properties become more uniform during the beginning of pad life.

After this initial break-in, conditioning downforce and rotation are set to minimize occlusion of foreign material in, and glazing of the polishing pad [38]. These foreign materials include both wafer debris and slurry abrasive. As these materials build up in the pores, the removal in that area becomes nonuniform and defect prone. This leads to an artificial decrease in the lifetime of the pad. By etching the pad with a conditioner this material can be dislodged, leading to a recovery of the initial polishing characteristics. Glazing is a term that refers to a loss of structure and change in the surface properties of the pad. Glazing occurs when the flat wafer "polishes" the pad (fig. 1.8).

![img-8.jpeg](images\img-8.jpeg)

Figure 1.8. Pad glazing followed by surface recovery due to conditioning. Conditioning to maintain an effective polishing surface is the leading cause of pad wear during operation.

While glazing and material occlusion can decrease the useful lifetime of a pad, they have little effect on its physical wear. The removal of pad material by a conditioner to recover the initial surface seen in figure 1.8 is the source of this physical wear. To minimize wear, the degree of glazing during polishing needs to be constantly measured to ensure a good surface can be maintained without over conditioning and reducing pad lifetime.

The final parameter for conditioning is the design of the conditioner (fig. 1.9). Early conditioning disks used diamonds of varying sizes imbedded in electroplated nickel, leading to nonuniformity in the conditioning process. This non-uniformity gave the technician the undesirable choice between not fully removing the glazed layer or over-conditioning some spots leading to decreased pad lifetime.

![img-9.jpeg](images\img-9.jpeg)

Figure 1.9. Diamonds of different a) size, b) depth, c) orientation and d) shape on a conditioner along with an e) SEM image of a conditioner pad [39]. The characteristics of each diamond and its placement results in non-uniform conditioning of the pad surface with most conditioning occurring at a small number of highly exposed diamonds.

While improvements in size selection have eliminated this problem, scaling to smaller sizes means that sources of non-uniformity that were previously unimportant must be addressed. When the diamonds are all of the same size, differences in shape and the depth they sink into the Ni brazing matrix during the brazing process become important factors to control. With a small number of protruding diamonds, the cut rate is initially high but non-uniform. As these diamonds wear other diamonds can come in contact with the pad. This increases the uniformity of conditioning but decrease the cut rate due to the load being shared across a greater surface area.

Instead of being randomly arranged across the surface of the conditioner, diamonds may be embedded in patterns containing recessed channels between the areas with diamonds to improve flow of the slurry on the polishing pad (fig. 1.10a) or by placing the diamonds at the same distance from the center of the conditioner to ensure more uniform conditioning (fig. 1.10b). The

latter arrangement ensures that each diamond has the same angular momentum and consequently the same relative velocity in respect to the polishing pad.
![img-10.jpeg](images\img-10.jpeg)

Figure 1.10. Optical images of diamonds placed on a conditioner pad in a) spiral [40] and b) ring patterns [41]. Controlling the placement of diamonds on the conditioner can improve slurry flow and make conditioning more uniform.

To further improve conditioning, many companies are shifting to patterned ceramic structures with a layer of CVD diamond over the top. This new design is known as a microreplicated diamond conditioner [42]. These conditioners ensure that the cutting edge is evenly shared across all "diamonds" and can be engineered with specific cutting surface arrangements to improve function (fig. 1.11).

![img-11.jpeg](images\img-11.jpeg)

Figure 1.11. a) Optical image of a microreplicated diamond conditioner. b) SEM image of the cutting surface with a repeating pyramidal motif of ceramic that diamond is CVD coated onto. Images are of the 3M ${ }^{\text {TM }}$ Trizact ${ }^{\text {TM }}$ B5-M990-5S2 Pad Conditioner [43].

The final property of CMP that can be controlled is the design of the slurry, which is tailored to the material being polished. For example, the CMP of many metals simply requires the use of an oxidizing agent to chemically convert the surface to a weaker oxide to ease mechanical removal by abrasives [44]. Copper, however, requires additional chemicals to complex the copper oxide and achieve high removal while the mechanical aspect is focused on ensuring low surface roughness $[45]$.

After the chemistry is determined, the abrasive characteristics must be chosen. The three main abrasives for CMP are ceria, silica and alumina [46]. Silica is the most popular abrasive due to its low cost. The second most popular abrasive is ceria. Even with its higher cost, ceria greatly outperforms silica for polishing silicon oxide and so it is the primary abrasive used in critical polishing steps. Finally, alumina is used when a hard particle is necessary to achieve high

material removal. Though CMP is well established component of semiconductor manufacturing, its adoption by the semiconductor community did not come easily.

# D. History of Semiconductor CMP 

The following history of semiconductor CMP is condensed from multiple sources [28], [47][51]. In 1997 Gordon Moore was interviewed about the improvements in semiconductor processing. During this interview he stated that the most important technique for adding more layers to a semiconductor was CMP [52]. The usefulness of CMP was not realized by the semiconductor community initially, and such a "dirty" procedure was not considered for surface roughness improvements during fabrication. This relegated CMP in the semiconductor field to the preparation of bare silicon wafers until 1983. Klaus Beyer, at this time working for IBM, discovered that STI silicon oxide could be polished by CMP to create a uniform surface around the active regions [53]. In STI the transistors are contained in isolated active regions and separated by regions of silicon oxide. Unfortunately, the silicon oxide could not be created with a low enough stress to be viable in manufacturing and STI was not introduced in a product at that time.

This shifted focus for CMP of silica from the transistors in the front end of the line (FEOL) to the dielectric in the back end of the line (BEOL). The BEOL contains metal lines, at that time made of aluminum, that connect transistors on the chip to the rest of the device, and ultimately to the outside world. To ensure there is no interaction between metal lines they are separated by a dielectric known as the inter layer(metal) dielectric (ILD). As multi-level interconnect schemes became common, it became necessary to ensure planar surfaces for the subsequent lithographic

steps to maintain in-focus patterning. Previous planarization schemes such as etch-back were no longer sufficient for this goal, and CMP was reconsidered for the dielectric.

A few years later, tungsten vias were introduced in between the transistors and the first metal level. Though ILD CMP worked well to planarize the dielectric between pre-existing aluminum lines, the order of these steps is reversed for a via. That is, the dielectric is deposited first and planarized before via holes are etched into it, and the tungsten deposited last by CVD. Therefore, any scratches in the ILD post-CMP became filled with the CVD tungsten, causing electrical shorts. To remedy this, tungsten CMP was developed between 1987-1988. This research lead to the production of both ILD and W CMP by 1990. The first high volume commercial device created while employing CMP came in 1993 with the original Pentium ${ }^{\circledR}$ microprocessor.

By this point, advances in the field of electron cyclotron resonance plasma sources had allowed for the creation of low stress $\mathrm{SiO}_{2}$ films [54]. With these films, the earlier proposed STI structure could be realized. To polish these films, the STI CMP that was developed by Klaus Beyer a decade prior was used. However, the fumed silica particles used in ILD CMP and W CMP left scratches that were large enough to ruin the isolating properties of the STI layer. To remedy this, slurries using colloidal silica were developed. STI CMP was introduced and adopted by semiconductor manufacturers worldwide by 1997 (fig 1.12).

![img-12.jpeg](images\img-12.jpeg)

Figure 1.12. 1997 SEM images of DRAM a) without and b) with CMP [55]. The introduction of CMP stopped the proliferation of surface roughness and allowed for the creation of devices with more layers and smaller size.

Two years later, IBM announced their dual damascene copper interconnect as a replacement to the Al line/ W via interconnect to address the challenges of moving to smaller line sizes. This replacement would be completed by 2001. The new architecture introduced an additional Cu CMP process to flatten the damascene lines while keeping the tungsten plug between the FEOL and the BEOL.

As devices continued to scale, new materials were introduced which had their own unique CMP challenges. By 2005 and the introduction of the 65 nm node, the scratches left by colloidal silica on $\mathrm{SiO}_{2}$ films were now too large and improvements to the abrasive had to be made. Within a year, STI CMP had converted to using calcined ceria abrasives in the place of colloidal silica due to the lower number of scratches and higher removal rate that was reported during glass lens polishing almost 80 years prior. Further scaling has resulted in changes to the ceria particles from calcined to colloidal to nano ceria in the same way manufacturers had changed from fumed to

colloidal silica. Each successive generation of smaller particles has resulted in longer polishing times but smoother surfaces.

# E. Ceria CMP Removal Mechanism 

The difference between the removal rates and scratch density/ depth of silica and ceria can be attributed to the unique properties of ceria's mixed oxidation state discussed previously, which enable a different mechanism for material removal than in silica CMP [56]. To explain this difference, it is first necessary to discuss the mechanism by which 'traditional' silica particles remove material during CMP. In the following explanations and diagrams, the silicon oxide surface is depicted as a lattice for ease of viewing, but can be understood to be the glassy network typical of silica surfaces.

During silicon oxide polishing with silica particles, the primary method of material removal is mechanical. As the particle approaches the wafer surface, the local pressure and temperature increase, allowing molecules of water to be forced into the lattice (fig. 1.13a). Under these elevated conditions the water will hydrolyze the bonds between silicon and oxygen (equation 1.3, fig. 1.13b).

$$
H_{2} O+S i-O-S i \leftrightarrow S i-O H+S i-O H
$$

As the particle leaves, the pressure and temperature will return to normal conditions and the hydrolyzed bond condenses (fig. 1.13c) but the water remains inside the lattice (equation 1.3

reverse, fig. 1.13d). As this process repeats, the number of water molecules incorporated and consequently $\mathrm{Si}-\mathrm{O}$ bonds broken continues to increase (fig. 1.13e) until a silicate is formed. This silicate has no remaining surface bonds and if it is large enough, will be carried away from the surface by the turbulent flow of the slurry across the pad before the bonds can reform (fig. 1.13f). This process continues to repeat itself until the polishing is complete.

![img-13.jpeg](images\img-13.jpeg)

Figure 1.13. Schematic representation of the mechanical polishing process in CMP. The steps for this process are a) water incorporation, b) hydrolysis and c) condensation leaving water inside the lattice d). After e) repeated impacts, silicates can f) be removed from the oxide surface between steps b and c .

The removal process with ceria involves a few more steps than with silica and has a much higher removal rate. This increased removal rate is due to the addition of a chemical removal mechanism at the particle surface along with the mechanical removal mechanism present with silica slurries. The chemical removal of oxides with ceria was first described in 1990 by Cook [57]. Since then his mechanism known as the "tooth-comb model" has been further expanded but remains the most agreed upon explanation for ceria chemical removal. In this model, the $\mathrm{Ce}^{3+}$ sites at the particle surface will contain surface oxygen vacancies. When dispersed in water these vacancies can be filled by an $\mathrm{H}_{2} \mathrm{O}$ molecule resulting in a surface hydroxyl group (fig. 1.14).
![img-14.jpeg](images\img-14.jpeg)

Figure 1.14 Filling of ceria oxygen vacancies in water. This $\mathrm{Ce}-\mathrm{OH}$ site becomes an active site for chemical reactions between ceria and other materials. Structures visualized using VESTA [7].

As a ceria particle approaches the oxide surface, the water incorporation and hydrolysis described in the mechanical process will occur along with an additional chemical reaction. The increased temperature and pressure will induce the condensation of ceria's hydroxyl groups with oxygen on the silicon oxide wafer. This forms a bond between the particle and the oxide surface (equation 1.4 and 1.5 , fig. 1.15a).

$$
\begin{gathered}
S i-O^{-}+C e-O H \rightarrow S i-O-C e+O H^{-} \\
S i-O H+C e-O H_{2}^{+} \rightarrow S i-O-C e+H_{3} O^{+}
\end{gathered}
$$

The pathway that this condensation follows is based on the pH of the slurry. If the slurry is basic $(\mathrm{pH}=8)$, the ceria will be neutral and the wafer will be negatively charged resulting in the condensation reaction of equation 1.4. Conversely, if the slurry is highly acidic $(\mathrm{pH}=2)$, the ceria will be positively charged and the wafer will be neutral resulting in the condensation reaction of equation 1.5 .

As the particle leaves, this bond is stressed and breaks (fig. 1.15b and c). With subsequent impacts the bonds between a silicate and the surface will be broken, allowing the ceria to remove this silicate through the condensed bond. With equivalent bond strengths between oxygen and silicon or oxygen and cerium, $8.18 \mathrm{eV} /$ bond for $\mathrm{Si}-\mathrm{O}$ and $8.24 \mathrm{eV} /$ bond for $\mathrm{Ce}-\mathrm{O}$, this removal also has a chance to occur when there is one remaining bond between the silicate and the surface (fig. 1.15d) [58]. Since this chemical removal is not size dependent, it happens more frequently than the mechanical removal and material is removed more rapidly than in the purely mechanical case.

![img-15.jpeg](images\img-15.jpeg)

Figure 1.15. Schematic representation of the chemical polishing process of ceria in CMP. The steps for this process are a) condensation of surface oxygen containing groups, b) bond stress as the particle leaves with stressed bonds denoted in red and c) bond cleavage followed by silicate removal. When bonds on both sides of the silicate are broken it can either be removed or condense onto the oxide surface d).

Proof for this polishing mechanism also comes from the strong attachment of ceria particles to the wafer surface post-polish [59]. These particles are very hard to remove from the wafer surface and a post-polish clean needs to be performed with chemicals that can undercut the $\mathrm{Ce}-\mathrm{O}-\mathrm{Si}$ bond while also preventing rebonding to the wafer surface [60]. Further confirmation is given by investigating the amount of free $\mathrm{Ce}^{3+}$ ions in the slurry post-polish [61]. During polishing it is possible based on the geometry of the particle and the number of remaining

surface bonds on the wafer that a $\mathrm{Ce}^{3+}$ site will be removed from the particle surface. This would result in more $\mathrm{Ce}^{3+}$ ions in solution and has been widely reported.

These experiments in support of the tooth-comb model are only indirect measures, however. The first type used X-ray photoelectron spectroscopy (XPS), a surface sensitive technique, to investigate the wafer post-polish instead of using it to probe the surface of the particles themselves [59], [62], [63]. The second relies on UV-Vis spectroscopy, which measures free $\mathrm{Ce}^{3+}$ ions in solution and not the $\mathrm{Ce}^{3+}$ sites on the surface of the particle [61], [62], [64]. Lacking direct experimental documentation of the particle surface, the conclusions about the tooth-comb model are mere inferences.

While the effect of physical parameters on $\mathrm{Ce}^{3+} \%$ is well documented, the effect of the slurry chemical environment on the particle is less so. Here again, the literature on the effect of chemical environment bases their conclusions on UV-Vis or XPS of the wafer surface postpolishing and assumes this corresponds to changes occurring at the particle surface [65]. A further complication is that many sources base their conclusions on their polishing results and work backwards to infer the removal mechanism, rather than studying what is happening to the particle and working forward.

My approach to remedy these gaps in the field starts with directly probing the ceria particles themselves through XPS. This work directly measures the effects of chemical environment on $\mathrm{Ce}^{3+} \%$. By combining my results with previous literature on the effect of physical parameters and particle-oxide interactions, a more complete understanding of chemical removal by ceria is

reached. I then apply this new understanding to design slurries with improved removal characteristics which could enable the extension of ceria slurries beyond their traditional use in polishing silicon oxide to planarize other materials in semiconductor process flow, including metals.

Having laid out a history of ceria CMP and the basic principles involved, the remainder of the thesis is organized to support the preceding assertions. The following chapter describes the methods used to address these questions regarding chemical environment and also determines the efficacy of my polishing experiments. Chapter 3 introduces my experiments on the effect of slurry chemical environment on $\mathrm{Ce}^{3+} \%$. Chapter 4 details the polishing of thermal silicon oxide with ceria and acts as a confirmation of my new understanding of chemical environment outlined in chapter 3. Based on the changes made to ceria slurries in chapter 3, I am able to use ceria to polish metals. The final chapter 5 presents novel polishing targets for ceria slurry in the form of ruthenium, tungsten and copper.

# II. Characterization Methods 

## A. Scanning Electron Microscopy

Direct visualization of the particles used for polishing was accomplished using a Zeiss LEO1550 Schottky-type field emission scanning electron microscope (FE-SEM). Images obtained varied in magnification from 150000x to 450000x at 2-3 keV and 4 mm working distance. The image is created by impacting the surface of a sample with an electron beam that scans across its surface [66]. As a result of this impact, low energy ( $<100 \mathrm{eV}$ ) "secondary electrons" are emitted. At this short working distance, the sample is inside the magnetic field of the final lens and the electrons are draw back into the lens. Inside the lens there is a detector, called an immersion or in-lens detector, with an applied bias that the secondary electrons are accelerated towards. These electrons will impact the detector scintillator creating photons that are guided into a photomultiplier to create a detectable signal.

As the beam is scanned across the sample, the detected intensity at each point is assigned a gray scale value. The scan of the electron beam is synchronized with the computer display, and an image is built up by plotting the grayscale intensity at each pixel. To avoid charge buildup on the surface of the particles two methods were used. The first method was to image using an electron beam with a low accelerating voltage. While this reduces charging, it also reduces the resolution of the image. To minimize this loss of resolution, the SEM used was outfitted with a beam booster inside of the microscope column. A beam booster will send an electron beam of higher energy through the column (promoting tighter beam diameter and less scattering) and lower the energy of the beam to the desired level before it leaves. This reduces the distance travelled at low beam energies and therefore reduces the scattering induced by collisions with residual gas

molecules within the vacuum chamber. While using low beam energies is helpful to reduce charging, the long capture times needed to minimize noise in the image still causes a buildup of electrons on the sample surface. To address this, the complementary technique of frame averaging was used. This technique images over a short capture time and reduces noise by averaging many captures together into a composite image. For this purpose, twenty images were captured at a rate of 1 per second over a time span of 20 seconds.

Images of these particles were analyzed using the image processing program ImageJ [67]. Before analysis the edges of the particles were sharpened by setting the gamma to 2 and adjusting the brightness and contrast manually (fig. 2.1).
![img-16.jpeg](images\img-16.jpeg)

Figure 2.1. SEM images before a) and after b) image correction to sharpen particle edges for further processing and analysis.

After correction, all of the dark areas of the image were excluded through automated thresholding to avoid user bias and increase reproducibility. The program was then used to detect

the outline of every particle in the image and a particle size distribution was extracted. Assuming a single distribution, data points were rejected if their size was $<10 \%$ or $>190 \%$ of the average particle size given by the manufacturer. If the sample was multi-modal then lower and upper cutoffs were applied to the smallest and largest particles sizes respectively. Using the resulting distributions, the average particle size of each slurry was determined.

# B. X-Ray Photoelectron Spectroscopy 

The ratio of $\mathrm{Ce}^{3+} / \mathrm{Ce}^{4+}$ on the abrasive surface was determined through the use of a Thermo Scientific ${ }^{\mathrm{TM}}$ ThetaProbe angle resolved x-ray photoelectron spectrometer (ARXPS). Cerium 3d spectra were acquired using a 0.05 eV step size, 50 eV pass energy, 50 ms dwell time and averaged over 40 scans. XPS exploits the photoelectric effect, using an X-ray of a known energy $(h \nu)$ as the probing radiation [68]. This travels through the sample until it impacts an atom (fig. 2.2).

![img-17.jpeg](images\img-17.jpeg)

Figure 2.2. Diagram of an XPS photoelectron emission. An incident X-ray transfers energy to a bound electron from the K shell, which is ejected, leaving a hole (open circle) behind.

As a result of this absorption, energy is transferred from the X-ray to an electron bound to the molecule with a certain energy $\left(E_{B}\right)$ determined by its orbital position. If there is enough energy transferred to overcome the binding energy of the electron, the particle will be ejected and the kinetic energy $\left(E_{K}\right)$ of the particle will be measured. This $E_{K}$ is a combination of the true kinetic energy $\left(E_{K}^{\prime}\right)$ and the work function of the sample $\left(\phi_{S}\right)$ shown in equation 2.1. Since this work function is unknown and varies between samples, it is more practical to ignore its effect and base all calculations off of the measured kinetic energy. Using this $E_{K}$ and the $h v, E_{B}$ can be determined from equation 2.2:

$$
\begin{gathered}
E_{K}=E_{K}^{\prime}-\phi_{S} \\
E_{K}=h v-E_{B}-\phi_{D}
\end{gathered}
$$

Equation 2.1
Equation 2.2

Where $\phi_{D}$ is the work function of the detector. As the sample is irradiated, electrons are ejected concurrently across the entire allowable energy range of $0<E_{K}<\left(h v-\phi_{D}\right)$, but measurements must be made over a much smaller range of energies, a step, due to the operation of the detector. When making measurements, the measured $E_{K}$ and the $E_{K}$ of the electron as it hits the detector will be different values. These measurements are a two-step process where the electrons are first focused through a series of electrostatic or magnetic lenses while their kinetic energy is retarded [69] and then the lower energy electrons impact the detector. When measuring a step in the spectrum, the retardation $(R)$ brings electrons of that $E_{K}$ to a chosen energy known as the pass energy $\left(E_{P}\right)$. For example, when measuring the electron count at $E_{K}=500 \mathrm{eV}$ with an $E_{P}=50 \mathrm{eV}$, electrons entering the detector will be retarded by the same magnitude of $R=450 \mathrm{eV}$. Following this, the electrons enter a hemispherical detector. This detector has an electrostatic field applied across the inner and outer hemispheres. Electrons with $E_{K}$ not equal to $E_{P}$ will not be able to travel the length of the detector without impacting the walls. After detection, the instrument software will compensate the detected kinetic energy with the known retarding energy to recover the $E_{K}$ of the electrons (equation 2.3). Adding this to equation 2.2 , the equation used by the instrument to determine binding energy becomes equation 2.4 .

$$
\begin{gathered}
E_{K}=R+E_{P} \\
E_{P}=h v-E_{B}-\phi_{D}-R
\end{gathered}
$$

Equation 2.3

The resolution and signal to noise ratios of this technique are determined by the $E_{P}$ chosen. To understand why, a deeper explanation of the detector operation is necessary. As electrons pass through the detector, the flight of those electrons with energy $E_{P}$ should be through the mean

distance between the two hemispheres $R_{0}$. To achieve this, the voltages are positive on the inner hemisphere $\left(R_{1}, V_{1}\right)$ and negative on the outer hemisphere $\left(R_{2}, V_{2}\right)$, creating a voltage gradient in the area between the two hemispheres. The voltages required to keep electrons with energy $E_{P}$ along this mean line, $V_{0}$, are determined by the detector geometry (equation 2.5 , figure 2.3).

$$
e V_{0}=E_{P}\left(\frac{R_{2}}{R_{1}}-\frac{R_{1}}{R_{2}}\right)
$$

![img-18.jpeg](images\img-18.jpeg)

Figure 2.3. Schematic of an XPS hemispherical detector. Electrons enter the detector slit of width $d$ and an angle $\alpha$. A negative voltage of $V_{1}$ is applied to the inner plate $R_{1}$, while a positive voltage $V_{2}$ is applied to the outer plate $R_{2}$. This ensures electrons with $E_{K}=E_{P}$ travel along the mean line between the detectors $R_{0}$ and exit through a slit of the same width $d$ on the other side. Electrons with energies that are too high or low will hit the plates and not be detected.

Using equation 2.5 , the voltages applied to the inner (equation 2.6) and outer (equation 2.7) plates to achieve this $V_{0}$ are:

$$
\begin{aligned}
& V_{1}=E_{P}\left(2 \frac{R_{0}}{R_{1}}-1\right) \\
& V_{2}=E_{P}\left(2 \frac{R_{0}}{R_{2}}-1\right)
\end{aligned}
$$

These equations indicate that at low $E_{P}$ the voltage gradient will be less and small differences in $E_{K}$ will be deflected further. As the $E_{P}$ increases, so does the voltage gradient, resulting in less deflection of electrons and more electrons passing through the detector. In this way, increasing the $E_{P}$ decreases the resolution of the instrument while increasing the magnitude of the signal and consequently the signal to noise ratio. The complete equation for determining the resolution of XPS is given by equation 2.8 .

$$
\Delta E=E_{P}\left(\frac{d}{2 R_{0}}+\alpha^{2}\right)
$$

Where $\Delta E$ is the resolution of the instrument, $d$ is the slit width and $\alpha$ is the half angle of electrons as they enter the detector. Both $d$ and $\alpha$ are shown on figure 2.3. Due to the high background in the ceria XPS region, discussed further in chapter 3, the $E_{P}$ used is larger than what would typically be used when scanning a region in the spectrum. This further increases the difficulty of fitting an already complicated spectrum.

Because orbital binding energies are unique, this technique can identify and quantify the elements present. Further, the energy resolution of the instrument is sufficient to detect the small differences in binding energy due to splitting of the electron orbitals. Since electrons can only travel a few nanometers through a solid before losing energy [70], [71], the information collected

through this technique is limited to the surface of a sample. The surface is the only region that participates in chemical reactions, so this is property is ideal for studying the effect of $\mathrm{Ce}^{3+} \%$ on chemical removal. A typical ceria spectrum will contain 10 peaks which are deconvolved using the CasaXPS (Ver. 2.3.19) analysis software through a process discussed in chapter 3 [72].

# C. pH 

The pH measurements were carried out with a HANNA instruments HI2210-01 pH meter coupled with a HI1131B double junction glass electrode. This instrument measures an electrical signal that is the result of a change in $\mathrm{H}^{+}$concentration to determine the pH of the solution. The pH of a slurry is an important metric that can affect both the mechanical and chemical removal of a wafer.

## D. Ellipsometry

Thickness measurements for silicon oxide and nitride films were measured on a J.A. Woollam RC-2 variable angle spectroscopic ellipsometer (VASE) over a spectral range of 250 nm to 1000 nm and three angles of incidence $\left(55^{\circ}, 65^{\circ}, 75^{\circ}\right)$. In this technique, a light source emits radiation that passes through a polarizer before impacting a sample and being reflected into a detector (fig. 2.4) [73]. This light oscillates both perpendicular (s) and parallel (p) to the plane of incidence. After polarization, the oscillations have the same phase and amplitude resulting in linearly polarized light where the "spot" is a line. After reflection, however, the two components will no longer be in phase or have the same amplitude resulting in an ellipsoidal spot. This is the origin of the name ellipsometry. The true initial and reflected values of each component cannot

be determined, but the differences can be calculated through a complex equation involving the ratio between the measured parallel and perpendicular amplitudes $\left(\frac{r_{p}}{r_{s}}\right)$ (equation 2.9 ).

$$
\frac{r_{p}}{r_{s}}=\tan (\Psi) e^{i \Delta}
$$

![img-19.jpeg](images\img-19.jpeg)

Figure 2.4. Schematic of the ellipsometry process. Linearly polarized light, left, will impact a particle surface causing a change in both its phase and amplitude resulting in light with an ellipsoidal spot. $\mathrm{E}_{\mathrm{i}}$ and $\mathrm{E}_{\mathrm{r}}$ cannot be measured but $\Psi$ can be determined experimentally.

The difference in amplitude and phase are denoted $\Psi$ and $\Delta$ respectively. By altering the wavelength of the probing light and the angle of incidence, multiple spectra can be obtained; each with unique $\Psi$ and $\Delta$ values across the range of wavelengths scanned. By fitting these spectra, the thickness of the sample being measured can be calculated.

# E. Atomic Force Microscopy 

Short-range roughness ( $R_{B M S}$ ) measurements were obtained using a Dimension Icon scanning probe microscope/ atomic force microscope (AFM) in tapping mode. In this technique, a

sharpened tip is rastered back and forth across the sample surface (trace-retrace) through the application of voltages on a piezoelectric tube in the x and y directions [74]. The probe tip is on the free end of a cantilever and voltages applied on the tube in the $z$ direction cause this cantilever to flex. This forces the tip to oscillate with a known amplitude and frequency. While sampling, a laser focused on the backside of the cantilever is deflected onto a series of mirrors into a position sensitive photo-detector. The position of the laser on the detector oscillates in phase with the oscillating cantilever. During operation the cantilever is lowered to a known height above the sample. At this height, the cantilever will touch the surface during its oscillation. These impacts or "taps" on the surface decrease the free range of motion of the cantilever (fig. 2.5).

![img-20.jpeg](images\img-20.jpeg)

Figure 2.5. SEM image of the cantilever a) and tip b) of a Bruker TESPA-V2 AFM Probe [75]. Schematic representation of an oscillating cantilever when it approaches a sample surface c). The reduction in oscillation amplitude and change in frequency can be used to determine the distance between the sample and the reference height.

This results in a decrease in the amplitude of both the cantilever and, consequently, the laser on the detector. Using this change in amplitude and the known height of the cantilever above the surface at every point, a topographical map is constructed and roughness values extracted from this map. These values are often reported as root mean square roughness $\left(\mathrm{R}_{\mathrm{RMS}}\right) . \mathrm{R}_{\mathrm{RMS}}$ reveals the magnitude of deviation from the mean surface (equation 2.10 ).

$$
R_{R M S}=\sqrt{\frac{1}{n} \sum_{i=1}^{n} j_{i}^{2}}
$$

Where $n$ is the number of data points along the scan and $j_{i}$ is the distance from the mean surface at the $i^{\text {th }}$ point.

By using tapping instead of contact mode, lateral forces can be reduced and any debris or particles left on the wafer post-polish will not be dragged by the tip while scanning, altering the resulting data. For $\mathrm{R}_{\mathrm{RMS}}$ measurements in this study, the image was obtained over an area of 10 $\mu \mathrm{m} \times 10 \mu \mathrm{~m}$ with a scan rate of 0.7 Hz using a TESPA-V2 probe-tip with nominal tip height and radius of $12.5 \mu \mathrm{~m}$ and 7 nm respectively. The lateral resolution of this technique is $\sim 40 \mathrm{~nm}$, while the vertical resolution is $\leq 0.1 \mathrm{~nm}$. The decrease in lateral resolution is a result of the pixel size at such a large sample area. This pixelation has no effect on the vertical resolution of the instrument.

# F. Profilometry 

Long-range roughness ( $R_{Z}$ ) measurements were obtained using a Veeco Dektak 150 profilometer. During this technique a stylus is placed in contact with the sample and scanned across the surface. The change in height of the stylus as it scans is used to determine the roughness of the sample surface. $R_{Z}$ or $R_{Z} D I N$ is calculated by splitting the scan length into five sections and taking the average of the difference between the highest peak and lowest valley $\left(R_{t}\right)$ in each section $s$ (equation 2.11 ).

$$
R_{Z}=\frac{1}{s} \sum_{i=1}^{s} R_{t, i}
$$

The stylus used in this work has a radius of $12 \mu \mathrm{~m}$ and was used with a downforce of 0.1 N at a scan rate of $200 \mu \mathrm{~m} / \mathrm{sec}$ over $2000 \mu \mathrm{~m}$ and a measurement range of $6.5 \mu \mathrm{~m}$ in the z-direction. These settings result in a horizontal resolution of $0.667 \mu \mathrm{~m}$ and a vertical resolution of 1.0 nm .

# G. Mass Removal 

Mass measurements were carried out with an A\&D BM-20 mass balance. This balance has a resolution of $\pm 6 \mu \mathrm{~g}$. With such high resolution, mass removal can be detected for polishing even over short time scales. A standard microbalance would require polishing for an hour or more before a difference could be measured accurately. Over this long time period, the pore structure of the polishing pad would be destroyed and the polishing properties would not be uniform across a single polish or between experiments.

# III. Design of Ceria Slurry for CMP Applications 

## A. Introduction

The creation and improvement of commercial products is often a process of finding what works the best without the need to fully understand the mechanisms that underlie those improvements. Optimizing ceria slurries followed this path, but further improvements can be achieved by understanding the chemical properties of ceria and applying this knowledge to synergize with the improvements from the physical properties of ceria particles. The chemical reaction between ceria and other oxides as described by Cook requires $\mathrm{Ce}^{3+}$ sites at the surface of the particle [57], often reported as $\mathrm{Ce}^{3+} \%$ due to the presence of both $\mathrm{Ce}^{3+}$ and $\mathrm{Ce}^{4+}$ at the surface. If this percentage can be increased there will be more active sites, and presumably a proportionately greater removal rate.

Most studies to date have focused on altering physical properties of the ceria to increase the $\mathrm{Ce}^{3+} \%$. The most studied property for increasing the $\mathrm{Ce}^{3+} \%$ is altering the size of the nanoparticles [11], [76], [77]. This change in oxidation state with size is due to the increase in strain at the particle surface. To relieve this strain an oxygen atom forms an anti-Frenkel defect, leaving behind a charged vacancy at the surface of the particle [78], [79]. Using Kröger-Vink notation, the vacancy formation can be described by a reaction between cerium, oxygen and an oxygen vacancy (equation 3.1). In this notation an element symbol as a subscript denotes a lattice site for that element, V denotes a vacancy, while ' and - denote electrons and holes respectively. Taken with this notation, $V_{O}$ is a vacancy located at an oxygen lattice site that has two holes ( +2 charge).

$$
2 C e_{C e}+O_{O}=2 C e_{C e}^{\prime}+V_{O}+\frac{1}{2} O_{2}(g)
$$

As the electrons left behind by the oxygen reduce the nearby cerium from $\mathrm{Ce}^{4+}$ to $\mathrm{Ce}^{3+}$ without any other change to the cerium sites, this can subsequently be simplified to an electron-vacancy pair reaction (equation 3.2 ).

$$
O_{O}=2 e^{\prime}+V_{O}+\frac{1}{2} O_{2}(g)
$$

Based on these reactions, each vacancy has two positive charges balanced by two delocalized electrons. These electrons will align to one side of the vacancy creating a dipole. This dipole attracts nearby vacancies, which migrate until they are close enough that their electrons begin to repel each other [80], [81]. The charge of these near-adjacent vacancies will be compensated by their surrounding cerium atoms (equation 3.3), with the cerium atoms bound to two vacancies being reduced.

$$
4 e^{\prime}+2 V_{O}+8 C e^{4+}=2 V_{O}+4 C e^{4+}+4 C e^{3+}
$$

This equation can, in turn, be simplified to the redox reaction for cerium given earlier as equation 1.1, reproduced here:

$$
C e^{4+}+e^{-} \leftrightarrow C e^{3+}
$$

In addition to the size-related strain mechanism, the $\mathrm{Ce}^{3+} \%$ content of a particle can be increased by the addition of lanthanide dopants that are naturally stable in the trivalent state [82]. These dopants force oxygen vacancies into the particle around which the bound cerium is converted to the $\mathrm{Ce}^{3+}$ state.

The second physical property studied for altering the $\mathrm{Ce}^{3+} \%$ is synthesis conditions [12], [65] (table 3.1).

Table 3.1. Physical properties of ceria particles with different synthesis methods

| Synthesis Method | Wet chemical at <br> $\mathbf{2 5}^{\circ} \mathbf{C}$ | Wet chemical at <br> elevated <br> temperature | Dry synthesis at <br> $\mathbf{3 0 0}{ }^{\circ} \mathbf{C}$ |
| :-- | :-- | :-- | :-- |
| Crystallinity | polycrystalline | polycrystalline | monocrystalline |
| Defectivity | high | high | low |
| Shape | rounded | rounded | faceted |
| Initial $\mathbf{C e}^{\mathbf{3 +}} \%$ | High | High | low |

There are three distinct routes for the formation of ceria nanoparticles: wet chemical synthesis at room temperature, wet chemical synthesis at elevated temperature but beneath the boiling point of the solvent, and dry synthesis at temperatures exceeding $300^{\circ} \mathrm{C}$. At higher synthesis temperatures, the initial $\mathrm{Ce}^{3+} \%$ of the ceria nanoparticles is lower [10]. This trend results from the crystallinity of the particles synthesized. A monocrystalline product like that created through dry synthesis, calcination or thermal decomposition, will have very few surface defects and hence low $\mathrm{Ce}^{3+} \%$. Additionally, these particles also perform poorly as CMP abrasives from a mechanical perspective due to their highly faceted nature. The many sharp edges will scratch a wafer if used for polishing. Both of the other two routes, room temperature and solvothermal synthesis, will produce polycrystalline particles. These particles have many surface defects resulting in a higher $\mathrm{Ce}^{3+} \%$ and are more spherical [13], [83]. This leads to better CMP from

both a chemical and mechanical perspective. For very small particles ( $<10 \mathrm{~nm}$ ), there is no difference in the crystallite size within the particles between different wet chemical methods. With larger particles ( $10<\mathrm{x}<200 \mathrm{~nm}$ ), the increased temperature of a solvothermal synthesis will cause recrystallization, leading to larger crystallites within a given particle and a decrease in the number of surface defects $\left(\mathrm{Ce}^{3+} \%\right)$ on the particle [12].

These factors, specifically the size and synthesis temperature as well as any dopants added during synthesis, will determine the initial $\mathrm{Ce}^{3+} \%$ while the particles are isolated but does not fully reflect the chemical interactions that may occur during slurry creation and subsequent polishing. As the particles are dispersed in a slurry, interactions with the chemicals in this new environment can dramatically alter both the reaction rates and the $\mathrm{Ce}^{3+} \%$.

# 1. Determination of Chemical Effects with XPS 

Most studies to date analyze the slurry post-polishing spectroscopically using UV-Vis to determine the $\mathrm{Ce}^{3+} \%$. These studies agree that the $\mathrm{Ce}^{3+} \%$ present in the slurry is dependent on pH [61], [62], [64], [84]. However, UV-Vis only measures the concentration of $\mathrm{Ce}^{3+}$ ions in the slurry liquid, not on the surface of the particles and therefore cannot offer direct insight into the reactions at the particle surface. A few studies have used the surface measurement technique XPS to evaluate CMP outcomes, but they focused on identifying foreign materials left behind on the polished surface rather than studying the slurry itself [59], [62], [63]. In this study, I rely on the surface sensitive nature of XPS, combined with its ability to discriminate between different chemical states of the same element to offer insights not available in any previous study. In

particular, XPS enables me to determine the $\mathrm{Ce}^{3+} \%$ on the surface of the ceria particles in a slurry.

A comprehensive description of the XPS equipment can be found in Chapter 2; here I present a brief review of the technique with a detailed description of the orbitals and energetics of cerium specifically, to account for all of the spectral features in my data.

The first step to obtaining $\mathrm{Ce}^{3+} \%$ information is determining the appropriate electron orbital to measure in XPS. The binding energy of an electron is unique to the orbital in which it is localized, as dictated by quantum mechanics. The orbital chosen must be able to undergo splitting so that the different oxidation states can be distinguished from each other. While the electron configuration of cerium, $[\mathrm{Xe}] 4 \mathrm{f}^{1} 5 \mathrm{~d}^{1} 6 \mathrm{~s}^{2}$, contains orbitals with energy from the $1 \mathrm{~s}-6 \mathrm{~s}$, electrons with binding energies that are greater than the energy of the incoming $\mathrm{Al} \mathrm{K}_{\mathrm{a}} \mathrm{X}$-ray ( 1487 eV ) will not be ejected upon impact [85], [86]. Mathematically, this would result in a negative $\mathrm{E}_{\mathrm{K}}$ in equation 2.2 , which is clearly not meaningful. Physically, this means that the incoming X-ray does not have sufficient energy to eject an electron from one of those orbitals. For cerium, this eliminates the possibility of obtaining information from orbitals with higher energy than the 3 d orbital. Of the orbitals with energy lower than 3 d , the 5 s orbital cannot exhibit splitting and the valence orbitals ( $4 \mathrm{f}, 5 \mathrm{~d}, 6 \mathrm{~s}$ ) have very low peak intensities and binding energy making them unsuited for XPS analysis. Of the remaining orbitals, while they encounter the same problems as the valence orbitals, the $4 \mathrm{p}, 4 \mathrm{~d}$ and 5 p can be analyzed for oxidation state information. Unfortunately, to resolve the small differences in energy between peaks of different oxidation state in these orbitals, a very low pass energy is required, greatly lowering the signal-

to-noise ratio. Therefore, this analysis requires single crystal samples and very high resolution instruments operating with detectors of large center radius $R_{0}$, low angle of electron entry $\alpha$ and small slit width $d$ as per equation 2.8 , reproduced here:

$$
\Delta E=E_{P}\left(\frac{d}{2 R_{0}}+\alpha^{2}\right)
$$

This leaves the 3d orbital as the best orbital to analyze for chemical information. Though selecting the orbital was easy, analysis of the 3d orbital is not. This region has ten different photoelectron peaks with four corresponding to $\mathrm{Ce}^{3+}$ and six with $\mathrm{Ce}^{4+}$ (fig. 3.1 and Table 3.2).
![img-21.jpeg](images\img-21.jpeg)

Figure 3.1. Theoretical spectra of $\mathrm{Ce}^{4+}$ (blue) and $\mathrm{Ce}^{3+}$ (red). There are 10 peaks, 6 from $\mathrm{Ce}^{4+}$ and 4 from $\mathrm{Ce}^{3+}$. Nine of these peaks overlap with each other as one set of 5 and a second set of 4 [87].

Table 3.2 List of peaks by binding energy and type. Colors
indicate the different peak regions in a ceria spectra [88]

| Binding energy (eV) | Oxidation State | Peak type |
| :--: | :--: | :-- |
| 916.7 | $4+$ | Shake-up 3d ${ }_{3 / 2}$ |
| 907.4 | $4+$ | Parent 3d ${ }_{3 / 2}$ |
| 904.0 | $3+$ | Parent 3d ${ }_{3 / 2}$ |
| 901.0 | $4+$ | Shake-down 3d ${ }_{3 / 2}$ |
| 898.9 | $3+$ | Shake-down 3d ${ }_{3 / 2}$ |
| 898.4 | $4+$ | Shake-up 3d ${ }_{5 / 2}$ |
| 888.8 | $4+$ | Parent 3d ${ }_{5 / 2}$ |
| 885.4 | $3+$ | Parent 3d ${ }_{5 / 2}$ |
| 882.6 | $4+$ | Shake-down 3d ${ }_{5 / 2}$ |
| 880.6 | $3+$ | Shake-down 3d ${ }_{5 / 2}$ |

These peaks are grouped into three regions of decreasing binding energy with one (one $\mathrm{Ce}^{4+}$ ), five (three $\mathrm{Ce}^{4+}$, two $\mathrm{Ce}^{3+}$ ), and four (two $\mathrm{Ce}^{4+}$, two $\mathrm{Ce}^{3+}$ ) peaks respectively. These regions are color-coded in Table 3.2 as blue, red, and yellow, respectively. The large number of peaks arise from four different processes occurring simultaneously: (1) splitting of electron orbitals due to bonding, (2) increased/decreased screening of core nuclear charge, (3) the so-called 'shake-up' process, and (4) the so-called 'shake-down' process. Their origins and energies are summarized

in Table 3.2, and described individually in detail next, along with the so-called 'shake-off' process which contributes to an increased background signal in this region of the XPS spectrum.

The first process is the splitting of electron orbitals. When an atom has bonds to other elements, the orbital energy levels split based on the coordination of the bond [89]. In the case of the tetrahedral bonding between cerium and oxygen, the five 3d orbitals will split into two $3 \mathrm{~d}_{3 / 2}$ at higher binding energy and three $3 \mathrm{~d}_{5 / 2}$ orbitals with lower binding energy (fig. 3.2). This splitting results in each peak having a doublet with a difference in energy of $\sim 18.6 \mathrm{eV}$ and a peak area ratio of 2:3 for $3 \mathrm{~d}_{3 / 2}$ to $3 \mathrm{~d}_{5 / 2}$ respectively [90]. When a photoelectron is ejected and has no further interactions with the atom from which it is ejected, the resulting peak in the spectrum is called the parent peak and is denoted as $\mathrm{Ce}\left(3 \mathrm{~d}^{-1}\right)$. Thus, the orbital splitting results in two parent peaks for each of the cerium oxidation states in table 3.2.
![img-22.jpeg](images\img-22.jpeg)

Figure 3.2. Diagram of cerium 3d orbital splitting in $\mathrm{Ce}^{4+}$. Closed circles represent electrons and open circles are holes. As the 3d orbitals (red boxes) split, a difference in both eV and relative peak area is introduced into the XPS spectrum.

The second process arises from the presence of multiple oxidation states at the sample surface, the property of most interest for the XPS analysis of ceria. The difference of one electron between the $\mathrm{Ce}^{4+}$ and $\mathrm{Ce}^{3+}$ states results in a decrease in binding energy of the $\mathrm{Ce}^{3+}$ peaks by $\sim 4$ eV when compared to $\mathrm{Ce}^{4+}$. This difference is due to the extra 4 f electron in $\mathrm{Ce}^{3+}$ increasing the screening of the negatively charged electrons on the positively charged core [91]. This increased screening results in decreased pull on the photoelectron, allowing it to leave with a greater kinetic energy.

The last two processes, shake-up and shake-down, arise from energy transfers between the photoelectron and the other electrons in the atom as it is ejected [92]. During a shake-up process, the ejected electron will transfer energy to an electron in the highest occupied orbital equal to the amount needed to promote that electron to the lowest unoccupied orbital. This transfer lowers the kinetic energy of the exiting photoelectron resulting in a calculated binding energy that is higher than the true binding energy for that electron when using the previous formula (fig. 3.3). For ceria, this transfer has an energy difference of 13.6 eV for a $\mathrm{Ce}^{4+}$ atom and the resulting peak denoted as $\mathrm{Ce}\left(3 \mathrm{~d}^{-1} 5 \mathrm{p}^{-1} 6 \mathrm{~s}^{+1}\right)$.

![img-23.jpeg](images\img-23.jpeg)

Figure 3.3. Schematic diagram of energy transfer from a moving photoelectron (blue) to a 5 p electron resulting in the photoelectron leaving the atom with lower energy (shake-up satellite peak) and the atom having an electron in an excited state.

A similar process can occur with atoms in the $\mathrm{Ce}^{3+}$ state, but the probability is very low, leading to this peak being lost in the considerable background in the Ce3d spectrum [93]. This background is due to an energy transfer referred to as a shake-off process. This is similar to the shake-up process, but the photoelectron transfers enough energy to eject the 5 p electron resulting in a wide range of detected photoelectron energies and considerable background, expressed as $\mathrm{Ce}\left(3 \mathrm{~d}^{-1} 5 \mathrm{p}^{-1}\right)$, at binding energies equal or greater than the true binding energy of the ejected electron (fig. 3.4).

![img-24.jpeg](images\img-24.jpeg)
![img-25.jpeg](images\img-25.jpeg)

Figure 3.4. Schematic diagram of the shake-off process, which increases the overall background in the spectrum but does not lead to a separate peak. (a) Transfer of energy from the exiting blue photoelectron to a 5 p electron which is also ejected (shake-off) results in (b) the photoelectron leaving with less energy than it initially posessed. (c) XPS spectrum of this region, demonstrating the increased background in the spectrum at binding energies $\geq$ the cerium energy region as a result of this process.

The shake-down process occurs through multiple steps starting the moment an X-ray imparts its energy upon the 3d electron [93]. Since this electron is no longer present in the 3d orbital, every

orbital with lower binding energy is now being screened from the positively charged nucleus by one electron less than it normally would be (fig 3.5a). This change is equal to the pull of a nucleus of praseodymium, the next lanthanide in the periodic table. Based on this information, it is theorized that the energy levels of all orbitals with lower binding energy than 3 d will be at the energy level of the same orbitals in praseodymium (equivalent core argument). This new energy level means that the 4 f orbital is now below the fermi level for cerium and a delocalized electron from the nearby O 2 p orbital can be transferred to the Ce 4 f orbital (fig 3.5b). As the photoelectron passes the 4 f orbital this extra localized electron increases the screening effect of the electrons on the core, similar to the increased screening of $\mathrm{Ce}^{3+}$ over $\mathrm{Ce}^{4+}$ discussed previously. This increase in kinetic energy is $\sim 5 \mathrm{eV}$ and the peak is labeled $\mathrm{Ce}\left(3 \mathrm{~d}^{-1} 4 \mathrm{f}^{-1}\right) \mathrm{O}\left(2 \mathrm{p}^{-1}\right)$ (fig. 3.5c).

![img-26.jpeg](images\img-26.jpeg)

Figure 3.5. Schematic diagrams of electron transfer between oxygen and cerium during ejection. Ejection of a 3d electron a) increases the binding energy of the 4 f orbital below the fermi level of cerium. This allows for b) the transfer of electrons from oxygen and c) decreases the pull from the nucleus (represented by green lines) on the ejected photoelectron, increasing its kinetic energy (shake-down satellite peak).

After obtaining a spectrum that contains all ten peaks, fitting must be performed along with deconvolution of the areas with multiple peaks to calculate an accurate $\mathrm{Ce}^{3+} \%$. The first step in fitting is to determine the positions of each peak in the spectrum. Cerium naturally forms the

oxide $\mathrm{CeO}_{2}\left(\mathrm{Ce}^{4+}\right)$ so there are readily available references that have these peak positions listed [88]. Unfortunately, the oxide $\mathrm{Ce}_{2} \mathrm{O}_{3}\left(\mathrm{Ce}^{3+}\right)$ is a pyrophoric compound at room temperature and so cannot be isolated to create a reference. Most papers use the peaks for $\mathrm{CePO}_{4}$, a stable compound in which cerium is pinned in the $\mathrm{Ce}^{3+}$ state as a substitute reference for the oxide [94]. Alternatively, reference peak positions for $\mathrm{Ce}^{3+}$ in an oxide can be obtained in situ by etching a $\mathrm{CeO}_{2}$ film (fig. 3.6a) inside the XPS to form a $\mathrm{Ce}_{2} \mathrm{O}_{3}$ surface on the sample (fig 3.6b). This oxidation state change is due to the much lower atomic weight of oxygen compared to cerium which leads to differential sputtering of the oxygen, leaving the film in the sub-stoichiometric state $\mathrm{CeO}_{\mathrm{x}}$ where x is between 2 and 1.5 . After many etch steps x will be $\cong 1.5$ and the film will have artificially changed oxidation state from $4+$ to $3+$. This in situ method was used as the second reference spectrum for the remainder of this study.
![img-27.jpeg](images\img-27.jpeg)

Figure 3.6. XPS spectra of the $\mathrm{CeO}_{2}$ film initially a) and after 2400 s etching b). $\mathrm{Ce}^{4+}$ peaks are no longer present with a large enough area to mask the position of the $\mathrm{Ce}^{3+}$ peaks. Data for this reference generated during a study of Au impregnated ceria films [95].

These two references allow the position of each of the nine convoluted peaks to be determined in relation to the single isolated peak at 916.7 eV . This is an important step to compensate for any charging the surface may experience during sampling.

The next consideration for accurate fitting is the background used [96]. The traditional background types used in XPS fitting are Shirley and Tougaard. The former is iteratively determined through estimation of the total peak area over the range being fit while the latter is based on the probability of an electron undergoing a loss event [97], [98]. Since both of these methods make assumptions about the processes occurring, the actual peak areas calculated can vary widely from fit to fit. Alternatively, a practical background for fitting a Ce3d spectrum was chosen, consisting of a linear background split into three distinct sections, each corresponding to the three groups of peaks. Though this background has no physical meaning, its repeatability and reproducibility means that the spectra fit with this background can be directly compared to each other. In other words, although the absolute values obtained from a single spectrum may be inaccurate, they are precise; differences between spectra can therefore be reliably interpreted.

The third parameter for fitting is the shape of the peaks being fit. Peaks in a spectrum should be sharp lines as the orbital energies are sharply defined by quantum mechanics, but they undergo broadening due to detector response, x-ray line shape, thermal broadening, sample charging, and natural broadening due to uncertainties in the lifetime and energy of the ejected electron. The first four effects are Gaussian in nature, while the last is Lorentzian [96]. To account for all of these effects a pseudo-Voigt line shape that takes the product of the Gaussian and Lorentzian components is used at a mix of 70:30 [99].

The final parameter for fitting is the full width half max of each peak (FWHM). The $3 \mathrm{~d}_{3 / 2}$ parent peak is slightly isolated at higher binding energy side of the middle group enabling the determination that the FWHM of these peaks is 3.5 eV and is independent of sample charging. The satellite peaks range in FWHM from 2.4-3 eV due to sample charging with their FWHM determined on a sample by sample basis by fitting the isolated shake-up peak.

After these parameters are determined, constraints need to be added to the system. Since fitting programs give the mathematically best possible fit, they can create unrealistic peak profiles to achieve their goal such as negative peak areas or peaks that have a higher intensity then the data they are being fitted to (fig. 3.7). By adding constraints, fits can be performed that give a meaningful $\mathrm{Ce}^{3+} \%$ estimate. The constraints used in this thesis were $\pm 0.5 \mathrm{eV}$ FWHM, $\pm 0.3 \mathrm{eV}$ peak position, a doublet splitting of $18.6 \pm 0.2 \mathrm{eV}$, an area ratio of $2: 3$ for $3 \mathrm{~d}_{3 / 2}: 3 \mathrm{~d}_{5 / 2}$ and a maximum peak height equal to the spectrum height. Additionally, based on the various reference spectrum obtained for the $\mathrm{Ce}^{3+}$ peaks, the peak area of the shake-down doublet is between 50-80 $\%$ of the parent doublet. This final constraint is crucial to proper fitting since the $\mathrm{Ce}^{3+}$ peaks are fully concealed by the $\mathrm{Ce}^{4+}$ peaks leading to unrealistic fits where the parent peaks are 1000x more intense than the shake-down peaks or vice versa.

![img-28.jpeg](images\img-28.jpeg)

Figure 3.7. The importance of realistic fitting in XPS analysis. a) Fitting a ceria peak without constraints can result in peak with greater height than the data they are derived from (black highlighted region). (b) With proper constraints, the non-physical results can be avoided.

After fitting with these constraints, a Monte Carlo simulation is performed and if the standard deviation of the peak position is greater than $1 \mathrm{eV}, \sim 25 \%$ of the smallest difference in peak position being measured (parent to shake-down), the fit is discarded. The final step of fitting is decoupling peak area and the element being analyzed (equation 3.4).

$$
\text { Adjusted Area }=\frac{\text { Raw Area }}{\text { RSF }+T+M F P}
$$

Where RSF is the relative sensitivity factor, T is the transmission factor and MFP is the mean free path of an electron traveling through a solid. The RSF of a peak is determined by X-ray source, element, orbital and spin orbital. The two RSF libraries that are commonly used are Scofield [100] and Wagner [101]. For this fitting I used the Scofield library for an Al X-ray source. When fitting peaks, only one orbital per element should be fit. If only one spin orbital is fit, the RSF of that spin orbital is used. If both are fit, the combined RSF is used to fit all peaks

[96]. Throughout this study, the RSF used is 51.6, the combined RSF of the $3 \mathrm{~d}_{3 / 2}$ and $3 \mathrm{~d}_{5 / 2}$ orbitals. MFP is determined by the element that the electron is traveling through. Once the fit is accepted and the peak areas calculated, the $\mathrm{Ce}^{3+} \%$ can be extracted by dividing the area of the $\mathrm{Ce}^{3+}$ peaks by the total area of the Ce peaks.

Using this information, the effect of a variety of chemical additives on the ceria surface can be determined. I hypothesized that pH has no effect on the $\mathrm{Ce}^{3+} \%$ on the particle surface and that any changes reported in literature were changes in oxidation state of free ions in solution. To test this hypothesis, I first measured the known effect of particle size on $\mathrm{Ce}^{3+} \%$. After this confirmation, I measured the $\mathrm{Ce}^{3+} \%$ over a pH range of 2-12. Additionally, I tested the effect of other slurry additives, namely oxidizing agent and surfactants, on the $\mathrm{Ce}^{3+} \%$.

# B. Materials and Methods 

1. Materials

Table 3.3 Chemicals used during ceria abrasive slurry trials

| Chemical name | Manufacturer |
| :-- | :-- |
| 50 nm ceria powder | Sigma-Aldrich, St. Louis, MO |
| 5 nm ceria dispersion (20 wt.\%) |  |
| Hydrogen peroxide $\left(\mathrm{H}_{2} \mathrm{O}_{2}\right)$ |  |
| Potassium hydroxide $(\mathrm{KOH})$ |  |
| Nitric acid $\left(\mathrm{HNO}_{3}\right)$ |  |
| Sodium dodecyl sulfate (SDS) |  |
| Polyvinylpyrrolidone (PVP) |  |
| Glycine |  |
| Cetyltrimethylammonium bromide (CTAB) |  |
| 20 nm ceria powder | Sky Spring Nanomaterials, Houston,TX |

## 2. Procedure

Slurries were prepared by mixing $0.02 \mathrm{~g}(1.0 \mathrm{wt} . \%)$ ceria abrasives, $0.030 \mathrm{~cm}^{3}$ of $30 \mathrm{wt} . \% \mathrm{H}_{2} \mathrm{O}_{2}$ $(0.5 \mathrm{wt} . \%)$ and $1.5 \mathrm{~cm}^{3} \mathrm{DI} \mathrm{H}_{2} \mathrm{O}$, after which the final volume was adjusted to $2 \mathrm{~cm}^{3}$ with $\mathrm{DI} \mathrm{H}_{2} \mathrm{O}$. The pH of the slurry was subsequently adjusted to pH 8 with 0.1 M KOH . Following this, the slurry was placed in a sonication bath for 1 min to ensure proper dispersion of the ceria abrasives. To optimize the chemical removal properties of ceria abrasive slurries, several chemical and one physical parameter were investigated.

# C. Results and Discussion 

## 1. Effect of particle size

Before determining the effect of chemical environment on $\mathrm{Ce}^{3+} \%$, the effect of physical properties of the particles were determined. This ensures that the results are representative of ceria as a whole and not due to an unknown variable in the production process. To isolate the physical properties, three different sizes of ceria from two different manufacturers were measured. The three sizes chosen represent the main range of particle sizes for typical ceria CMP abrasives (5-70 nm). The representative SEM images of the different ceria used in this study are shown in figure 3.8.

![img-29.jpeg](images\img-29.jpeg)

Figure 3.8. SEM images of a) $\mathrm{Ce} 1(68 \mathrm{~nm})$ and b) $\mathrm{Ce} 2(20 \mathrm{~nm})$ at a magnification of 150 kx . The final image c) $\mathrm{Ce} 3(6 \mathrm{~nm})$ was obtained at a magnification of 450 kx .

The particles in figure 3.8 a and b were obtained as a powder and re-dispersed to form a slurry while those in figure 3.8 c were already dispersed in water. These samples will be referred to as Ce1, Ce2 and Ce3 respectively. Ce1 had the largest particle size average, at 68 nm ; Ce2 was 20 nm ; and Ce 3 was 6 nm . To prepare XPS samples, these slurries were dried onto a conductive copper substrate. After drying, the particles were introduced into the vacuum chamber and analyzed. While it is impossible to ensure the number of particles in each sample is identical, the calculation for $\mathrm{Ce}^{3+} \%$ is based on the ratio of peak areas in a single spectrum and not the intensity of those peaks. This difference in sample loading will therefore not have an effect on

the $\mathrm{Ce}^{3+} \%$ that is calculated. To ensure the XPS results were meaningful multiple samples were created for each data point to obtain average values and their associated errors. XPS spectra for the three ceria particle sources are shown in figure 3.9. As the size of the particles decreases, the size of the $\mathrm{Ce}^{3+}$ peaks in the spectrum increases, indicating a higher $\mathrm{Ce}^{3+} \%$ on the particle surface, consistent with other reports [11], [76], [77]. The sizes and initial $\mathrm{Ce}^{3+} \%$ of the asreceived samples are summarized in Table 3.3.
![img-30.jpeg](images\img-30.jpeg)

Figure 3.9. XPS analysis of as-received ceria abrasives a) Ce1 b) Ce2 c) Ce3. The blue peaks correspond to $\mathrm{Ce}^{4+}$ while the green correspond to $\mathrm{Ce}^{3+}$. The area of the green peaks $\left(\mathrm{Ce}^{3+}\right.$ \%) increases with decreasing particle size.

Table 3.4 Average size and $\mathrm{Ce}^{3+} \%$ of as-received ceria powders

| Particle | Average Size (nm) | $\mathbf{C e}^{\mathbf{3 +}}$ concentration (\%) |
| :-- | :-- | :-- |
| Sigma Powder | $68 \pm 10$ | $12 \pm 1.4$ |
| Sky Spring Nanomaterials <br> Powder | $20 \pm 5.5$ | $26 \pm 1.2$ |
| Sigma Dispersion | $5 \pm 1.8$ | $31 \pm 1.2$ |

# 2. Effect of pH 

The first chemical parameter investigated was pH , since it has been previously reported to have an effect on $\mathrm{Ce}^{3+} \%$. Ce 1 and Ce 2 were dispersed in water and the pH of all three samples were measured and found to be $\sim 8$ without any modification. Model slurries were then made with pH ranging from 2-12. When samples were dried from these models, a pH strip was dipped in DI $\mathrm{H}_{2} \mathrm{O}$ and then pressed against the dried powder. The pH values measured indicated that no changes in pH had occurred due to the drying process. Thus, the XPS measurements, despite being conducted on dry powders (which are not normally referred to in terms of pH ) will still be representative of the pH of the liquid slurry.

Figure 3.10 shows that the calculated concentration of $\mathrm{Ce}^{3+}$ on the surface of each ceria changes negligibly across a wide range of pH . While the particles differ from each other, each particle stayed at its own initial value across the pH range tested. These values are in disagreement with those found previously in the literature, which measured cerium ions in solution using UV-Vis spectroscopy post-CMP, but did not directly measure the $\mathrm{Ce}^{3+}$ on the surface of the nanoparticles.
![img-31.jpeg](images\img-31.jpeg)

Figure 3.10. Effect of pH on the $\mathrm{Ce}^{3+}$ concentration of different ceria particles. No ceria particles exhibited significant change in $\mathrm{Ce}^{3+} \%$ across the pH range of 2-12. Lines included as a guide for the eye only.

This point is critical, since these prior literature reports linked an increase in removal rate as pH approached the isoelectric point of ceria [102] to their detection of $\mathrm{Ce}^{3+}$ in solution. However, since changing the pH did not change the proportion of available $\mathrm{Ce}^{3+}$ on the particles that are actually responsible for material removal, the observed increase in removal rates with increasing pH must be related to the interaction between ceria and the oxide surface. As discussed earlier,

chemical removal occurs when the slurry is at or near the isoelectric point of either the ceria or the oxide (equations 1.3 or 1.4). Cook stated in his paper that to obtain high removal rates the oxide must be able to undergo hydrolysis to incorporate $\mathrm{H}_{2} \mathrm{O}$ into its lattice. This incorporation breaks subsurface oxygen bonds upon subsequent particle impacts, thus increasing the probability that a silicate will be removed. The hydrolysis of silica has been determined to only occur at an appreciable rate above pH 7 (equation 1.2) [56].

Based on these points, it can be seen that the highest removal rate would occur at $\mathrm{pH} 8-9$, due to greater hydrolysis of silica and increased rate of condensation between ceria and silica. A final consequence of chemical removal through condensation reactions is that the concentration of $\mathrm{Ce}^{3+}$ sites has no effect on reaction rate. Any increased removal due to increasing $\mathrm{Ce}^{3+} \%$ is instead due to a greater probability for the reaction to occur.

# 3. Effect of peroxide 

The second chemical parameter tested was the effect of oxidizing agent on the $\mathrm{Ce}^{3+} \%$ of the particles, shown in figure 3.11. The initial $\mathrm{Ce}^{3+} \%$ values given in Table 3.3 correspond to the $0 \%$ $\mathrm{H}_{2} \mathrm{O}_{2}$ data points in this figure.

![img-32.jpeg](images\img-32.jpeg)

Figure 3.11. Effect of $\mathrm{H}_{2} \mathrm{O}_{2}$ on the $\mathrm{Ce}^{3+}$ concentration of different ceria particles (lines included as a guide for the eye only). Both of the smaller particles (Ce2 and Ce3) exhibit an inverse relationship between $\mathrm{Ce}^{3+} \%$ and $\mathrm{H}_{2} \mathrm{O}_{2}$ wt. $\%$. Ce 1 has a more complicated relationship with a peak in $\mathrm{Ce}^{3+} \%$ at $0.5 \mathrm{wt} . \% \mathrm{H}_{2} \mathrm{O}_{2}$.

It would normally be assumed that as the oxidizing agent concentration increases, the cerium particles will be oxidized and the $\mathrm{Ce}^{3+} \%$ will subsequently decrease. This behavior holds true for both Ce 2 and Ce 3 , but surprisingly not for Ce 1 , where a more complicated relationship was found. In particular, the $\mathrm{Ce}^{3+} \%$ on the surface of Ce 1 doubles with the addition of small amounts of $\mathrm{H}_{2} \mathrm{O}_{2}$, then gradually decreases back to its initial concentration.

Traditionally, the effect of $\mathrm{H}_{2} \mathrm{O}_{2}$ on ceria has been explained using reduction-oxidation reactions due to ceria's use as a catalyst. Equations 3.5 and 3.6 correspond to the reduction of ceria, whereas equations 3.7 and 3.8 detail ceria oxidation [103].

$$
\begin{gathered}
C e O H^{3+}+H^{+}+e^{-} \rightarrow C e^{3+}+H_{2} O, E_{\text {red }}=+1.709 \\
H_{2} O_{2} \rightarrow 2 H^{+}+O_{2}+2 e^{-}, E_{o x}=-0.695 \mathrm{~V} \\
C e^{3+}+H_{2} O \rightarrow C e O H^{3+}+H^{+}+e^{-}, E_{o x}=-1.709 \mathrm{~V} \\
H_{2} O_{2}+2 H^{+}+2 e^{-} \rightarrow 2 H_{2} O, E_{\text {red }}=+1.776 \mathrm{~V}
\end{gathered}
$$

Equation 3.7

Equation 3.8

Equation 3.9

Based on these reactions the reduction of ceria is favored, yet only Ce 1 exhibits reduction, and even then, it is only upon small additions of $\mathrm{H}_{2} \mathrm{O}_{2}$. To understand how this seemingly counterintuitive result - that an oxidizing agent can reduce a metal cation - requires a deeper investigation into how ceria switches oxidation states. Ceria is often used to scavenge oxygen through catalysis [104], but in this case, it is more instructive to examine its ability to scavenge reactive oxygen species (ROS) from biological cells [26], [105]. For this purpose, ceria can mimic two different ROS scavengers, the enzymes catalase and superoxide dismutase (SOD). Ceria's SOD mimetic activity requires reacting with both $\mathrm{H}_{2} \mathrm{O}_{2}$ and oxygen radicals, whereas catalase only reacts with $\mathrm{H}_{2} \mathrm{O}_{2}$. Since the concentration of $\mathrm{H}_{2} \mathrm{O}_{2}$ in the slurry is much higher than the naturally occurring ${ }^{\bullet} \mathrm{O}_{2}^{-}$the ceria will react according to the catalase reaction mechanism (fig. 3.12 adapted from [27]).

![img-33.jpeg](images\img-33.jpeg)

Figure 3.12. Catalase mimetic activity of ceria. In this cycle, ceria reacts with $\mathrm{H}_{2} \mathrm{O}_{2}$ twice. At the top of the cycle, it converts $\mathrm{Ce}^{4+}$ to $\mathrm{Ce}^{3+}$, while at the bottom of the cycle it converts $\mathrm{Ce}^{3+}$ to $\mathrm{Ce}^{4+}$ (adapted from [27]).

Through this mechanism ceria reacts with $\mathrm{H}_{2} \mathrm{O}_{2}$ twice. First converting from $\mathrm{Ce}^{4+}$ to $\mathrm{Ce}^{3+}$ (top of diagram) and the second time reverts the particle back to the $\mathrm{Ce}^{4+}$ state (at the bottom of the diagram).

When the particle starts with a low initial $\mathrm{Ce}^{3+}$ state, like Ce 1 , it will proceed in the forward reaction converting $\mathrm{Ce}^{4+}$ to $\mathrm{Ce}^{3+}$ until enough $\mathrm{H}_{2} \mathrm{O}_{2}$ is added to continue the reaction and oxidize the cerium [106]. The other particles, Ce 2 and Ce 3 , enter the cycle with a higher $\mathrm{Ce}^{3+} / \mathrm{Ce}^{4+}$ ratio

and therefore proceed through the second half of the cycle only. With this knowledge, larger particles (which naturally have a lower $\mathrm{Ce}^{3+} / \mathrm{Ce}^{4+}$ ratio) and those with low $\mathrm{Ce}^{3+} \%$ due to other reasons can be tailored through small additions of $\mathrm{H}_{2} \mathrm{O}_{2}$ to increase this value and make them more effective as polishing abrasives.

# 4. Effect of surfactant 

The final parameter investigated was the effect of surfactants on the ability of $\mathrm{H}_{2} \mathrm{O}_{2}$ to increase $\mathrm{Ce}^{3+} \%$. Only Ce 1 was used for this set of experiments since there was no increase in $\mathrm{Ce}^{3+} \%$ upon $\mathrm{H}_{2} \mathrm{O}_{2}$ addition for either Ce 2 or Ce 3 .

As seen in figure 3.13a, the addition of surfactants to Ce 1 without $\mathrm{H}_{2} \mathrm{O}_{2}$ had no significant effect on the $\mathrm{Ce}^{3+} \%$ across a range of concentrations. Figure 3.13b shows the impact of surfactant after $0.5 \mathrm{wt} . \% \mathrm{H}_{2} \mathrm{O}_{2}$ has been added to the Ce 1 slurry, which maximizes the initial $\mathrm{Ce}^{3+} \%$. In this case, a difference is observed between the surfactants, where glycine and PVP both reduced the $\mathrm{Ce}^{3+} \%$ significantly while CTAB and SDS had almost no effect. While all the surfactants were added at $0.5 \mathrm{wt} . \%$, this concentration is above the critical micelle concentration for both SDS and CTAB [107], whereas glycine and PVP were in the form of single molecules or polymer chains respectively. This structural difference means that fewer surfactant molecules were available to bind to the ceria surface for the micellular surfactants than the linear ones. Subsequently, there are more unbound $\mathrm{Ce}^{3+}$ sites in slurries that contain the former, resulting in a greater $\mathrm{Ce}^{3+} \%$ at the particle surface.

![img-34.jpeg](images\img-34.jpeg)

Figure 3.13. Effect of surfactants on the $\mathrm{Ce}^{3+}$ concentration both a) without $\mathrm{H}_{2} \mathrm{O}_{2}$ and b) with 0.5 wt. $\% \mathrm{H}_{2} \mathrm{O}_{2}$ at $0.5 \mathrm{wt} . \%$ surfactants. Surfactants have a small effect on $\mathrm{Ce}^{3+}$ without $\mathrm{H}_{2} \mathrm{O}_{2}$. With $\mathrm{H}_{2} \mathrm{O}_{2}$ micellular surfactants (CTAB and SDS) have less effect on $\mathrm{Ce}^{3+} \%$ than linear surfactants (Glycine and PVP).

# D. Conclusions 

A model for the effect of chemical environment on the oxidation state of ceria abrasives for CMP was described. Each particle had a different initial $\mathrm{Ce}^{3+} / \mathrm{Ce}^{4+}$ ratio that is determined by their size and synthesis conditions. This ratio was not affected by the pH of the solution that the particles were dispersed in. By introducing $\mathrm{H}_{2} \mathrm{O}_{2}$ to the slurry, the ratio of cation valence state was altered in a predictable way based upon the initial conditions of the particle owing to the catalase-like reaction of ceria in the presence of $\mathrm{H}_{2} \mathrm{O}_{2}$. Finally, the addition of surfactants reduced the effectiveness of the slurries. The extent of the reduction depended on the physical structure of surfactants, which affected the number of surface sites that were blocked, leading to differences in their effect on the $\mathrm{Ce}^{3+} / \mathrm{Ce}^{4+}$ ratio. These findings can be used to inform and improve the design of future ceria slurries to maximize their chemical removal of oxides.

# IV. Improved Ceria Slurry for Thermal Silicon Oxide Polishing 

## A. Introduction

The previous chapter established the means for probing the $\mathrm{Ce}^{3+} \%$ on the surface of nanoparticles, and how that parameter responded to the chemical environment surrounding the particles [9]. The underlying premise is that such changes to the nanoparticles will have an impact on the polishing efficacy of a slurry made with those nanoparticles. This chapter now sets out to demonstrate the validity of this premise by polishing thermal silicon oxide.

There are two types of silicon oxide polishing currently being used in semiconductor manufacturing, the previously mentioned STI and ILD manufacturing steps. While polishing for these steps are each carried out in two phases known as the initial and final polish, the two processes have distinctly different challenges, and a brief review is provided here [51].

CMP after STI is focused on removal of excess dielectric material to create islands of active device regions isolated by dielectric trenches [49]. The first step of oxide CMP removes most of the excess material and planarizes the surface. At this stage, the remaining oxide should be of uniform thickness across the entire wafer surface. The second "final" polishing step is slower and smooths the surface across short distances. This polish removes the remaining excess material and stops once the nitride cap over the active region has been exposed.

Any long-range non-uniformity (within-wafer non-uniformity, WIWNU) that remains after the first step of polishing will propagate through the second polish. This can manifest as variation in

the nitride cap layer thickness, for example, which results in nonuniform transistor gate thickness and incomplete contacts with the tungsten plugs. Improper planarization at the first CMP step may also leave oxide residue on the nitride surface after the final polish. This oxide will inhibit chemical etch of the nitride and prevent the creation of transistor gates in that region.

While short-range variations (i.e., scratches) are unfavorable in the first polish, they can be compensated for with the final polish. On the other hand, scratches created during the final polish, especially in the nitride cap, will not be removed and are detrimental to the subsequent processing steps [108] (fig. 4.1).
![img-35.jpeg](images\img-35.jpeg)

Figure 4.1. SEM images [109], of "chatter mark" defects due to STI CMP. Post-CMP cleaning will etch the damage surface preferentially, resulting in defects that are much larger than the original scratch. Scale bars altered to improve visibility.

In addition, since the second CMP step exposes two materials, the selectivity to oxide polishing or difference in removal rate between oxide (high removal) and nitride (low removal) is critical at this stage. The lower this selectivity, the more likely there will be within-wafer differences in nitride cap thickness causing similar nonuniform transistor gate thickness and incomplete contacts with the tungsten plugs mentioned before.

Finally, correct endpoint determination is necessary at this stage to reduce overpolishing of the oxide. Oxide overpolishing will result in dishing, a concave surface, between the transistors and propagate this shape to later processing steps including lithography. High selectivity can help alleviate this problem because there will be a sharp decrease in removal rate once the nitride cap is exposed. This metric is therefore a reliable indicator of the polishing endpoint.

The second type of oxide CMP, ILD CMP, planarizes the oxide used to electrically isolate the metal layers in the MOL and BEOL. After ILD CMP is performed, metal contact (MOL) or via holes (BEOL) will be made to connect the FEOL to the BEOL or adjacent metal layers respectively. The initial polishing step for ILD CMP is the same as for STI CMP. This leads to the same challenges of WIWNU leading to errors in contact/via depth. The final polishing step in ILD CMP stops at a specific oxide thickness instead of a stopping layer (i.e. the nitride cap). This lack of an easily detectable endpoint complicates the CMP process and subsequently the polishing conditions are as gentle as possible to widen the acceptable window for polishing time. As before, an additional focus of this final polish is to remove any scratches created during the initial polish. This step is particularly critical in ILD CMP, since metals (and diffusion barriers) will be deposited next, during which steps the deposit will fill scratches that may be deeper than

the subsequent CMP can remove. This residual metal may cause shorts between the contacts or lines.

Summarizing, then, the critical performance metrics in both STI and ILD polishing are material removal rate (MRR), long-range surface roughness $\left(\mathrm{R}_{\mathrm{Z}}\right)$ and short-range surface roughness $\left(\mathrm{R}_{\mathrm{RMS}}\right)$. Selectivity relative to nitride is also an important factor in slurry evaluation [110]-[112]. This chapter focuses on correlating these metrics to the slurry design presented in the previous chapter for polishing thermal oxide. Slurry design for metal polishing has other considerations that will be discussed in the next chapter.

# B. Materials and Methods 

1. Materials

Table 4.1 Chemicals used during ceria polishing experiments

| Chemical name | Manufacturer |
| :--: | :--: |
| 50 nm ceria powder |  |
| 5 nm ceria dispersion ( $20 \mathrm{wt} . \%$ ) |  |
| Hydrogen peroxide $\left(\mathrm{H}_{2} \mathrm{O}_{2}\right)$ |  |
| Potassium hydroxide $(\mathrm{KOH})$ |  |
| Nitric acid $\left(\mathrm{HNO}_{3}\right)$ |  |
| Polyvinylpyrrolidone (PVP) | Sigma-Aldrich, St. Louis, MO |
| Cetyltrimethylammonium bromide <br> (CTAB) |  |
| 20 nm ceria powder | Sky Spring Nanomaterials, Houston,TX |
| Commercial ceria slurry | NY CREATES, Albany, NY |
| 180 nm thermal oxide on silicon |  |
| 80 nm PECVD nitride on silicon |  |
| Crystalbond ${ }^{\text {TM }}$ adhesive 821-3 | Ted Pella Inc, Redding, CA |
| ChemPol ${ }^{\text {TM }}$ non-woven polishing pad |  |

| $30 \mathrm{~nm} \& 80 \mathrm{~nm}$ colloidal silica | Allied High Tech, Rancho |
| :-- | :-- |
| dispersion | Dominguez, CA |

# 2. Procedures 

To correlate the findings of chemical environment effects on ceria oxidation state with key polishing parameters, the environmental conditions discussed in chapter 3 were investigated as they relate to polishing efficiency. Additional experiments were included to measure the oxide:nitride selectivity of this new ceria slurry.

Slurries were prepared by mixing $0.254 \mathrm{~g}(1.0 \mathrm{wt} . \%)$ ceria abrasives, $0.381 \mathrm{~cm}^{3}$ of $30 \mathrm{wt} . \% \mathrm{H}_{2} \mathrm{O}_{2}$ $(0.5 \mathrm{wt} . \%)$ and $20 \mathrm{~cm}^{3} \mathrm{DI} \mathrm{H}_{2} \mathrm{O}$, after which the volume was adjusted to a final volume of $25 \mathrm{~cm}^{3}$ with $\mathrm{DI} \mathrm{H}_{2} \mathrm{O}$. The pH of the slurry was subsequently adjusted to pH 8 with 0.1 M KOH . Following this, the slurry was placed in a sonication bath for 1 min to ensure proper dispersion of the ceria abrasives.

Polishing samples were prepared through cleaving a 300 mm wafer into coupons with an area of $2.25 \mathrm{~cm}^{2}$. These coupons were attached to a parallel polishing fixture with Crystalbond ${ }^{\mathrm{TM}}$ at 180 ${ }^{\circ} \mathrm{C}$, after which they were cooled to room temperature. After cooling, the fixture was attached to a Multiprep benchtop polisher (Allied High Tech, Rancho Dominguez, CA) modified with a slurry retention system. The coupon was subsequently polished for 1 min with a downforce of $20 \mathrm{kPa} / 2.9 \mathrm{psi}$ and rotation speeds of 40 rpm clockwise (platen), 20 rpm counter-clockwise (head) and 8 rpm (oscillation). After polishing, the coupon was reheated to $180^{\circ} \mathrm{C}$ to remove it

from the polishing head and underwent a two-step post-polish clean. The first step was an acetone wash to remove residual Crystalbond ${ }^{\mathrm{TM}}$ from the back of the coupon. The second step was performed using a mixture of $\mathrm{H}_{2} \mathrm{O}_{2} / \mathrm{KOH}$ at a ratio of $2: 3$ to remove any ceria abrasives that may be chemically bound to the surface. This ratio was found to be most effective for cleaning ceria particles that are small and/or highly chemically active off oxide surfaces [60].

The $\mathrm{R}_{\mathrm{Z}}$ and $\mathrm{R}_{\mathrm{RMS}}$ of the thermal oxide on silicon wafers were measured through profilometry and AFM respectively. The MRR for thermal oxide and PECVD nitride on silicon were both measured through ellipsometry. In this technique, the difference in phase $(\Delta)$ between the light that reflects off of the wafer surface and that which reflects off the buried silicon surface can be used to determine the thickness for films up to a few $\mu \mathrm{m}$ thick [73]. Unfortunately, these measurements are complicated by the complex optical constants of the material as the light passes through it. Both the amplitude of the light, $\Psi$, and refractive index of the material, n, must be taken into account as well to determine the true thickness of a film. Other complexities include transparency of the film, optical properties of the substrate and surface roughness [113]. Due to a large change in absorption of the underlying silicon substrate after its bandgap ( $>1100$ nm ) [114], the upper limit of the fitting was set to 1000 nm . Both oxide and nitride films are transparent with extinction coefficients of $\mathrm{k} \cong 0$ over the wavelengths measured (250-1000 nm) [115], [116]. This reduces the equation for complex refractive index (equation 4.1) to just the real component of refractive index (equation 4.2).

$$
\begin{gathered}
\underline{n}=n+I k \\
\underline{n}=n
\end{gathered}
$$

With this simplification, fitting of optical constants will have physical meaning even if the relation between the real and imaginary components is not contained in the model (Kramers-Kronig relations) [117]. The final complication, roughness, effectively lowers the refractive index of the film at the surface, altering the value for thickness that is calculated. To account for this, an approximation known as the effective medium approximation (EMA) is used [118]. This assumes that there is a layer of material on the surface of a film of unknown thickness that is $50 \%$ the material being measured and $50 \%$ air. This layer will have a refractive index that is a mix of the measured material and air $(\mathrm{n}=1)$.

The fitting procedure used is determined by the material that is being measured. For thermal oxide fitting the most commonly used fitting procedure is the Cauchy equation (equation 4.3) [119]. For these fitting procedures, C was set to zero as it is only important at very small wavelength [120]. This reduces the equation to that shown in equation 4.4.

$$
\begin{gathered}
n(\lambda)=A+\frac{B}{\lambda^{2}}+\frac{C}{\lambda^{4}}+\cdots \\
n(\lambda)=A+\frac{B}{\lambda^{2}}
\end{gathered}
$$

With this reduced Cauchy equation, the two constants A and B determine the minimum refractive index and how quickly the refractive index increases with decreasing wavelength

respectively. The complete analysis profile has three layers consisting of silicon substrate/Cauchy silicon oxide/EMA and the terms being fit include thickness, A and B.

The fitting procedure for the PECVD nitride film is much more complicated. Silicon nitride films contain crystalline regions which undergo crystal field splitting [121]. As such, fits of this material require multiple oscillators to model their dispersion characteristics and are not meaningfully fit by the Cauchy equation. To fully model this material, the Cauchy equation is replaced with the much more general Lorentz oscillator equation (equation 4.5) that describes the imaginary component of the refractive index in the form of the imaginary dielectric function $\varepsilon_{2}(E)[122]$.

$$
\varepsilon_{2}(E)=A_{T}\left(E-E_{\beta}\right)^{2} / E^{2}
$$

Where $\mathrm{A}_{\mathrm{T}}$ is a fitting parameter and $\mathrm{E}_{\mathrm{g}}$ is the optical band gap. To account for the differences in energy due to crystal field splitting, the Tauc density of states equation (equation 4.6) is combined with equation 4.5. This equation describes the imaginary part of the dielectric function for all valence and conduction band states.

$$
\varepsilon_{2}(E)=2 n k=\frac{A_{L} E_{0} C E}{\left(E^{2}-E_{0}^{2}\right)^{2}+C^{2} E^{2}}
$$

In this equation, $\mathrm{A}_{\mathrm{L}}$ is a different fitting parameter, $\mathrm{E}_{0}$ is the peak transition energy and C defines the broadening. The combined form of these equations known as the Tauc-Lorentz model (equation 4.7) and was first proposed in 1996 to model the imaginary part of the refractive index.

To determine the real part of the refractive index, the Kramer-Kronig relation mentioned earlier is used to relate the imaginary component of the dielectric function $\varepsilon_{2}(E)$ to the real component $\varepsilon_{1}(E)$ (equation 4.8 ).

$$
\begin{aligned}
\varepsilon_{2}(E) & =\left[\frac{A E_{0} C\left(E-E_{g}\right)^{2}}{\left(E^{2}-E_{0}^{2}\right)^{2}+C^{2} E^{2}} \times \frac{1}{E}\right], E>E_{g} \\
\varepsilon_{1}(E) & =\varepsilon_{1}(\infty) \frac{2}{\pi} P \int_{E_{g}}^{\infty} \frac{\xi \varepsilon_{2}(\xi)}{\xi^{2}-E^{2}} d \xi
\end{aligned}
$$

In the first equation (4.7), the previous $\mathrm{A}_{\mathrm{T}}$ and $\mathrm{A}_{\mathrm{L}}$ fitting parameters are combined into a single term denoted A. Additionally, equation 4.8 introduces the new variables $\varepsilon_{1}(\infty)$ and P . The former is the real dielectric function as energy approaches infinity while the latter is the Cauchy principle value of the integral. This complete analysis profile has four layers consisting of silicon substrate/native silicon oxide/Tauc-Lorentz silicon nitride/EMA. The extra native oxide layer is added to account for any oxide that may have grown on the surface of the wafer between cleaning and nitride deposition. The terms that are fit for these equations include thickness, $\mathrm{E}_{\mathrm{g}}$, $\mathrm{E}_{0}, \varepsilon_{1}(\infty), \mathrm{C}$ and A . In practice both $\mathrm{E}_{\mathrm{g}}$ and $\varepsilon_{1}(\infty)$ are made constant with values determined by the material and only thickness, $\mathrm{E}_{0}, \mathrm{C}$ and A are fit.

# C. Results and discussion 

## 1. Effect of peroxide

Given that the particles used for the model slurries were larger than the nominal average of the commercial slurry ( 68 nm vs. 40 nm ), a slightly higher MRR but also greater roughnesses were anticipated. In addition, all of the model slurries created had higher $\mathrm{Ce}^{3+}$ percentages than the commercial slurry, further increasing the anticipated MRR of the model slurries. Figure 4.2 shows the performance comparison between the commercial slurry and four formulations of model slurry, each with increasing peroxide content. Even without peroxide, the model slurry's MRR was double that of the commercial slurry, and was further increased by adding peroxide, as demonstrated in figure 4.2a. The model slurry with the highest $\mathrm{Ce}^{3+} \%$, corresponding to $0.5 \mathrm{wt} . \% \mathrm{H}_{2} \mathrm{O}_{2}$, polished 5.5 times faster than the commercial slurry, which cannot be explained by the slightly larger particle size alone. The MRR for the model slurries follows the change in $\mathrm{Ce}^{3+} \%$ as a function of oxidizing agent concentration as reported in the previous chapter. This result supports Cook's tooth-comb model, where increasing $\mathrm{Ce}^{3+}$ sites will increase MRR [57].

![img-36.jpeg](images\img-36.jpeg)

Figure 4.2. Effect of $\mathrm{H}_{2} \mathrm{O}_{2}$ concentration on the a) MRR of ceria slurries and the b) post-polish oxide surface ( $\mathrm{R}_{\mathrm{Z}}$ and $\mathrm{R}_{\mathrm{RMS}}$ ). The trends in MRR and roughness for the model slurries closely match the trends for $\mathrm{Ce}^{3+} \%$ presented in chapter 3 .

Most of the slurries improved the coupon's surface finish (fig. 4.2b). In this figure, the dashed black line represents the $\mathrm{R}_{\mathrm{Z}}$ before polishing, while the purple bars are the $\mathrm{R}_{\mathrm{Z}}$ after polishing. Similarly, the dashed red line shows the $\mathrm{R}_{\mathrm{RMS}}$ before polishing and the orange bars show the $\mathrm{R}_{\mathrm{RMS}}$ after polishing. The slurry with no peroxide was the worst performer; not only did it result in significantly higher long-range roughness than the commercial slurry, it was also the only slurry that worsened the roughness relative to the unpolished case. The addition of $0.5 \% \mathrm{H}_{2} \mathrm{O}_{2}$ showed the best results, while higher concentrations of peroxide resulted in surface roughnesses comparable to those achieved by the commercial slurry.

Surprisingly, the slurry with the highest MRR also has the lowest $\mathrm{R}_{\mathrm{Z}}$ and $\mathrm{R}_{\mathrm{RMS}}$, which runs contrary to the conventional relationship expected based on particle size [123]. Since these results occur despite using a larger particle size than the commercial slurry, chemical removal

must be the main driving force behind roughness improvements and further investigation into the chemical removal mechanism is required.

Chemical removal occurs through condensation followed by ripping the condensed silicate off of the wafer surface. Since cerium and silicon have similar oxygen bond strengths, the number of bonds remaining between this silicate and the wafer surface is crucial in determining whether a condensed silicate remains attached to the wafer surface or the particle surface (and thus is removed). Specifically, silicate removal increases as the number of bonds to the wafer surface decreases. Such a situation may occur if, for example, there is a scratch or other asperity on the oxide surface. The edges of this feature will have fewer surface bonds, making the silicates at those asperities more vulnerable to chemical removal by the ceria. In this way chemical removal with ceria selectively polishes asperities, thereby reducing roughness.

# 2. Effect of pH 

The pH of the slurry will affect both the chemical and mechanical MRRs. Since the chemical removal of thermal oxide with ceria occurs through condensation reactions, these MRRs are greatest when one material is charged and the other is at its isoelectric point [84]. For the materials in this system the isoelectric point values are 2-3 [56] (thermal oxide) or 8 [102] (ceria), suggesting maximal removal will occur at these two points. If the polishing is performed at pH 2-3, the mechanical removal will be hampered because it relies on hydrolysis of the thermal oxide. The ability of thermal oxide to hydrolyze is a function of pH , and does not become appreciable until the pH is greater than 7 [56]. The hydrolysis rate at the isoelectric point of the thermal oxide will therefore be low and non-uniform, and subsequent mechanical removal

will be similarly non-uniform, resulting in poor surface quality. Therefore, the isoelectric point of ceria, pH 8 , should be the target for this polishing system. The commercial slurry, for comparison, had a pH of 7.8 .

Figure 4.3 details the impact of pH on the MRR and surface finish of the polished coupons for slurries made with 68 nm particles. Of these model slurries, both low and high pH resulted in MRR $(\sim 20 \mathrm{~nm} / \mathrm{min})$, about 4 times that of the commercial slurry (fig. 4.3a). At pH 6 , the MRR is low because the pH is both below the threshold for hydrolysis and away from the isoelectric point of either material, consistent with the model described above.
![img-37.jpeg](images\img-37.jpeg)

Figure 4.3. Effect of slurry pH on the a) MRR of ceria slurries and the b) post-polish oxide surface ( $\mathrm{R}_{\mathrm{Z}}$ and $\mathrm{R}_{\mathrm{RMS}}$ ). MRR and roughness values are strongly affected by pH due to the pH dependent nature of ceria's chemical removal mechanism. The pH 8 slurry gave the best combination of MRR and roughness.

Figure 4.3b describes the impact of pH on surface roughness. As before, the dashed lines indicate the pre-polishing values for the coupon. The pH 4 slurry has very high $\mathrm{R}_{\mathrm{Z}}$ values, significantly worse than the commercial ceria and other model slurries despite having a similar MRR. This $\mathrm{R}_{\mathrm{Z}}$ value is indicative of the significant pitting which occurred on all coupons polished at this pH due to low hydrolysis rates (fig. 4.4). This pitting may have artificially increased the MRR values reported for this slurry, as that calculation was based on the assumption of uniform removal averaged across the full coupon area.
![img-38.jpeg](images\img-38.jpeg)

Figure 4.4. Optical images of the surface of a thermal oxide coupon post-polish with a) a pH 4 ceria slurry and b) a pH 8 ceria slurry. The color of a thermal oxide film is a strong indicator of film thickness. The color shifts from light blue to dark blue to violet as the thickness decreases [124]. The speckled nature of coupon a) demonstrates the pitting present on the film.

The pH 8 slurry has both a lower $\mathrm{R}_{\mathrm{Z}}$ and, more importantly, a lower $\mathrm{R}_{\mathrm{RMS}}$ than the pH 10 slurry. It can be construed that at pH 8 a slurry results in a much smoother surface for a given particle size. The main difference between these two slurries is the type of removal that is maximized at

each pH . On the one hand, the hydrolysis of silica increases by a factor of 4 between pH 8 and 10. This increase in hydrolysis will result in a higher MRR since fewer impacts will be necessary for a large silicate to form and be removed by the turbulent motion of the slurry. On the other hand, the chemical removal is affected by two factors: the previously discussed condensation reactions and hydrolysis, and the zeta potential of the two materials. As the pH increases from 8 to 10 the zeta potential of ceria doubles [125]. With the silica surface already having a negative potential, both materials strongly repel each other at these pH levels, resulting in much lower chemical removal. Thus, the pH 10 slurry, despite having an overall MRR similar to pH 8 , does not have sufficient chemical removal to counteract asperities that may be formed through mechanical removal. The pH 8 slurry, by contrast, having high chemical removal which selectively attacks the vulnerable silicates at the edge of asperities, as described in the previous section, results in significantly better surface quality, locally and globally.

# 3. Effect of particle size 

Traditionally, roughness has been improved by moving to smaller particle sizes at the expense of MRR [11], [76], [77]. The roughness improvements demonstrated earlier in this chapter indicated that I may be able to forgo these MRR losses while obtaining comparable roughness results. To test this, our standard slurry containing 68 nm ceria particles was compared to slurries made with 20 nm and 5 nm particles. All three slurries were adjusted to pH 8 using the concentration of peroxide needed to reach their maximum $\mathrm{Ce}^{3+} \%[9]$.

Figure 4.5a shows a decrease in MRR with decreasing particle size as expected, although all of them were comparable or better than the 50 nm commercial slurry. This emphasizes the

importance of maximizing $\mathrm{Ce}^{3+} \%$. In particular, a particle that is $1 / 10^{\text {th }}$ the size of the commercial slurry, which should have a commensurately decreased mechanical removal component, can have a comparable total MRR due to the enhanced chemical effect enabled by a maximized $\mathrm{Ce}^{3+} \%$.
![img-39.jpeg](images\img-39.jpeg)

Figure 4.5. Effect of abrasive size on the a) MRR of ceria slurries and the b) post-polish oxide surface ( $\mathrm{R}_{\mathrm{Z}}$ and $\mathrm{R}_{\mathrm{RMS}}$ ). By maximizing the chemical and mechanical polishing with ceria, the slurry with 68 nm particles has higher MRR and equivalent roughness to slurries made with smaller ceria particles.

By the same token, while one would expect a larger particle size to achieve a higher MRR at the expense of surface roughness, Figure 4.5 b illustrates that the $\mathrm{R}_{\mathrm{Z}}$ and $\mathrm{R}_{\mathrm{RMS}}$ for all three particle sizes are within error of each other, and better than the commercial slurry, due to the chemical removal enabled by maximizing the $\mathrm{Ce}^{3+} \%$ on the surface of the particles.

# 4. Effect of Surfactants 

Surfactants often result in a decrease in MRR, but can increase the shelf life of the slurry either by ensuring particles stay dispersed in the solvent or by restricting agglomeration once flocculation occurs to promote redispersability. Based on the results from chapter 3, it was hypothesized that the linear surfactants, which caused a greater drop in $\mathrm{Ce}^{3+} \%$ than the micellular surfactants, would have the same relative effect on the MRR and roughness. The surfactants tested included CTAB as a micellular type and PVP as a linear type.

Surprisingly, the polishing experiments determined that the surfactant influence was the opposite of what was expected from the response of $\mathrm{Ce}^{3+} \%$ to surfactants in the previous chapter (fig. 4.6). The micellular surfactant reduced the material removal of our best slurry to that of the commercial one, corresponding to an $80 \%$ decrease in material MRR.

![img-40.jpeg](images\img-40.jpeg)

Figure 4.6. Effect of surfactant on the a) MRR of ceria slurries and the b) post-polish oxide surface ( $\mathrm{R}_{\mathrm{Z}}$ and $\mathrm{R}_{\mathrm{RMS}}$ ). The micellular surfactant dramatically decreased MRR and increased the roughness of the oxide. These effects were much less pronounced when a linear surfactant was used.

At the same time, the roughness values approached double that of the commercial slurry, corresponding to a surface roughness twice that of an unpolished wafer. In contrast, the linear surfactant only decreased material removal by $30 \%$, and had the same effect on roughness as the commercial slurry.

To explain this contradiction with our $\mathrm{Ce}^{3+} \%$ data, both the mechanism for surfactant binding and chemical removal must be evaluated. As discussed in chapter 3, CTAB forms micelles and can only bind to the surface of a ceria particle with a limited number of head groups (fig. 4.7a). This leaves many exposed $\mathrm{Ce}^{3+}$ sites for further chemical binding. On the other hand, PVP can bind multiple times along the length of polymer as it wraps itself around the ceria particle, leaving fewer exposed $\mathrm{Ce}^{3+}$ sites (fig. 4.7b).

![img-41.jpeg](images\img-41.jpeg)

Figure 4.7. Conceptual depiction of ceria particles (blue) covered in a) micellular or b) linear surfactants (orange). The size of the micellular surfactants adhered to the ceria surface prevent condensation reactions from occurring. The difference in size between the ceria particles and the surfactant (micelle or mono-layer) is drawn to scale.

While initially this would suggest higher chemical removal could be expected with CTAB, the mechanism for chemical removal requires that the $\mathrm{Ce}^{3+}$ site must be close enough to the oxide surface to undergo a condensation reaction. The physical size of the micelle sterically hinders this reaction from taking place, limiting the removal mechanism of slurries to the purely mechanical process, albeit with a particle of larger effective size than the initial 68 nm ceria particle. Assuming a single layer of micelles, the size of the particle will increase by $\sim 11.7 \mathrm{~nm}$ for slurries with CTAB [126]. When coated in PVP the particle size will increase by $0.1-0.4 \mathrm{~nm}$ depending on orientation and bond lengths. During polishing, this surfactant coating will be compressed or sheared from the particle or wafer surface but quickly reforms after the particle leaves [127]. With this consideration taken into account, the results of low material removal and high roughness for slurries with micellular surfactants is equivalent to polishing with a silica slurry of $\sim 80 \mathrm{~nm}$, which has no chemical removal and only mechanical effects. Repeating this polishing experiment with a mix of silica particles of 30 and 80 nm to simulate purely

mechanical removal does in fact give results that are similar to the micellular surfactant slurry (fig. 4.8). The smaller particles in the mixture have little effect on material removal and are instead added to improve roughness. As such the material removal can be reasonably attributed to the 80 nm particles in both the silica slurry and the micellular surfactant ceria slurry.
![img-42.jpeg](images\img-42.jpeg)

Figure 4.8. Comparison between the MRR of 68 nm ceria with 5 nm micellular surfactants to 80 nm silica. Without the ability to form condensation bonds with the oxide surface, the slurry can only remove material through mechanical means.

# 5. Selectivity measurements 

Since the selective removal of oxides over nitrides is an important desired advantage of ceria slurries, additional experiments were conducted to ensure that previous improvements in MRR were not obtained at the expense of selectivity. For these tests, SiN wafers were polished using the commercial slurry and the model slurry with the best mix of MRR and roughness properties ( $1.0 \mathrm{wt} . \% 68 \mathrm{~nm}$ ceria, $0.5 \mathrm{wt} . \% \mathrm{H}_{2} \mathrm{O}_{2}, \mathrm{pH} 8$ ).

The chemical removal of nitrides by ceria is a two-step process. Repeated abrasive impacts on the nitride surface along with incorporation of $\mathrm{H}_{2} \mathrm{O}$ eventually results in hydrolysis of the nitride and the formation of a sub-oxide layer on the surface. This layer will be subsequently removed chemically by the same mechanism as the oxide (equation 1.3 and 1.4) [112], [128]. Since hydrolysis is the limiting step, increasing the chemical MRR would cause an increase in the nitride MRR, but not to the same extent as the increase in oxide MRR. This outcome was confirmed in figure 4.9, where the nitride was polished 2.25 x faster with the model slurry but the oxide was polished 5.5 x faster. This results in an increase in the oxide to nitride selectivity of the polishing from nearly $1: 1$ with the commercial slurry to $3: 1$ with the model slurry. Thus, the improvements to silica polishing in both rate and roughness can be achieved without sacrificing, but indeed enhancing, selectivity.
![img-43.jpeg](images\img-43.jpeg)

Figure 4.9. Effect of slurry improvements on the selectivity of oxide to nitride MRR. Since hydrolysis is the limiting step in nitride polishing, improving ceria's chemical removal has a much lower effect on nitride removal than oxide removal, increasing the selectivity of the slurry.

# D. Conclusions 

The knowledge obtained regarding the mechanism for altering the $\mathrm{Ce}^{3+} \%$ on the ceria surface was successfully used to create slurries with higher MRR and better nitride selectivity than slurries that are currently being used in industry [129]. The MRR increases obtained through peroxide additions confirm that the concentration of $\mathrm{Ce}^{3+}$ on the ceria surface is a key factor for increasing MRR. An unexpected consequence of maximizing this chemical removal is that roughness was also improved, allowing us to use larger particles than would traditionally be desirable and increasing the mechanical removal without sacrificing surface finish.

# V. Improved Ceria Slurry for Metal Polishing 

## A. Introduction

While STI and ILD CMP discussed in the preceding chapter had different integration challenges, the oxide that was being polished was similar. In contrast, metal CMP refers to the polishing of a variety of materials each with unique challenges for both slurry design and polishing performance. The most common metals polished in semiconductor CMP are tungsten in the contacts between the FEOL and BEOL and copper lines in the BEOL, with their associated barrier/liner materials [50]. These are typically nitride barriers to prevent diffusion of metal into the dielectric and thin metal liners to promote adhesion of the bulk metal to the diffusion barrier. Tungsten uses a barrier/liner of titanium (TiN/Ti), while copper uses tantalum (TaN/Ta). Thus, 'metal CMP' includes not only the initial and final polishing steps discussed for oxide CMP, but an additional step for liner CMP. In more recent years both cobalt and ruthenium have been researched for use in the BEOL. These metals again provide their own unique challenges for CMP. Both metals are possible replacements for the Ta liners or copper seed layers needed for electrochemical deposition (ECD) of copper as well as for a complete replacement for copper fill at the smallest lines [130]-[133]. Metal CMP challenges arise because each metal has its own polishing characteristics due to its unique hardness, oxidizability, reactivity and hydrolysis rate. To account for these differences, each slurry is designed with chemicals and pH values which target the metal of interest. While most of the complications during metal CMP (WIWNU, scratches, planarity) were discussed in the preceding chapter, new problems arise due to the additional chemicals necessary for oxidation and removal of these materials, as well as the need to polish patterned structures having multiple materials exposed to the polishing media at the same time. These two issues are discussed next in more detail [51], [109].

In metal CMP, the chemicals added to a slurry are necessary to achieve high MRRs. This reliance on chemistry can be detrimental to the final surface roughness because of the polycrystalline nature of the metals, which was not an issue for the isotropic, amorphous oxide discussed previously. In particular, the chemical MRR of a crystalline material is determined by the grain orientation of the surface. The surface of a single metal line is made up of many grains along its length. The lower the surface energy of the grain, the more resistant it is to chemical removal. In the case of copper, a (111) surface will be removed at a lower rate than other surfaces [134], [135]. When a scratch is made on a metal surface, this problem is compounded as crystal planes are exposed at the edges and along the faces of the scratch. These facets undergo preferential chemical attack, causing local MRRs to be higher than at other points along the grain surface. Thus, the chemicals necessary to achieve high MRRs result in orientation-dependent removal which can be detrimental to the final surface roughness. This further incentivizes the creation of slurries with low scratch formation, to avoid such a complication.

The exposure of multiple materials is again an issue not seen in the CMP of blanket oxide. However, in the BEOL manufacturing step, the oxide is patterned, and the barrier/liner completely coats the wafer surface (as conformally as possible) after its deposition. The remaining recesses are filled with metal, usually with a significant overburden (excess) beyond the bare minimum fill (fig. 5.1b). To electrically isolate these wires, the overburden is removed through metal CMP down to the tops of the wires/vias. Once the final polish nears its end point, the liner will be exposed at the spaces between the wires, on top of the interlayer dielectric (fig. 5.1c).

![img-44.jpeg](images\img-44.jpeg)

Figure 5.1. Schematic representation of a metal CMP process. After a) lines are etched into the dielectric (blue), a barrier/liner (grey) conformally coats the surface followed by a metal fill (orange) with significant overburden b). This overburden is polished with a slurry formulated for metal polishing until the barrier/liner is exposed as show in c). At this point, d) a slurry for barrier polish is used to remove the barrier/liner in the spaces between the wires. This barrier polish often results in some loss of thickness in both the metal and oxide.

The final polish must immediately stop at this point to prevent dishing in the lines or contacts. This dishing can be more pronounced than in oxide CMP due to the targeted removal of metal by the chemical additives in the slurry and the lower polishing rate of the (hard) nitride-based liner material. This necessitates the switch to a barrier polish slurry that will remove both the barrier and liner at the same rate as the metal (fig. 5.1d). In addition, as the contact points between these different metals are exposed, galvanic corrosion due to the chemicals in the slurry may occur [51]. This corrosion is most notable when cobalt is used as a seed layer for copper deposition. The cobalt between the tantalum liner and the copper line will be etched away preferentially resulting in a convex line surface with a protrusion of the barrier/liner on either side. In more

extreme cases, the cobalt can be fully corroded in spots giving the appearance of a copper line that is floating inside its trench (fig. 5.2). To combat these problems, barrier polish has less of a focus on chemical removal than the other steps in metal CMP.
![img-45.jpeg](images\img-45.jpeg)

Figure 5.2. a) SEM image of a copper wire that has undergone galvanic corrosion with STEM b) and EELS c) images of the interface. SEM images d) of a copper wire where the cobalt liner has been completely corroded, leaving copper 'floating' in the trench [136].

In semiconductor manufacturing, basic initial and final metal polishing occurs through a twostep process. In the first step, chemicals will react with the metal surface to convert it to a metal oxide. Oxides typically are less mechanically and chemically stable than their zero-valent forms.

After this conversion, material will be removed mechanically by slurry abrasives (typically silica) as the second step.

Some metals, most notable copper, require additional chemicals to achieve high MRRs. The addition of these chemicals expands the removal mechanism to a four-step process (fig. 5.3) [51]. Steps one and two (fig. 5.3a and b) are identical to other metals, but the removal is primarily chemical. This is a result of the high reactivity between copper oxide and complexing agents such as glycine, and an increase in hardness as copper oxidizes decreasing the mechanical MRR [137]. This chemical removal proceeds rapidly in an uncontrollable manner once an oxide surface is formed. Consequently, inhibiting agents are added to create a passivated surface on the metal to slow and control chemical removal (fig 5.3c). This passivated surface is chemically strong but mechanically weak and can be removed by the abrasive to expose the bare metal for further oxidation (fig. 5.3d) [138]. This cycle of oxidation, chemical removal, passivation, mechanical removal repeats until polishing is completed.

![img-46.jpeg](images\img-46.jpeg)

Figure 5.3. Schematic of metal CMP cycle. The metal surface is oxidized a) to ease chemical removal b). To slow the rate of chemical removal an inhibitor creates a passive surface c) that can only be removed by mechanical abrasion d) to return the surface to its initial state. Many metals only require steps a and b during polishing.

The most common oxidizing agent used in metal CMP is $\mathrm{H}_{2} \mathrm{O}_{2}$ [139]. This suggests an easy compatibility with the ceria slurries created in part 1 , where $\mathrm{H}_{2} \mathrm{O}_{2}$ was shown to improve the ability of ceria slurries to chemically abrade silica surfaces. Since the $\mathrm{H}_{2} \mathrm{O}_{2}$ in our improved ceria slurries would form a metal oxide surface to react with, we believed these slurries will chemically polish metals through the same tooth-comb model as silica. This offered an opportunity to extend the tooth-comb model for polishing silica to the more general polishing of an oxide with a cation center. For metals to be removed in this manner, three parameters must be taken into account: the metal-oxygen bond strength, the metal oxide isoelectric point, and the extent of hydrolysis of the metal oxide. The first is an intrinsic property of the metal and could be used as a first pass to rule out metal oxides that would not be polished through this mechanism. The latter two parameters can be used to determine the best slurry pH for chemical and mechanical removal.

To explore this possibility, three metals of interest to the semiconductor industry were tested: copper, tungsten and ruthenium. Copper is the material of choice for metal lines and vias; tungsten is used as the connection between the transistors (FEOL) and the metal lines (BEOL); and ruthenium is used as a barrier material as well as being a promising future replacement for copper in the smallest metal lines. All three metals satisfy the criteria of (1) lower oxygen bond strength than cerium, (2) an isoelectric point that differs from that of ceria, and (3) effective hydrolysis near one of the isoelectric points in the system (Table 5.1).

Table 5.1 Parameters for effective polishing through the tooth-comb mechanism

| Material | Oxygen Bond Strength <br> (eV/bond) [58] | Isoelectric Point (pH) | High Rate of <br> Hydrolysis (pH) |
| :-- | :--: | :--: | :--: |
| Ceria | 8.24 | $8[102]$ | - |
| Copper | 3.56 | $9.5[140]$ | $7-8.5[141]$ |
| Tungsten | $6.13-6.67$ | $2[142]$ | $<2[143]$ |
| Ruthenium | 4.99 | $4.2-5.3[144]$ | $>7[145]$ |

Based on the values from the table, the best pH values for the three polishing slurries are 8,2 and 8 respectively. Aside from these parameters, there may be metal-specific considerations to their slurry design. For example, the addition of complexing agents and inhibitors to copper polishing slurries could have an effect on the $\mathrm{Ce}^{3+} \%$ of the ceria particles. However, the additional chemical removal afforded by the complexing agent might be able to outweigh the loss in chemical removal from decreasing $\mathrm{Ce}^{3+} \%$. The main consequence of this change would be an increase in the post-polish surface roughness, as the removal by complexing agent is not

localized to a particle surface. These chemicals will exacerbate asperities as described earlier as well as preferentially remove small grains and those without (111) orientation. The additional complexing agents are not used in slurries for polishing tungsten and ruthenium, which only contain abrasives and oxidizing agents. This simplifies the transition from silica to ceria abrasives for polishing these two metals. Lastly, in the case of ruthenium there is one other consideration, which is the potential to form the toxic gas $\mathrm{RuO}_{4}$ in acidic $\mathrm{pH}[146]$; however, the slurry design factors cited above are already avoiding this regime.

The final consideration for slurry design is differences between the two abrasive materials themselves. The lack of chemical removal by silica particles was discussed previously. Other key factors are the dispersibility of the particles and their cost. While ceria particles can rapidly settle out of solution, silica particles are easily dispersed for long periods of time [107]. Besides reducing need for surfactants, the higher dispersibility of silica particles also results in a higher allowable abrasive concentration in a silica slurry than in a ceria slurry. The second point, the price of the abrasive, is important from a business perspective because the abrasives make up the largest component of slurry cost. While cerium is not a particularly scarce material, silicon is the second most abundant element on Earth after oxygen (66 [1]vs 282,000 ppm [147]). As such, colloidal silica particles cost roughly $0.07 \$ / \mathrm{g}$ while ceria particles of comparable size can cost between $0.14-0.70 \$ / \mathrm{g}$ (calculations based upon commercial slurry prices at time of writing). This price differential would have a noticeable impact on evaluating the viability of ceria slurry despite any improved performance it may exhibit.

These last two points suggest that the assessment of a ceria slurry as a replacement for silica slurry in metal CMP should be determined on a per-cost basis rather than, say, comparing slurries with the same abrasive loading by weight fraction. Since ceria costs up to 10x what silica costs, that same-price comparison means the model ceria slurries should be compared with silica slurries that contain ten times greater abrasive concentration. As with part 3, the metrics for polish quality included MRR, long-range surface roughness $\left(\mathrm{R}_{\mathrm{Z}}\right)$ and short-range surface roughness ( $\mathrm{R}_{\mathrm{RMS}}$ ). The MRR was measured through the mass lost during polishing and converted to $\AA / \mathrm{min}$ using the area of the coupon polished $\mathrm{A}\left(\mathrm{cm}^{2}\right)$, the density of the metal $\rho\left(\mathrm{g} / \mathrm{cm}^{3}\right)$, the difference in mass before and after polishing $\Delta \mathrm{m}(\mathrm{g})$, and the polishing time $\mathrm{t}(\mathrm{min})$ through the following equation.

$$
M R R=\frac{\Delta m}{4 \rho t} \cdot 10^{8}
$$

Equation 5.1

# B. Materials and Methods 

1. Materials

Table 5.2 Chemicals used during metal polishing experiments

| Chemical name | Manufacturer |
| :--: | :--: |
| 68 nm ceria powder |  |
| Hydrogen peroxide $\left(\mathrm{H}_{2} \mathrm{O}_{2}\right)$ |  |
| Potassium hydroxide $(\mathrm{KOH})$ |  |
| Nitric acid $\left(\mathrm{HNO}_{3}\right)$ |  |
| Glycine |  |
| Benzotriazole (BTA) | Sigma-Aldrich, St. Louis, MO |
| 200 nm ruthenium on silicon <br> $\left(\rho=12.45 \mathrm{~g} / \mathrm{cm}^{3}\right)$ | Tokyo Electron (TEL) |
| Tungsten foil ( $99.97 \% \mathrm{~W}$, <br> $\rho=19.25 \mathrm{~g} / \mathrm{cm}^{3}$ ) | Plansee Reutte, Austria |
| Copper foil (110 Alloy, $99.9 \% \mathrm{Cu}$, <br> $\rho=8.94 \mathrm{~g} / \mathrm{cm}^{3}$ ) | McMaster-Carr Elmhurst, IL |
| Crystalbond ${ }^{\text {TM }}$ adhesive 821-3 | Ted Pella Inc, Redding, CA |
| ChemPol ${ }^{\text {TM }}$ non-woven polishing pad | Allied High Tech, Rancho |
| 30 nm \& 70 nm colloidal silica <br> dispersion ( 25 wt.\% silica) | Dominguez, CA |

# 2. Procedures 

Ceria slurries were prepared by mixing $0.254 \mathrm{~g}(1.0 \mathrm{wt} . \%)$ ceria abrasives, $0.381 \mathrm{~cm}^{3}$ of $30 \mathrm{wt} . \%$ $\mathrm{H}_{2} \mathrm{O}_{2}(0.5 \mathrm{wt} . \%)$ and $20 \mathrm{~cm}^{3} \mathrm{DI} \mathrm{H}_{2} \mathrm{O}$, after which the volume was adjusted with $\mathrm{DI} \mathrm{H}_{2} \mathrm{O}$ to reach a final volume of $25 \mathrm{~cm}^{3}$. Additional chemicals in the form of Glycine and BTA were added at a concentration of 0.01 M in the case of copper polishing. The pH of the slurry was subsequently adjusted to pH 8 for ruthenium and copper with 0.1 M KOH and pH 2 for tungsten with 0.1 M $\mathrm{HNO}_{3}$. Following this the slurry was placed in a sonication bath for 1 min to ensure proper dispersion of the ceria abrasives. Silica slurries were prepared by dilution of the $25 \mathrm{wt} . \%$ dispersion to the desired concentration followed by pH adjustments as well as the addition of BTA and glycine and/or $\mathrm{H}_{2} \mathrm{O}_{2}$ to model commercial slurries for each metal.

Ruthenium thin film samples for polishing were prepared from a 300 mm wafer by cleaving into coupons with an area of $2.25 \mathrm{~cm}^{2}$. Copper and tungsten foil samples were prepared by cutting squares with the same area. The samples were subsequently attached to a parallel polishing fixture with Crystalbond ${ }^{\mathrm{TM}}$ at $180^{\circ} \mathrm{C}$, after which they were cooled to room temperature. After cooling, the head was attached to a Multiprep benchtop polisher (Allied High Tech, Rancho Dominguez, CA) modified with a slurry retention system. The sample was subsequently polished for 1 min with a downforce of $20 \mathrm{kPa} / 2.9 \mathrm{psi}$ and rotation speeds of 40 rpm clockwise (platen), 20 rpm counter-clockwise (head) and 8 rpm (oscillation).

After polishing, the coupon was reheated to $180^{\circ} \mathrm{C}$ to remove it from the polishing head and underwent a two-step post-polish clean. The first step was an acetone wash to remove residual Crystalbond ${ }^{\mathrm{TM}}$ from the back of the coupon. The second step was performed using a cleaning

solution unique to each metal to remove any ceria abrasives that remained chemically bound to the surface. Tungsten cleaning used the same $\mathrm{H}_{2} \mathrm{O}_{2} / \mathrm{KOH}$ with a 2:3 ratio solution as was used for cleaning silica [60]. Ruthenium cleaning was performed with a solution of 0.2 M Citrate at pH 9 [148] and copper cleaning was performed with a $3 \mathrm{wt} . \% \mathrm{HNO}_{3} / 5 \mathrm{mM}$ BTA solution [141]. Following cleaning, the final mass (MMR) of the coupons was measured along with the short $\left(\mathrm{R}_{\mathrm{RMS}}\right)$ and long $\left(\mathrm{R}_{\mathrm{Z}}\right)$ range roughness.

# C. Results and discussion 

## 1. Ruthenium polishing

To polish the ruthenium, the best performing ceria slurry from Chapter 4 and a standard silica slurry were first compared at equal abrasive concentration of $1.0 \mathrm{wt} . \%$. While our ceria slurry at this concentration contains $0.5 \mathrm{wt} . \% \mathrm{H}_{2} \mathrm{O}_{2}$, a silica slurry for ruthenium polishing contains $3.0 \mathrm{wt} . \% \mathrm{H}_{2} \mathrm{O}_{2}$ [44]. The abrasives in these slurries are either 68 nm for ceria or a mix of 80 and 30 nm for silica (fig. 5.4).

![img-47.jpeg](images\img-47.jpeg)

Figure 5.4. SEM images of a) 68 nm ceria particles and b) a mix of 80 nm and 30 nm silica particles. The mixture of two particle sizes is used to obtain high MRR with the large particles while eliminating asperities with the small particles.

Though an equal concentration comparison results in slurries with very different cost, it does give insight into the magnitude of enhancement in the chemical removal provided by ceria particles (fig. 5.5).

![img-48.jpeg](images\img-48.jpeg)

Figure 5.5. Performance comparison polishing ruthenium films with silica and ceria slurries having equal abrasive content by weight. a) MRR and b) roughness ( $\mathrm{R}_{\mathrm{Z}}$ and $\mathrm{R}_{\mathrm{RMS}}$ ) show the additional chemical removal provided by the ceria results in improvements of at least 2 x in each metric measured.

The additional chemical removal resulted in an increase in the MRR for ceria slurries by a factor of three (fig. 5.5a). This supports the hypothesis that ceria can polish metals as long as they have been oxidized. The improved MRR was expected due to ceria's polishing action being both mechanical and chemical in nature, instead of the pure mechanical removal that occurs with a silica slurry.

While polishing with a silica slurry did improve the roughness relative to the unpolished Ru , the ceria slurry reduced the roughness even further (fig 5.5b). In this figure, the dashed black line represents the $\mathrm{R}_{\mathrm{Z}}$ before polishing, while the purple bars are the $\mathrm{R}_{\mathrm{Z}}$ after polishing. Similarly, the dashed red line shows the $\mathrm{R}_{\mathrm{RMS}}$ before polishing and the orange bars are the $\mathrm{R}_{\mathrm{Z}}$ after polishing. The ceria improved the surface finish of the ruthenium (fig. 5.5b) by 2 x and 3 x for $\mathrm{R}_{\mathrm{Z}}$ and $\mathrm{R}_{\mathrm{RMS}}$

respectively. These roughness improvements also coincide with a decrease in the $\mathrm{H}_{2} \mathrm{O}_{2}$ content by 6 x when switching from silica to ceria slurries.

As mentioned previously, the 2-3x improvements in polishing metrics at equal abrasive concentration do not balance the 10x increase in cost. As such, a gram-for-gram (equal wt.\%) comparison is not as compelling as a cost-for-cost comparison. Therefore, ceria slurries with lower abrasive concentration were created to account for the impact of cost on slurry adoption. Before polishing with these new slurries, XPS experiments were performed to determine if the effect of $\mathrm{H}_{2} \mathrm{O}_{2}$ wt. $\%$ on $\mathrm{Ce}^{3+} \%$ was linear (fig. 5.6) to ensure that the dilution did not inadvertently impact the polishing efficiency of the ceria nanoparticles.
![img-49.jpeg](images\img-49.jpeg)

Figure 5.6. Effect of $\mathrm{H}_{2} \mathrm{O}_{2}$ on $\mathrm{Ce}^{3+} \%$ at different ceria concentrations. The maximum $\mathrm{Ce}^{3+} \%$ decreased with decreasing abrasive concentration. The relation between $\mathrm{H}_{2} \mathrm{O}_{2}$ wt. $\%$ for maximum $\mathrm{Ce}^{3+} \%$ and ceria concentration is linear. Lines included as guides for the eye only.

The concentration of $\mathrm{H}_{2} \mathrm{O}_{2}$ necessary for maximum $\mathrm{Ce}^{3+} \%$ at $1.0 \mathrm{wt} . \%$ ceria is $0.5 \mathrm{wt} . \%$ or a ratio of 2:1 ceria to $\mathrm{H}_{2} \mathrm{O}_{2}$. This ratio to maximize $\mathrm{Ce}^{3+} \%$ was maintained when the particle concentration was lowered to both $0.5 \mathrm{wt} . \%$ and $0.1 \mathrm{wt} . \%$. The $\mathrm{H}_{2} \mathrm{O}_{2}$ concentrations used to create these slurries were therefore set to $0.25 \mathrm{wt} . \%$ and $0.05 \mathrm{wt} . \%$ respectively. At the same time, the maximum $\mathrm{Ce}^{3+} \%$ decreased as ceria concentration decreased. There are two possible explanations for this change. First, as the "peak width" for maximum $\mathrm{Ce}^{3+} \%$ narrows, the impact of small discrepancies in the $\mathrm{H}_{2} \mathrm{O}_{2} \mathrm{wt} . \%$ during pipetting, such as rounding errors while using a micropipette with $5 \mu \mathrm{~L}$ graduations, will be more noticeable. Secondly, as the concentration of both ceria and $\mathrm{H}_{2} \mathrm{O}_{2}$ decreases, the frequency of collisions between them, and subsequently the rate of reaction, will decrease. This decrease in kinetics would shift the equilibrium between $\mathrm{Ce}^{4+}$ and $\mathrm{Ce}^{3+}$ towards the former leading to less conversion and lower $\mathrm{Ce}^{3+} \%$.

With the slurry design completed, experiments were carried out to compare polishing outcomes of three different concentrations of ceria ( $1,0.5$ and $0.1 \mathrm{wt} . \%$ ) to that of the previous $1.0 \mathrm{wt} . \%$ silica slurry (fig. 5.7).

![img-50.jpeg](images\img-50.jpeg)

Figure 5.7. Performance comparison polishing ruthenium films with 1.0 wt.\% silica or ceria slurries having decreasing abrasive content. All ceria slurries achieved at least 2x the MRR, shown in (a) and roughness improvements shown in (b), over the silica slurry.

As before, the 1.0 wt.\% ceria significantly out-performed the comparable silica. Even more encouraging, however, was the ceria slurry with reduced particle concentration to compensate for the price differential between powders (10:1). This ceria slurry of comparable abrasive cost still provided MRR and roughness improvements that were 2 x that of silica. This reduced-concentration ceria slurry ( $0.1 \mathrm{wt} . \%$ ), was then used as a benchmark to push the comparison further by modifying the silica slurry. In particular, the abrasive concentration of the silica slurry was now increased to determine how much was necessary to achieve the same MRR as that of the reduced-concentration ( $0.1 \mathrm{wt} . \%$ ) ceria slurry (fig. 5.8).

![img-51.jpeg](images\img-51.jpeg)

Figure 5.8. Performance comparison polishing ruthenium films using the reduced-concentration ( $0.1 \mathrm{wt} . \%$ ) ceria benchmark slurry or increasing concentration of silica abrasives, including a) MRR and b) roughness. Only the highest silica concentration, 15 x the reference abrasive cost, obtained MRR or roughness values that approached those of the $0.1 \mathrm{wt} . \%$ ceria.

To achieve a similar MRR as the $0.1 \mathrm{wt} . \%$ ceria, at least $15 \mathrm{wt} . \%$ silica was needed. Additionally, the ceria is still the best-performing of the slurries by post-polish roughness, although the impact is less dramatic than in previous comparisons because of the significantly lower ceria concentration in this slurry than in the previous experiments. The $\mathrm{R}_{\mathrm{Z}}$ values for the silica slurry seem insensitive to concentration, with all silica slurries performing worse than the ceria. The cost-equivalent silica slurry ( $1.0 \mathrm{wt} . \%$ ) had significantly worse $\mathrm{R}_{\mathrm{RMS}}$ than the ceria slurry; when the concentration of silica was increased, the $\mathrm{R}_{\mathrm{RMS}}$ values became equal between silica and ceria. This suggests that the increase in small particle concentration begins to overcome the asperities formed through mechanical removal with large particles, leading to an improved $\mathrm{R}_{\mathrm{RMS}}$. On the other hand, the lower MRR of these particles cannot overcome long

range non-uniformities in polishing, leaving $\mathrm{R}_{\mathrm{Z}}$ unaffected by the increase in silica concentration.

Although the $15 \mathrm{wt} . \%$ silica achieved similar MRR and roughness as the $0.1 \mathrm{wt} . \%$ ceria, this formulation of the silica slurry would cost at least 15 x that of the ceria slurry. This value comparison is simply based on the cost of the abrasive particle; it is expected the true cost of the ceria slurry would be even more economical, as these effects are achieved with $1 / 60^{\text {th }}$ the concentration of $\mathrm{H}_{2} \mathrm{O}_{2}$ required for the equivalently performing silica slurry. This lower $\mathrm{H}_{2} \mathrm{O}_{2}$ concentration also means that the ceria slurry is much more environmentally friendly than the silica slurry. Based on these differences, it can be concluded that the ceria slurry outperforms silica slurries in MRR, roughness, cost, and environmental impact when polishing ruthenium.

# 2. Tungsten polishing 

Tungsten polishing occurs through the same mechanism as ruthenium, with a relatively simple slurry containing some particular concentration of abrasive and $3.0 \mathrm{wt} . \% \mathrm{H}_{2} \mathrm{O}_{2}$ [149]. The main difference from the other slurries discussed so far is that slurries for tungsten polishing must be acidic to properly hydrolyze the metal. This hydrolysis is strongly affected by pH , with the rate increasing dramatically with decreasing pH and only achieving significant removal at a $\mathrm{pH} \leq 2$ (fig. 5.9).

![img-52.jpeg](images\img-52.jpeg)

Figure 5.9. Tungsten MRR using $1.0 \mathrm{wt} . \%$ ceria slurry at three different pH values: a) 4 , b) 2 and c) 1.8. As the pH approaches 2 removal begins to occur and the rate accelerates as the pH is decreased further.

With a pH of 4 , the mass removed within the 1 min polishing time was undetectable within the error of the microbalance. This polishing experiment was repeated for 1 hr and a MRR of $\sim 4 \AA / \mathrm{min}$ was obtained. Based on this value, while decreasing from pH 2 to 1.8 increases the MRR by a factor of 2 , decreasing the pH from 4 to 1.8 results in a 300x increase in the MRR. While the pH is above 2, no hydrolysis can occur and the abrasive particles are polishing tungsten oxide through solely mechanical removal. In this situation the relative hardnesses (table 5.3) of the particulate and the metal oxide must be considered to understand the MRR results. Because ceria is similar in hardness to tungsten oxide, it is difficult for ceria nanoparticles to mechanically abrade the surface. In this situation it would be much more cost effective to switch to a harder abrasive such as silica or alumina.

Table 5.3 Hardness of different metal CMP materials using the common Mohs scale along with approximate Vickers scale values.

| Material | Mohs hardness | Vickers hardness $\left(\mathbf{k g} / \mathbf{m m}^{\mathbf{2}}\right)$ |
| :-- | :--: | :--: |
| Ceria | 6 | $817[150]$ |
| Silica | 7 | $1161[151]$ |
| Alumina | 9 | $1800[137]$ |
| Tungsten oxide | 5.7 | $726[152]$ |

However, once the pH is lowered enough for hydrolysis to occur, the incorporation of water into the metal oxide lattice both lowers the hardness and more importantly, breaks the subsurface bonds that were preventing chemical removal by ceria. With the addition of chemical removal, ceria can now challenge the MRRs obtained with the harder silica particles while achieving roughness improvements (fig. 5.10) similar to those that were seen in the polishing of ruthenium.

![img-53.jpeg](images\img-53.jpeg)

Figure 5.10. Effect of abrasive concentrations on tungsten MRR at pH 1.8. Pairs of bars represent ceria and silica concentrations of equal cost (low, medium and high abrasive concentrations shown). Silica is more effective at low concentrations but becomes less effective relative to ceria as the abrasive concentration increases.

At low abrasive concentrations, the mechanical removal by silica is able to greatly outpace the combined chemical and mechanical removal by ceria. As the concentration of the abrasive increases, the number of impacts with the oxide surface increases, leading to greater mechanical removal. Additionally, this greater mechanical removal has a synergistic effect on the chemical removal. Greater mechanical removal leads to more asperities. These asperities create surfaces with fewer surface bonds that are more easily removed chemically. Due to this increased rate of both mechanical and chemical removal, ceria slurries exhibit a more dramatic increase in MRR with abrasive concentration than the silica slurries do. At the middle concentration, the MRRs for both slurries become equal, while at the highest concentration ceria gives double the MRR of silica. At this concentration, the chemical MRR of ceria is great enough to offset the higher mechanical MRR of silica.

Unlike the concentration-dependent MRR results, the roughness of tungsten post-polish is always better with ceria than silica, at all three concentration levels (fig. 5.11).
![img-54.jpeg](images\img-54.jpeg)

Figure 5.11. Roughness of a tungsten foil after being polished by a) ceria or b) silica abrasives. Roughness generally decreases as abrasive concentration increases. Ceria abrasives produce smoother surfaces at all concentration levels.

Similar to the case of ruthenium polishing, the added chemical removal provided by ceria abrasives results in a lower roughness than with silica particles and their purely mechanical removal. Additionally, the increased rate of chemical removal at higher abrasive concentrations increases the gap in $\mathrm{R}_{\mathrm{RMS}}$ between silica and ceria from a $25 \%$ improvement to $60 \%$. Unlike the case of ruthenium polishing, however, tungsten polishing with the ceria slurry is only preferable to silica slurry at mid to high concentrations of abrasive. As a result, the $\mathrm{H}_{2} \mathrm{O}_{2}$ concentration for a better performing ceria slurry would only be $1 / 12^{\text {th }}$ the concentration of the equal abrasive cost

silica slurry. This is a decrease in the $\mathrm{H}_{2} \mathrm{O}_{2}$ cost improvements by a factor of 5 when switching abrasive material.

# 3. Copper polishing 

The final metal that was polished, copper, uses a more complicated slurry. This slurry contains a complexing agent, glycine, and an inhibitor, BTA. While copper oxide is harder than copper metal, 160 vs $40 \mathrm{~kg} / \mathrm{mm}^{2}$ respectively [137], the rate of mechanical removal of metallic copper is low. The addition of these chemicals creates a copper oxide surface that is mechanically strong but chemically reactive. Though the mechanical polishing is suppressed, the chemical polishing introduced achieves high MRR of copper through the 4-step mechanism described schematically in figure 5.1. The specific chemistry of this slurry system is described next [51].

When the copper surface is oxidized, two glycine molecules come together at the copper surface to remove a copper atom as a complexed ion (fig. 5.12). This reaction is fast and attacks any exposed copper oxide surfaces uncontrollably. Clearly this is undesirable from an engineering standpoint.
![img-55.jpeg](images\img-55.jpeg)

Figure 5.12. Complexation of copper oxide with glycine. Depending on the pH of the system, the resulting copper complex may have different ionization states.

To control the rate of this complexation reaction, BTA is added to form a chemically inert passivation layer (fig. 5.13). This passivation layer has a hardness less than that of metallic copper. This low-hardness surface is easily polished mechanically by the abrasive to create a fresh metallic copper surface to oxidize.
![img-56.jpeg](images\img-56.jpeg)

Figure 5.13. Passivation of a copper oxide surface with the inhibitor BTA. The film formed through these repeated $\mathrm{N}-\mathrm{Cu}$ bonds is chemically inert but mechanically weak. The fused six and five member rings would align themselves parallel to the copper surface.

These additional chemicals create new challenges for slurry design, but also interesting possibilities as an additional design variable for tailored performance. To explore this possibility, the impact of glycine and BTA on our key performance metrics was studied next.

Glycine was a possible surfactant tested in Chapter 3, although it was tested at a greater concentration ( $0.5 \mathrm{wt} . \%$ ) than what is typically found in slurries ( $0.01 \mathrm{M}(\sim 0.075 \mathrm{wt} . \%$ )) for copper polishing. At that high concentration, it was found to decrease $\mathrm{Ce}^{3+} \%$. BTA also decreases the $\mathrm{Ce}^{3+} \%$ of the ceria particles. When creating a Cu CMP slurry, the addition of glycine and BTA reduced the high $\mathrm{Ce}^{3+} \%$ we had previously relied on from the optimized $26 \%$ back to the $12 \%$ found in the unimproved slurry (fig. 5.14).

![img-57.jpeg](images\img-57.jpeg)

Figure 5.14. XPS analysis of slurry containing $1.0 \mathrm{wt} . \% \mathrm{CeO}_{2}$ and $0.5 \mathrm{wt} . \% \mathrm{H}_{2} \mathrm{O}_{2}$ both a) without and b) with the addition of 0.01 M BTA and glycine. With the addition of glycine surface $\mathrm{Ce}^{3+}$ sites are blocked and the available $\mathrm{Ce}^{3+} \%$ is reduced from a) $26 \%$ to b) $12 \%$, equivalent to the $\mathrm{Ce}^{3+} \%$ found in slurries with no $\mathrm{H}_{2} \mathrm{O}_{2}$.

The silica slurry controls used for copper polishing contain silica abrasive along with $1.0 \mathrm{wt} . \%$ $\mathrm{H}_{2} \mathrm{O}_{2}$ and 0.01 M concentrations of both glycine and BTA. This $\mathrm{H}_{2} \mathrm{O}_{2} /$ glycine/BTA system has been used for most of the lifetime of copper in semiconductors and is still the most dominant commercial method for Cu CMP [141]. When comparing between ceria and silica with the same polishing system (i.e., all other slurry components identical), the MRR with ceria was on average 1.8 x that of silica at each equivalent abrasive cost point (fig. 5.15a).

![img-58.jpeg](images\img-58.jpeg)

Figure 5.15. Performance comparison of ceria and silica abrasives on the polishing of copper using the $\mathrm{H}_{2} \mathrm{O}_{2} /$ glycine/BTA system. a) MRR for low, medium and high abrasive concentrations, with each pair of bars representing equal abrasive cost. b) Post-polish surface roughness ( $\mathrm{R}_{\mathrm{Z}}$ and $\mathrm{R}_{\mathrm{RMS}}$ ) for the highest ceria concentration and cost-equivalent silica concentration slurries. Though the MRR was 1.8 x greater with ceria than silica, the suppression of ceria chemical removal by glycine limited the roughness improvements to equal or less than the comparable silica concentration.

The trade-off for this high MRR is, as mentioned previously, a suppression of the chemical removal mechanism of the ceria abrasives. With a lower ceria chemical removal, the selfcorrecting nature of these large particles with regards to asperities will also be suppressed. This results in both long- and short-range roughness values that are equal to or slightly worse than those of silica (fig. 5.15b).

Another avenue towards slurry design is to create a cleaner, more cost-effective Cu CMP slurry that can achieve high MRRs without the need for glycine. This in turn eliminates the need for

BTA, reducing the complexity of a Cu CMP slurry to that of the preceding Ru and W CMP slurries. This option was tested next. When glycine and BTA were removed from the system, the MRR with ceria was still higher than that of silica, but lower than that obtained with the $\mathrm{H}_{2} \mathrm{O}_{2} /$ Glycine/BTA system by $\sim 20 \%$. This reduced the average MRR improvements when switching from silica to ceria from the previous 1.8 x to 1.4 x (fig 5.16a).
![img-59.jpeg](images\img-59.jpeg)

Figure 5.16. Performance metrics comparison for polishing of copper using only $\mathrm{H}_{2} \mathrm{O}_{2}$, without glycine and BTA. a) MRR for ceria and silica at low, middle and high concentrations. Each pair of bars represent equal abrasive cost. b) Post-polish surface ( $\mathrm{R}_{\mathrm{Z}}$ and $\mathrm{R}_{\mathrm{RMS}}$ ) for the highest ceria concentration and cost-equivalent silica concentration slurries. In the absence of glycine, the ceria slurry yields a $20 \%$ lower MRR, but still out-performs the silica abrasive, while giving improvements in short range roughness.

Again, unlike the other materials studied in this dissertation, this lower copper polishing rate comes with an improvement in post-polish roughness (fig 5.16b). While the $\mathrm{R}_{\mathrm{Z}}$ was within error for all concentrations tested, the $\mathrm{R}_{\mathrm{RMS}}$ improvements ranged from $40-70 \%$ with ceria as the concentration of abrasives increased, compared to the flat $50 \%$ increase with silica.

These two avenues for developing ceria Cu CMP slurry, i.e., ceria slurry either with or without glycine/BTA, offer improvements over the standard silica Cu CMP slurry and the flexibility to tailor slurry for different stages of the process within a particular family of chemistries. For example, on the smallest lines, low roughness is much more important than high MRR, whereas with the large lines some roughness improvements could be sacrificed in exchange for higher wafer throughput. While the improvements may not be as dramatic for copper as for the other metals, the similar nature of these two slurry chemistries along with the others presented both in this and the previous chapter offers an additional advantage if adopted. Namely, the adoption of a single slurry family across multiple CMP steps could simplify the post-CMP cleaning of wafers by reducing the number of cleaning chemistries needed during the fabrication process.

# D. Conclusions 

These improvements to ceria slurry successfully extended the range of materials that can be polished by ceria and has led to the filing of a provisional patent [153]. These slurries achieved some combination of higher MRR and/or lower post-polish roughness for ruthenium, copper and tungsten. The improvements to ruthenium polishing at all price points indicates that ceria slurries are a clear replacement for silica slurries with this metal. Tungsten polishing requires sufficient abrasive concentration to achieve higher MRR, but produces a better surface finish at all

concentrations, indicating its effectiveness as a final polish slurry. Finally, ceria slurry for copper polishing when glycine and BTA are not present has a similar MRR to ruthenium and would be a suitable replacement for all polishing steps. This is a promising result that would be useful for minimizing dishing when polishing copper lines with ruthenium seed layers. If a higher material removal rate is necessary, Glycine/BTA can be added for the initial polish and then the ceria slurry without these chemicals should be used as a final polish step to ensure low roughness.

While ceria was shown to create promising slurries for the different metals tested in this chapter, many factors still remain untested. For example, a greater study on the trade-offs between pH (hydrolysis rate) and condensation reaction rate is needed for each metal to determine the optimal pH for metal polishing. The need for a surfactant must also be addressed in all slurries, with W CMP requiring the most focus. The low pH of this system results in a negatively charged ceria particle that will interact differently with surfactants than many other ceria slurry formulations, where the ceria is neutral to positively charged. Finally, the post-polishing cleaning chemistry requires further study to efficiently remove ceria from the metals post-CMP.

Cu CMP slurries will require their own unique optimization experiments. While both Cu CMP slurries require investigation into the points mentioned above, the ceria $/ \mathrm{H}_{2} \mathrm{O}_{2} /$ glycine/BTA system includes many new chemical interactions. These include the ratio of glycine/BTA to $\mathrm{H}_{2} \mathrm{O}_{2}$, glycine/BTA to ceria, along with the ratio of $\mathrm{H}_{2} \mathrm{O}_{2}$ to ceria when in the presence of glycine/BTA. While intriguing, these questions are beyond the scope of this dissertation and are left, therefore, for future researchers to explore.

# VI. A Final Summary 

While each chapter of experiments has been summarized, with individual conclusions and future directions, they are collected here to emphasize the wholeness of the dissertation topic and present the key findings for the convenience of future readers.

To remedy gaps in the field with regards to the mechanism for ceria CMP, I directly probed the ceria particles themselves through XPS. This work directly measured the effects of chemical environment on $\mathrm{Ce}^{3+} \%$. Each particle had a different initial $\mathrm{Ce}^{3+} / \mathrm{Ce}^{4+}$ ratio determined by their size and synthesis conditions. This ratio was not affected by the pH of the solution that the particles were dispersed in. By introducing $\mathrm{H}_{2} \mathrm{O}_{2}$ to the slurry, the ratio of cation valence state was altered in a predictable way based upon the initial conditions of the particle, owing to the catalase-like reaction of ceria in the presence of $\mathrm{H}_{2} \mathrm{O}_{2}$. Finally, the addition of surfactants reduced the $\mathrm{Ce}^{3+} \%$ of the particles. The extent of the reduction depended on the physical structure of surfactants, which affected the number of surface sites that were blocked. For example, micellular surfactants blocked more sites than linear surfactants, effectively preventing the necessary condensation reactions for CMP. By combining my results with previous literature on the effect of physical parameters and particle-oxide interactions, a more complete understanding of chemical removal by ceria was reached.

The knowledge obtained regarding this mechanism was subsequently used to create slurries for both a traditional polishing target in silicon oxide and novel targets in tungsten, ruthenium and copper. The former during STI and ILD CMP, while the latter three are targets during BEOL CMP. When silicon oxide was polished, the improved ceria slurry had higher MRR and better

nitride selectivity than slurries that are currently being used in industry. The MRR increases obtained through $\mathrm{H}_{2} \mathrm{O}_{2}$ additions confirm that the $\mathrm{Ce}^{3+} \%$ on the ceria surface is a key factor for controlling MRR. An unexpected consequence of maximizing this chemical removal is that roughness was also improved, allowing us to use larger particles than would traditionally be desirable and increasing the mechanical removal without sacrificing surface finish.

When polishing BEOL metals, the improved ceria slurries achieved some combination of higher MRR and/or lower post-polish roughness for ruthenium, copper and tungsten. The abrasive in these slurries, ceria, is as much as 10 x more expensive than the silica abrasive it would replace. To account for this difference, the comparisons between ceria and silica slurries were made with a difference in concentration of 10 x , creating an equal-cost comparison (i.e. $0.1 \mathrm{wt} . \%$ ceria vs. $1.0 \mathrm{wt} . \%$ silica). The improvements to ruthenium polishing at all price points indicates that ceria slurries are a clear replacement for silica slurries with this metal. Tungsten polishing requires sufficient abrasive concentration to achieve higher MRR, but produces a better surface finish at all concentrations, indicating its effectiveness as a final polish slurry. Finally, ceria slurry for copper polishing when glycine and BTA are not present has a similar MRR to ruthenium and would be a suitable replacement for all polishing steps. This is a promising result that would be useful for minimizing dishing when polishing copper lines with ruthenium seed layers. If a higher material removal rate is necessary, Glycine/BTA can be added for the initial polish and then the ceria slurry without these chemicals should be used as a final polish step to ensure low roughness.

While ceria was shown to create promising slurries for the different metals tested in this chapter, many factors still remain untested. For example, a greater study on the trade-offs between pH (hydrolysis rate) and condensation reaction rate is needed for each metal to determine the optimal pH for metal polishing. The need for a surfactant must also be addressed in all slurries, with W CMP requiring the most focus. The low pH of this system results in a negatively charged ceria particle that will interact differently with surfactants than many other ceria slurry formulations, where the ceria is neutral to positively charged. Finally, the post-polishing cleaning chemistry requires further study to efficiently remove ceria from the metals post-CMP.

Cu CMP slurries will require their own unique optimization experiments. While both Cu CMP slurries require investigation into the points mentioned above, the ceria $/ \mathrm{H}_{2} \mathrm{O}_{2} /$ glycine/BTA system includes many new chemical interactions. These include the ratio of glycine/BTA to $\mathrm{H}_{2} \mathrm{O}_{2}$, glycine/BTA to ceria, along with the ratio of $\mathrm{H}_{2} \mathrm{O}_{2}$ to ceria when in the presence of glycine/BTA. While intriguing, these questions are beyond the scope of this dissertation and are left, therefore, for future researchers to explore.

# VII. References 

[1] "Cerium | Ce (Element) - PubChem." https://pubchem.ncbi.nlm.nih.gov/element/58 (accessed Jun. 24, 2020).
[2] "Copper | Cu (Element) - PubChem." https://pubchem.ncbi.nlm.nih.gov/element/29 (accessed Jun. 24, 2020).
[3] "Cerium - MMTA." https://mmta.co.uk/metals/ce/ (accessed Jun. 24, 2020).
[4] "Innovations: Introduction to Copper: Mining \& Extraction." https://www.copper.org/publications/newsletters/innovations/2001/08/intro_mae.html (accessed Jun. 24, 2020).
[5] N. N. Greenwood and A. Eearnshaw, Eds., "30 - The Lanthanide Elements (Z = 58-71)," in Chemistry of the Elements (Second Edition), Second Edi., Oxford: ButterworthHeinemann, 1997, pp. 1227-1249.
[6] J. L. F. Da Silva, "Stability of the Ce2 O3 phases: A DFT+U investigation," Phys. Rev. B - Condens. Matter Mater. Phys., vol. 76, no. 19, pp. 2-5, 2007, doi: 10.1103/PhysRevB.76.193108.
[7] K. Momma and F. Izumi, "VESTA 3 for three-dimensional visualization of crystal, volumetric and morphology data," J. Appl. Crystallogr., vol. 44, no. 6, pp. 1272-1276, 2011, doi: 10.1107/S0021889811038970.
[8] V. Perrichon, A. Laachir, G. Bergeret, R. Fréty, L. Tournayan, and O. Touret, "Reduction of cerias with different textures by hydrogen and their reoxidation by oxygen," J. Chem. Soc. Faraday Trans., vol. 90, no. 5, pp. 773-781, 1994, doi: 10.1039/FT9949000773.
[9] C. M. Netzband and K. Dunn, "Investigation into the Effect of CMP Slurry Chemicals on Ceria Abrasive Oxidation State using XPS," ECS J. Solid State Sci. Technol., vol. 8, no.

10, pp. P629-P633, 2019, doi: 10.1149/2.0311910jss.
[10] P. Janoš, T. Hladík, M. Kormunda, J. Ederer, and M. Štastný, "Thermal treatment of cerium oxide and its properties: Adsorption ability versus degradation efficiency," Adv. Mater. Sci. Eng., vol. 2014, 2014, doi: 10.1155/2014/706041.
[11] L. Wu et al., "Oxidation state and lattice expansion of CeO2-x nanoparticles as a function of particle size," Phys. Rev. B - Condens. Matter Mater. Phys., vol. 69, no. 12, pp. 1-9, 2004, doi: 10.1103/PhysRevB.69.125415.
[12] A. S. Karakoti et al., "Preparation and characterization challenges to understanding environmental and biological impacts of ceria nanoparticles," Surf. Interface Anal., vol. 44, no. 8, pp. 882-889, 2012, doi: 10.1002/sia. 5006.
[13] M. Zarinkamar, M. Farahmandjou, and T. P. Firoozabadi, "One-step synthesis of ceria (CeO2) nano-spheres by a simple wet chemical method," J. Ceram. Process. Res., vol. 17, no. 3, pp. 166-169, 2016.
[14] H. X. Mai et al., "Shape-selective synthesis and oxygen storage behavior of ceria nanopolyhedra, nanorods, and nanocubes," J. Phys. Chem. B, vol. 109, no. 51, pp. 2438024385, 2005, doi: $10.1021 / \mathrm{jp} 055584 \mathrm{~b}$.
[15] J. S. Lee, J. S. Lee, and S. C. Choi, "Synthesis of nano-sized ceria powders by twoemulsion method using sodium hydroxide," Mater. Lett., vol. 59, no. 2-3, pp. 395-398, 2005, doi: 10.1016/j.matlet.2004.09.033.
[16] P. Chen and I. Chen, "Reactive Cerium(IV) Oxide Powders by the Homogeneous Precipitation Method," J. Am. Ceram. Soc., vol. 76, no. 6, pp. 1577-1583, 1993, doi: 10.1111/j.1151-2916.1993.tb03942.x.
[17] D. R. Lide, CRC Handbook of Chemistry and Physics, 87th ed. Boca Raton, FL: CRC

Press, 2006.
[18] M. S. Wickleder, B. Fourest, and P. K. Dorhout, "Thorium," in The Chemistry of the Actinide and Transactinide Elements, Dordrecht: Springer Netherlands, pp. 52-160.
[19] K. Reinhardt and H. Winkler, "Cerium Mischmetal, Cerium Alloys, and Cerium Compounds," in Ullmann's Encyclopedia of Industrial Chemistry, Weinheim, Germany: Wiley-VCH Verlag GmbH \& Co. KGaA, 2000.
[20] "Firestarters - Holtzman's Gorilla Survival." https://holtzmansurvival.com/collections/firestarters (accessed Jun. 25, 2020).
[21] W. Ure, "Meetings of the Society At Vancouver," J. R. Astron. Soc. Canada, vol. 27, p. 264, 1933.
[22] O. US EPA, "EPA History: The Clean Air Act of 1970."
[23] M. V. Twigg, "Controlling automotive exhaust emissions: Successes and underlying science," Philos. Trans. R. Soc. A Math. Phys. Eng. Sci., vol. 363, no. 1829, pp. 10131033, 2005, doi: 10.1098/rsta.2005.1547.
[24] K. Eguchi, T. Setoguchi, T. Inoue, and H. Arai, "Electrical properties of ceria-based oxides and their application to solid oxide fuel cells," Solid State Ionics, vol. 52, no. 1-3, pp. 165-172, 1992, doi: 10.1016/0167-2738(92)90102-U.
[25] D. R. Mullins, "The surface chemistry of cerium oxide," Surf. Sci. Rep., vol. 70, no. 1, pp. 42-85, 2015, doi: 10.1016/j.surfrep.2014.12.001.
[26] B. C. Nelson, M. E. Johnson, M. L. Walker, K. R. Riley, and C. M. Sims, "Antioxidant cerium oxide nanoparticles in biology and medicine," Antioxidants, vol. 5, no. 2, pp. 1-21, 2016, doi: 10.3390/antiox5020015.
[27] X. Wang, Y. Hu, and H. Wei, "Nanozymes in bionanotechnology: From sensing to

therapeutics and beyond," Inorg. Chem. Front., vol. 3, no. 1, pp. 41-60, 2016, doi: 10.1039/c5qi00240k.
[28] D. Merricks, B. Santora, B. Her, and C. Zedwick, "Evolution and revolution of cerium oxide slurries in CMP," Proc. - Electrochem. Soc., vol. PV 2008-1, pp. 531-536, 2008.
[29] T. Yu, Z. Li, and D. Wu, "Predictive modeling of material removal rate in chemical mechanical planarization with physics-informed machine learning," Wear, vol. 426-427, no. February, pp. 1430-1438, 2019, doi: 10.1016/j.wear.2019.02.012.
[30] J. Yi, "On the wafer/pad friction of chemical-mechanical planarization (CMP) processes Part I: Modeling and analysis," IEEE Trans. Semicond. Manuf., vol. 18, no. 3, pp. 359370, 2005, doi: 10.1109/TSM.2005.852101.
[31] "Chem-Pol." https://consumables.alliedhightech.com/Chem-Pol-p/chem.htm (accessed Jun. 29, 2020).
[32] "Precision Surface Wafer Polishing pads." http://www.nanofinishcorp.com/Industrial Products/Wafer Polishing Pads.htm (accessed Jun. 23, 2020).
[33] W. D. Lawson, C. A. Lynch, and J. C. Richards, "Corfam: Research Brings Chemistry to Footwear," Res. Manage., vol. 8, no. 1, pp. 5-26, 1965, doi: 10.1080/00345334.1965.11755739.
[34] D. P. James, "CMP Polishing Pads," in Chemical-Mechanical Planarization of Semiconductor Materials, M. R. Oliver, Ed. New York, NY: Springer, 2004, p. 176.
[35] B. J. Hooper, G. Byrne, and S. Galligan, "Pad conditioning in chemical mechanical polishing," J. Mater. Process. Technol., vol. 123, pp. 107-113, 2002.
[36] D. B. James, "CMP Polishing Pads," p. 178, 2004, doi: 10.1007/978-3-662-06234-0_6.
[37] Y. Nishi and R. Doering, Eds., Handbook of Semiconductor Manufacturing Technology.

New York, NY: Marcel Dekker Inc., 2000.
[38] A. S. Lawing, "Advances in CMP Pad Conditioning," 2015.
[39] M. Y. Tsai, S. T. Chen, Y. S. Liao, and J. Sung, "Novel diamond conditioner dressing characteristics of CMP polishing pad," Int. J. Mach. Tools Manuf., vol. 49, no. 9, pp. 722729, 2009, doi: 10.1016/j.ijmachtools.2009.03.001.
[40] "New BSL CMP Pad Conditioner - EHWA DIAMOND." http://ehwadia.com/portfolio-items/new-bsl-cmp-pad-conditioner/ (accessed Jun. 23, 2020).
[41] "Shinhan Diamond - CMP Pad Conditioner." http://en.shinhandia.co.kr/?post_type=portfolio\&p=7898\&ckattempt=1 (accessed Jun. 23, 2020).
[42] W.-T. Tseng et al., "Microreplicated Conditioners for Cu Barrier Chemical-Mechanical Planarization (CMP)," ECS J. Solid State Sci. Technol., vol. 4, no. 11, pp. P5001-P5007, 2015, doi: 10.1149/2.0011511jss.
[43] "3M ${ }^{\text {TM }}$ Trizact ${ }^{\text {TM }}$ Pad Conditioner B5-M990," no. January, 2016.
[44] K. Yadav, R. Manivannan, and S. Noyel Victoria, "Electrochemical characterization of ruthenium dissolution and chemical mechanical polishing in hydrogen peroxide based slurries," Mater. Today Proc., vol. 18, pp. 1220-1228, 2019, doi: 10.1016/j.matpr.2019.06.584.
[45] H.-P. Feng, J.-Y. Lin, M.-Y. Cheng, Y.-Y. Wang, and C.-C. Wan, "Behavior of Copper Removal by CMP and Its Correlation to Deposit Structure and Impurity Content," J. Electrochem. Soc., vol. 155, no. 1, p. H21, 2008, doi: 10.1149/1.2801394.
[46] M. R. Litchy, D. C. Grant, and R. Schoeb, "Effects of shear and cavitation on particle agglomeration during handling of CMP slurries containing silica, Alumina, and Ceria

particles," 2007 Proc. - 12th Int. Chem. Planarization ULSI Multilevel Interconnect. Conf. C. 2007, pp. 366-375, 2007.
[47] G. Banerjee and R. L. Rhoades, "Chemical Mechanical Planarization Historical Review and Future Direction," no. February 2015, pp. 1-19, 2008, doi: 10.1149/1.2912973.
[48] R. L. Rhoades, "CMP Historical Perspective and Future Outlook Historical Perspective of CMP," 2011.
[49] J.-Y. Lai, "Mechanics, Mechanisms and modeling of the Chemical Mechanical Polishing Process," Massachusetts Institute of Technology, 2001.
[50] K. Buchanan, "The evolution of interconnect technology for silicon integrated circuitry," Proc. Int. Conf. Compd. Semicond. Manuf. GaAsMANTECH2002, vol. 44, no. 0, pp. 1-3, 2002.
[51] S. V. Babu, Ed., Advances in Chemical Mechanical Planarization (CMP). Waltham, MA: Elsevier, 2016.
[52] Scientific America, "Interview with Gordon Moore," pp. 182-182, 1997.
[53] "ICPT Honors Dr. Klaus Beyer for CMP Discovery - Axus Technology," 2015. http://75.103.93.197/newsletter-archive/icpt-honors-dr-klaus-beyer-for-cmp-discovery (accessed Jun. 23, 2020).
[54] O. A. Popov and H. Waldron, "Electron cyclotron resonance plasma stream source for plasma enhanced chemical vapor deposition," J. Vac. Sci. Technol. A Vacuum, Surfaces, Film., vol. 7, no. 3, pp. 914-917, 1989, doi: 10.1116/1.575820.
[55] Smithsonian Chips, "DRAMs." [Online]. Available:
http://smithsonianchips.si.edu/ice/cd/STR97/DRAM.pdf.
[56] R. K. Iler, The Chemistry of Silica: Solubility, Polymerization, Colloid and Surface

Properties and Biochemistry of Silica. New York: John Wiley and Sons, 1979.
[57] L. M. Cook, "Chemical processes in glass polishing," J. Non. Cryst. Solids, vol. 120, no. 1-3, pp. 152-171, 1990, doi: 10.1016/0022-3093(90)90200-6.
[58] T. L. Cottrell, The Strengths of Chemical Bonds, 2nd ed. London, UK: Butterworths Publications Ltd., 1958.
[59] J. M. Werrell et al., "Effect of slurry composition on the chemical mechanical polishing of thin diamond films," Sci. Technol. Adv. Mater., vol. 18, no. 1, pp. 654-663, 2017, doi: 10.1080/14686996.2017.1366815.
[60] J. Seo, A. Gowda, and S. V. Babu, "Almost Complete Removal of Ceria Particles Down to 10 nm Size from Silicon Dioxide Surfaces," ECS J. Solid State Sci. Technol., vol. 7, no. 5, pp. P243-P252, 2018, doi: 10.1149/2.0131805jss.
[61] P. R. Veera Dandu, B. C. Peethala, H. P. Amanapu, and S. V. Babu, "Silicon Nitride Film Removal During Chemical Mechanical Polishing Using Ceria-Based Dispersions," J. Electrochem. Soc., vol. 158, no. 8, p. H763, 2011, doi: 10.1149/1.3596181.
[62] H. Doi, M. Suzuki, and K. Kinuta, "Effects of Ce3+ on Removal Rate of Ceria Slurries in Chemical Mechanical Polishing for SiO2," in 2014 International Conference on Planarization/CMP Technology, 2014, pp. 194-198.
[63] G. Chen, Z. Ni, Y. Bai, Q. Li, and Y. Zhao, "The role of interactions between abrasive particles and the substrate surface in chemical-mechanical planarization of Si-face 6 H SiC," RSC Adv., vol. 7, no. 28, pp. 16938-16952, 2017, doi: 10.1039/c6ra27508g.
[64] S. Kuchibhatla et al., "Influence of aging and environment on nanoparticle chemistry: Implication to confinement effects in nanoceria," J. Phys. Chem. C, vol. 116, no. 26, pp. 14108-14114, 2012, doi: 10.1021/jp300725s.

[65] G. Pulido-Reyes et al., "Untangling the biological effects of cerium oxide nanoparticles: The role of surface valence states," Sci. Rep., vol. 5, pp. 1-14, 2015, doi: 10.1038/srep15613.
[66] J. I. Goldstein, D. E. Newbury, J. R. Michael, N. W. M. Ritchie, J. H. J. Scott, and D. C. Joy, Scanning Electron Microscopy and X-Ray Microanalysis. New York, NY: Springer New York, 2018.
[67] C. A. Schneider, W. S. Rasband, and K. W. Eliceiri, "NIH Image to ImageJ: 25 years of image analysis," Nat. Methods, vol. 9, no. 7, pp. 671-675, 2012, doi: 10.1038/nmeth. 2089 .
[68] Thermo Scientific, "What is XPS." https://xpssimplified.com/whatisxps.php (accessed Jul. 01, 2020).
[69] "EA 125 Energy Analyser User's Guide," vol. 49, no. 2.1, pp. 35-48, 2002, [Online]. Available: http://uhv.cheme.cmu.edu/manuals/M470101.pdf.
[70] R. W. Welker, "Size Analysis and Identification of Particles," in Developments in Surface Contamination and Cleaning: Detection, Characterization, and Analysis of Contaminants, vol. 4, R. Kohli and K. L. Mittal, Eds. Waltham, MA: Elsevier, 2012, pp. 179-213.
[71] M. Krawczyk, M. Holdynski, W. Lisowski, J. W. Sobczak, and A. Jablonski, Electron inelastic mean free paths in cerium dioxide, vol. 341. Elsevier B.V., 2015.
[72] N. Fairley, "CasaXPS." Casa Software Ltd., 2005, [Online]. Available: http://www.casaxps.com/.
[73] J.A. Woollam, "Ellipsometry Tutorial," 2014. https://www.jawoollam.com/resources/ellipsometry-tutorial (accessed Jul. 01, 2020).
[74] B. Voigtländer, "Atomic Force Microscopy Designs," in Springer Series in Geomechanics

and Geoengineering, 2nd ed., Cham, Switzerland: Springer Nature Switzerland AG, 2019, pp. 69-86.
[75] "TESPA-V2 - Bruker AFM Probes."
https://www.brukerafmprobes.com/Product.aspx?ProductID=3844 (accessed Jul. 01, 2020).
[76] S. Kim, R. Merkle, and J. Maier, "Oxygen nonstoichiometry of nanosized ceria powder," Surf. Sci., vol. 549, no. 3, pp. 196-202, 2004, doi: 10.1016/j.susc.2003.12.002.
[77] I. Kosacki, T. Suzuki, H. U. Anderson, and P. Colomban, "Raman scattering and lattice defects in nanocrystalline CeO 2 thin films," Solid State Ionics, vol. 149, no. 1-2, pp. 99105, 2002, doi: 10.1016/S0167-2738(02)00104-2.
[78] W. D. Kingery, H. K. Bowen, and D. R. Uhlmann, Introduction to Ceramics, 2nd ed. New York: John Wiley and Sons, 1976.
[79] M. Nolan, S. Grigoleit, D. C. Sayle, S. C. Parker, and G. W. Watson, "Density functional theory studies of the structure and electronic structure of pure and defective low index surfaces of ceria," Surf. Sci., vol. 576, no. 1-3, pp. 217-229, 2005, doi: 10.1016/j.susc.2004.12.016.
[80] P. P. Dholabhai, J. B. Adams, P. Crozier, and R. Sharma, "Oxygen vacancy migration in ceria and Pr-doped ceria: A DFT+U study," J. Chem. Phys., vol. 132, no. 9, 2010, doi: 10.1063/1.3327684.
[81] J. Kullgren, "Oxygen Vacancy Chemistry in Ceria," Uppsala University, 2012.
[82] O. Bezkrovnyi et al., "The effect of Eu doping on the growth, structure and red-ox activity of ceria nanocubes," CrystEngComm, vol. 20, no. 12, pp. 1698-1704, 2018, doi: 10.1039/c8ce00155c.

[83] B. Rambabu, S. Ghosh, and H. Jena, "Novel wet-chemical synthesis and characterization of nanocrystalline CeO 2 and Ce 0.8 Gd 0.2 O 1.9 as solid electrolyte for intermediate temperature solid oxide fuel cell (IT-SOFC) applications," J. Mater. Sci., vol. 41, no. 22, pp. 7530-7536, 2006, doi: 10.1007/s10853-006-0837-6.
[84] J. T. Abiade, W. Choi, and R. K. Singh, "Effect of pH on ceria-silica interactions during chemical mechanical polishing," J. Mater. Res., vol. 20, no. 5, pp. 1139-1145, 2005, doi: 10.1557/JMR.2005.0176.
[85] J. A. Bearden and A. F. Burr, "Reevaluation of X-ray atomic energy levels," Rev. Mod. Phys., vol. 39, no. 1, pp. 125-142, 1967, doi: 10.1103/RevModPhys.39.125.
[86] M. Cardona and L. Ley, Eds., Photoemission in Solids I, vol. 26. Berlin, Heidelberg: Springer Berlin Heidelberg, 1978.
[87] Thermo Scientific, "XPS Knowledge Base: Cerium." https://xpssimplified.com/elements/cerium.php (accessed Jul. 06, 2020).
[88] M. Romeo, K. Bak, J. El Fallah, F. Le Normand, and L. Hilaire, "XPS Study of the reduction of cerium dioxide," Surf. Interface Anal., vol. 20, no. 6, pp. 508-512, 1993, doi: 10.1002/sia. 740200604 .
[89] P. S. Bagus, R. Broer, W. A. de Jong, W. C. Nieuwpoort, F. Parmigiani, and L. Sangaletti, "Atomic many-body effects for the p-shell photoelectron spectra of transition metals," Phys. Rev. Lett., vol. 84, no. 10, pp. 2259-2262, 2000, doi: 10.1103/PhysRevLett.84.2259.
[90] P. Burroughs, A. Hamnett, A. F. Orchard, and G. Thornton, "Satellite Structure in theXRay Photoelectron Spectra of some Binary and Mixed Oxides of Lanthanum and Cerium By," J. Chem. Soc., Dalt. Trans., no. 1686, pp. 1686-1698, 1976.
[91] A. Platau, L. I. Johansson, A. L. Hagström, S. E. Karlsson, and S. B. M. Hagström,

"Oxidation of cerium and titanium studied by photoelectron spectroscopy," Surf. Sci., vol. 63, no. C, pp. 153-161, 1977, doi: 10.1016/0039-6028(77)90334-X.
[92] E. Paparazzo, "Use and mis-use of x-ray photoemission spectroscopy Ce3d spectra of Ce2O3 and CeO2," J. Phys. Condens. Matter, vol. 30, no. 34, p. 343003, 2018.
[93] N. Răduțoiu and C. M. Teodorescu, "Satellites in Ce 3d X-ray photoelectron spectroscopy of ceria," Dig. J. Nanomater. Biostructures, vol. 8, no. 4, pp. 1535-1549, 2013.
[94] E. Bêche, P. Charvin, D. Perarnau, S. Abanades, and G. Flamant, "Ce 3d XPS investigation of cerium oxides and mixed cerium oxide (Ce xTiyOz)," Surf. Interface Anal., vol. 40, no. 3-4, pp. 264-267, 2008, doi: 10.1002/sia. 2686.
[95] N. M. Houlihan, N. Karker, R. A. Potyrailo, and M. A. Carpenter, "High Sensitivity Plasmonic Sensing of Hydrogen over a Broad Dynamic Range Using Catalytic Au-CeO2 Thin Film Nanocomposites," ACS Sensors, vol. 3, no. 12, pp. 2684-2692, 2018, doi: 10.1021/acssensors.8b01193.
[96] Casa Software Ltd., "Peak Fitting in XPS," 2006. .
[97] D. A. Shirley, "High-resolution x-ray photoemission spectrum of the valence bands of gold," Phys. Rev. B, vol. 5, no. 12, pp. 4709-4714, 1972, doi: 10.1103/PhysRevB.5.4709.
[98] S. Tougaard, "Universality classes of inelastic electron scattering cross-sections," Surf. Interface Anal., vol. 25, no. 3, pp. 137-154, 1997, doi: 10.1002/(SICI)10969918(199703)25:3<137::AID-SIA230>3.0.CO;2-L.
[99] N. Fairely, "CasaXPS Manual 2.3. 15 Getting started with CasaXPS," Casa Softw. Ltd, pp. 1-177, 2009, [Online]. Available:
http://scholar.google.com/scholar?hl=en\&btnG=Search\&q=intitle:CasaXPS+Manual+2.3. 15\#2.

[100] J. H. Scofield, "Theoretical photoionization cross sections from 1 to 1500 keV .," U.S. Atomic Energy Commission, Jan. 1973. doi: 10.2172/4545040.
[101] C. D. Wagner, L. E. Davis, M. V. Zeller, J. A. Taylor, R. H. Raymond, and L. H. Gale, "Empirical atomic sensitivity factors for quantitative analysis by electron spectroscopy for chemical analysis," Surf. Interface Anal., vol. 3, no. 5, pp. 211-225, 1981, doi: 10.1002/sia. 740030506.
[102] K. Osseo-Asare, "Surface Chemical Processes in Chemical Mechanical Polishing," J. Electrochem. Soc., vol. 149, no. 12, p. G651, 2002, doi: 10.1149/1.1516777.
[103] W.-T. Tseng, C. Wu, T. McCormack, and J. C. Yang, "Post Cleaning for FEOL CMP with Silica and Ceria Slurries," ECS J. Solid State Sci. Technol., vol. 6, no. 10, pp. P718-P722, 2017, doi: 10.1149/2.0101710jss.
[104] A. Trovarelli and J. Llorca, "Ceria Catalysts at Nanoscale: How Do Crystal Shapes Shape Catalysis?," ACS Catal., vol. 7, no. 7, pp. 4716-4735, 2017, doi: 10.1021/acscatal.7b01246.
[105] P. Ni, X. Wei, J. Guo, X. Ye, and S. Yang, "On the Origin of the Oxidizing Ability of Ceria Nanoparticles," RSC Adv., vol. 5, pp. 97512-97519, 2015, doi: 10.1039/C5RA20700B.
[106] T. Pirmohamed et al., "Nanoceria exhibit redox state-dependent catalase mimetic activity," Chem. Commun., vol. 46, no. 16, pp. 2736-2738, 2010, doi: 10.1039/b922024k.
[107] R. Dylla-Spears, L. Wong, P. E. Miller, M. D. Feit, W. Steele, and T. Suratwala, "Charged micelle halo mechanism for agglomeration reduction in metal oxide particle based polishing slurries," Colloids Surfaces A Physicochem. Eng. Asp., vol. 447, pp. 32-43, 2014, doi: 10.1016/j.colsurfa.2014.01.061.

[108] Tayyab Suratwala, "Lecture 13: Glass Finishing (Grinding \&m; Polishing)," Livermore, California, 2015. [Online]. Available:
https://www.lehigh.edu/imi/teched/GlassProcess/Lectures/Lecture13_Suratwala_Glass_Fi nishing_Lecture_Lehigh.pdf.
[109] M. Krishnan, J. W. Nalaskowski, and L. M. Cook, "Chemical mechanical planarization: Slurry chemistry, materials, and mechanisms," Chem. Rev., vol. 110, no. 1, pp. 178-204, 2010, doi: $10.1021 / \mathrm{cr} 900170 \mathrm{z}$.
[110] L. Y. Wang et al., "Origin of high oxide to nitride polishing selectivity of ceria-based slurry in the presence of picolinic acid," Chinese Phys. B, vol. 20, no. 3, pp. 1-8, 2011, doi: $10.1088 / 1674-1056 / 20 / 3 / 038102$.
[111] P. R. Dandu Veera, S. Peddeti, and S. V. Babu, "Selective Chemical Mechanical Polishing of Silicon Dioxide over Silicon Nitride for Shallow Trench Isolation Using Ceria Slurries," J. Electrochem. Soc., vol. 156, no. 12, p. H936, 2009, doi: 10.1149/1.3230624.
[112] Y. Z. Hu, "Silicon Nitride Chemical Mechanical Polishing Mechanisms," J. Electrochem. Soc., vol. 145, no. 11, p. 3919, 1998, doi: 10.1149/1.1838893.
[113] A. Martin, "Session 1B: Transparent Materials," Philadelphia, Pennsylvania, 2014.
[114] B. Streetman and S. Banerjee, Solid State Electronic Devices, 5th ed. Upper Saddle River, New Jersey: Prentice Hall, 2000.
[115] I. H. Malitson, "Interspecimen Comparison of the Refractive Index of Fused Silica," J. Opt. Soc. Am., vol. 55, no. 10, p. 1205, 1965, doi: 10.1364/josa.55.001205.
[116] S. L. Ku and C. C. Lee, "Optical and structural properties of silicon nitride thin films prepared by ion-assisted deposition," Opt. Mater. (Amst)., vol. 32, no. 9, pp. 956-960, 2010, doi: 10.1016/j.optmat.2010.01.032.

[117] M. Fox, Optical Property of Solids, 2nd ed. New York, NY: Oxford University Press, 2001.
[118] Y. Liu, J. Qiu, and L. Liu, "Applicability of the effective medium approximation in the ellipsometry of randomly micro-rough solid surfaces," Opt. Express, vol. 26, no. 13, p. 16560, 2018, doi: 10.1364/oe.26.016560.
[119] W. Rzodkiewicz and A. Panas, "Application of spectroscopic ellipsometry for investigations of compaction and decompaction state in $\mathrm{Si}-\mathrm{SiO} 2$ systems," J. Phys. Conf. Ser., vol. 181, no. 1, 2009, doi: 10.1088/1742-6596/181/1/012035.
[120] D. Patel, D. Shah, J. N. Hilfiker, and M. Linford, "A Tutorial on Spectroscopic Ellipsometry (SE), 2. The Cauchy Model," Vacuum Technology and Coatings, pp. 29-33, May 2019.
[121] S. Zollner, "Optical constants for metrology of hydrogenated amorphous silicon-nitrogen alloys on Si," vol. 532, no. March 2001, pp. 532-537, 2003, doi: 10.1063/1.1354451.
[122] G. E. Jellison and F. A. Modine, "Parameterization of the optical functions of amorphous materials in the interband region," Appl. Phys. Lett., vol. 69, no. 3, pp. 371-373, 1996, doi: $10.1063 / 1.118064$.
[123] Z. Zhang, W. Liu, and Z. Song, "Particle size and surfactant effects on chemical mechanical polishing of glass using silica-based slurry," Appl. Opt., vol. 49, no. 28, pp. 5480-5485, 2010, doi: 10.1364/AO.49.005480.
[124] "SiO2 color chart for thermally grown silicon dioxide, HTE Labs, sputter deposition services, thin film vacuum deposition,wafer foundry, bipolar process development, contract R\&D, bipolar wafer foundry services, thin film vacuum deposition services." http://www.htelabs.com/appnotes/sio2_color_chart_thermal_silicon_dioxide.htm

(accessed Jul. 10, 2020).
[125] Z. Zhang, L. Yu, W. Liu, and Z. Song, "Surface modification of ceria nanoparticles and their chemical mechanical polishing behavior on glass substrate," Appl. Surf. Sci., vol. 256, no. 12, pp. 3856-3861, 2010, doi: 10.1016/j.apsusc.2010.01.040.
[126] A. Cifuentes, J. L. Bernal, and J. C. Diez-Masa, "Determination of Critical Micelle Concentration Values Using Capillary Electrophoresis Instrumentation," Anal. Chem., vol. 69, no. 20, pp. 4271-4274, 1997, doi: 10.1021/ac970696n.
[127] I. U. Vakarelski, S. C. Brown, G. B. Basim, Y. I. Rabinovich, and B. M. Moudgil, "Tailoring silica nanotribology for CMP slurry optimization: $\mathrm{Ca} 2+$ cation competition in C12TAB mediated lubrication," ACS Appl. Mater. Interfaces, vol. 2, no. 4, pp. 12281235, 2010, doi: 10.1021/am100070e.
[128] W. G. America and S. V. Babu, "Slurry additive effects on the suppression of silicon nitride removal during CMP," Electrochem. Solid-State Lett., vol. 7, no. 12, pp. 327-330, 2004, doi: 10.1149/1.1817870.
[129] C. M. Netzband and K. Dunn, "Controlling the Cerium Oxidation State During Silicon Oxide CMP to Improve Material Removal Rate and Roughness," ECS J. Solid State Sci. Technol., vol. 9, no. 4, p. 044001, 2020, doi: 10.1149/2162-8777/ab8393.
[130] N. A. Lanzillo et al., "Exploring the Limits of Cobalt Liner Thickness in Advanced Copper Interconnects," IEEE Electron Device Lett., vol. 40, no. 11, pp. 1804-1807, 2019, doi: 10.1109/LED.2019.2940869.
[131] M. H. Van Der Veen et al., "Cobalt bottom-up contact and via prefill enabling advanced logic and DRAM technologies," 2015 IEEE Int. Interconnect Technol. Conf. 2015 IEEE Mater. Adv. Met. Conf. IITC/MAM 2015, no. v, pp. 25-27, 2015, doi: 10.1109/IITC-

MAM.2015.7325605.
[132] M. H. Van Der Veen et al., "Damascene Benchmark of Ru, Co and Cu in Scaled Dimensions," 2018 IEEE Int. Interconnect Technol. Conf. IITC 2018, no. c, pp. 172-174, 2018, doi: 10.1109/IITC.2018.8430407.
[133] M. Abe et al., "Highly-oriented PVD ruthenium liner for low-resistance direct-plated Cu interconnects," Proc. IEEE 2007 Int. Interconnect Technol. Conf. - Dig. Tech. Pap., pp. 4-6, 2007, doi: 10.1109/iitc.2007.382331.
[134] L. Vanasupa et al., "Impact of linewidth and line density on the texture of electroplated Cu in Damascene-fabricated lines," Electrochem. Solid-State Lett., vol. 2, no. 6, pp. 275277, 1999, doi: 10.1149/1.1390809.
[135] P. J. Andersen, M. N. Bentancur, A. J. Moll, and M. Frary, "Microstructural Effects during Chemical Mechanical Planarization of Copper," J. Electrochem. Soc., vol. 157, no. 1, p. H120, 2010, doi: 10.1149/1.3254163.
[136] T. Nogami, M. He, X. Zhang, K. Tanwar, R. Patlolla, and J. Kelly, "CVD-Co/Cu(Mn) integration and reliability for 10 nm node," in Interconnect technology conference (IITC), 2013, pp. 1-3.
[137] M. S. Mohebbi and A. Akbarzadeh, "Fabrication of copper/aluminum composite tubes by spin-bonding process: Experiments and modeling," Int. J. Adv. Manuf. Technol., vol. 54, no. 9-12, pp. 1043-1055, 2011, doi: 10.1007/s00170-010-3016-5.
[138] R. Ihnfeldt and J. B. Talbot, "Effect of CMP Slurry Chemistry on Copper Nanohardness," J. Electrochem. Soc., vol. 155, no. 6, p. H412, 2008, doi: 10.1149/1.2903293.
[139] K. Cheemalapati, J. Keleher, and Y. Li, "Key Chemical Components in Metal CMP Slurries," in Microelectronic Applications of Chemical Mechanical Planarization, Y. Li,

Ed. Hoboken, NJ, USA: John Wiley \& Sons, Inc., 2007, pp. 201-247.
[140] E. McCafferty, Acid-Base Properties of Surface Oxide Films. Cham: Springer International Publishing, 2015.
[141] Y. Ein-Eli and D. Starosvetsky, "Review on copper chemical-mechanical polishing (CMP) and post-CMP cleaning in ultra large system integrated (ULSI)-An electrochemical perspective," Electrochim. Acta, vol. 52, no. 5, pp. 1825-1838, 2007, doi: 10.1016/j.electacta.2006.07.039.
[142] M. Anik and T. Cansizoglu, "Dissolution kinetics of $\mathrm{WO}_{3}$ in acidic solutions," J. Appl. Electrochem., vol. 36, pp. 603-608, 2006, doi: 10.1007/s10800-005-9113-8.
[143] R. S. Lillard, "The Nature of Oxide Films on Tungsten in Acidic and Alkaline Solutions," J. Electrochem. Soc., vol. 145, no. 8, p. 2718, 1998, doi: 10.1149/1.1838704.
[144] T. P. Luxton, M. J. Eick, and K. G. Scheckel, "Characterization and dissolution properties of ruthenium oxides," J. Colloid Interface Sci., vol. 359, no. 1, pp. 30-39, 2011, doi: 10.1016/j.jcis.2011.03.075.
[145] I. Povar and O. Spinu, "Ruthenium redox equilibria: 1. Thermodynamic stability of Ru(III) and Ru(IV) hydroxides," J. Electrochem. Sci. Eng., vol. 6, no. 1, p. 123, 2016, doi: 10.5599/jese. 226 .
[146] J. Cheng, T. Wang, J. Pan, and X. Lu, "Corrosion Investigations of Ruthenium in Potassium Periodate Solutions Relevant for Chemical Mechanical Polishing," J. Electron. Mater., vol. 45, no. 8, pp. 4067-4075, 2016, doi: 10.1007/s11664-016-4579-1.
[147] "Silicon | Si (Element) - PubChem." https://pubchem.ncbi.nlm.nih.gov/element/14 (accessed Jul. 15, 2020).
[148] I. Kim, B. Cho, T. Kim, and J. Park, "Development of Post Ru CMP Cleaning Solutions,"

2007. 
[149] G. Lim, J. H. Lee, J. Kim, H. W. Lee, and S. H. Hyun, "Effects of oxidants on the removal of tungsten in CMP process," Wear, vol. 257, no. 9-10, pp. 863-868, 2004, doi: 10.1016/j.wear.2004.02.007.
[150] Q. He, "Experimental study on polishing performance of CeO 2 and nano-SiO 2 mixed abrasive," Appl. Nanosci., vol. 8, no. 1-2, pp. 163-171, 2018, doi: 10.1007/s13204-018-0657-4.
[151] T. Teague, "An improved technique for polishing difficult geological materials using a colloidal silica suspension," J. Sediment. Res., vol. 59, no. 4, p. 635, 1989, doi: 10.2110/jsr.59.635.
[152] N. M. G. Parreira, N. J. M. Carvalho, and A. Cavaleiro, "Synthesis, structural and mechanical characterization of sputtered tungsten oxide coatings," Thin Solid Films, vol. 510, no. 1-2, pp. 191-196, 2006, doi: 10.1016/j.tsf.2005.12.299.
[153] C. M. Netzband and K. Dunn, "Ceria Based Chemical Mechanical Polishing Slurries," U.S. Provisional Pat. Ser. No 62/955,047, 2019.

