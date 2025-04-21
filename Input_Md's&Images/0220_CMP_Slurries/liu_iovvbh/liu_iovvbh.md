# Development of Highly stable ceria slurry in acetic acid-ammonium acetate buffer Media for effective chemical mechanical polishing of silicon dioxide 

Min Liu ${ }^{\mathrm{a}, \mathrm{b}}$, Baoguo Zhang ${ }^{\mathrm{a}, \mathrm{b},{ }^{*}}$, Jihoon Seo ${ }^{\mathrm{c}, * *}$, Wenhao Xian ${ }^{\mathrm{a}, \mathrm{b}}$, Dexing Cui ${ }^{\mathrm{a}, \mathrm{b}}$, Shitong Liu ${ }^{\mathrm{a}, \mathrm{b}}$, Yijun Wang ${ }^{\mathrm{a}, \mathrm{b}}$, Sihui Qin ${ }^{\mathrm{a}, \mathrm{b}}$, Yang Liu ${ }^{\mathrm{a}, \mathrm{b}}$<br>${ }^{a}$ School of Electronic Information Engineering, Hebei University of Technology, Tianjin, 300130, People's Republic of China<br>${ }^{\mathrm{b}}$ Tianjin Key Laboratory of Electronic Materials and Devices, Tianjin, 300130, People's Republic of China<br>${ }^{c}$ Department of Chemical and Biomolecular Engineering, Clarkson University, \#366 CAMP, 8 Clarkson Avenue, Potsdam, NY, 13699, USA

## A R T I C L E I N F O

Keywords:
Ceria
Acetic acid-ammonium acetate buffer solution
Dispersant
Removal rate
Adsorption and dynamic simulation

A B S T R A C T

Shallow trench isolation (STI), as a key technology for device isolation, is commonly planarized with ceria slurry in chemical mechanical polishing (CMP). Due to the ceria particles are easily agglomerated, the stability of ceria slurry is still a key issue at present. In order to obtain excellent polishing performance for dielectric, it is necessary to prepare the ceria slurry with stable dispersion. This paper is to propose a new dispersant based on acetic acid that can improve the stability of ceria slurry. By comparing the dispersibility of acetic acid with that of a formulated acetic acid-ammonium acetate buffer solution, the buffer solution was chosen as more effective dispersant. The addition of buffer solution was more beneficial for the stability of the slurry. After 7 days, the zeta potential of ceria decreased from 46.47 mV to 35.01 mV (decreased about $24.6 \%$ ) with the addition of acetic acid, whereas it decreased from 51.22 mV to 42.19 mV (decreased about $17.6 \%$ ) with the addition of buffer solution. Furthermore, during the CMP process, the removal rate of TEOS was improved (from $621.59 \mathrm{~nm} / \mathrm{min}$ to $694.77 \mathrm{~nm} / \mathrm{min}$ ) along with surface roughness (Ra, from 0.37 nm to 0.07 nm ). The mechanism was characterized using X-ray photoelectron spectroscopy (XPS), UV-vis spectrometer (UV-Vis), and molecular dynamic simulation. The buffer solution increased the concentration of acetate ions in the slurry, which not only enhanced the adsorption between acetate ions and ceria but also promoted the generation of $\mathrm{Ce}^{3+}$ and oxygen vacancy. Furthermore, the free electrons of $\mathrm{Ce}^{3+}$ facilitated the breaking of the $\mathrm{Si}-O-\mathrm{Si}$ bonds through electron transfer, increasing the removal rate of silicon dioxide.

## 1. Introduction

In the advanced fabrication process of chips, Shallow trench isolation (STI) has become a key technology for device isolation which has been widely used in the fabrication of semiconductor devices [1-3]. Silicon dioxide $\left(\mathrm{SiO}_{2}\right)$ dielectric has excellent insulating properties, which improve the reliability and stability of devices, therefore, it is commonly used as the insulating dielectric layer in the STI structure [4,5]. It is well known that the STI structure comprises $\mathrm{SiO}_{2}$ and silicon nitride $\left(\mathrm{Si}_{3} \mathrm{~N}_{4}\right)$ with $\mathrm{SiO}_{2}$ left on top of $\mathrm{Si}_{3} \mathrm{~N}_{4}$. During STI planarization, the dishing of oxide in the trench is often seen. Therefore, the precise removal of the $\mathrm{SiO}_{2}$ layer is critical [6].

Chemical mechanical polishing (CMP) is an important process in integrated circuit manufacturing [7]. It is also an effective method for
achieving full planarization [8]. Currently, CMP has been applied to the planarization of various materials, such as sapphire [9], copper [10], diamond [11], metal, alloy barrier [12,13], and dielectric layer [14].

Currently, a great deal of research has focused on the study of slurries in CMP. The stronger the chemical properties of the slurry, the better the performance of the wafer, which is conducive to reduce the contamination caused by the abrasives after CMP. Sahir et al. [15] investigated the effect of ceria and silica abrasives on the contamination of PVA brushes after CMP. Compared to silica slurries, ceria slurries showed significantly more contamination of brushes compared to silica slurries due to the electrostatic attraction between ceria and brushes. At pH 4.0 , it was found that the effect of gap distance and brush rotation speed on brush contamination was not significant. And the brush contamination increased significantly with the concentration of abrasives increasing.

[^0]
[^0]:    * Corresponding author. School of Electronic Information Engineering, Hebei University of Technology, Tianjin, 300130, People's Republic of China.
    ** Corresponding author.
    E-mail addresses: bgzhang2000@163.com (B. Zhang), jseo@clarkson.edu (J. Seo).

And the contamination of PVA brushes by $0.05 \mathrm{wt} \%$ ceria abrasives was high at a process time of 5 min . Samanta et al. [16] formulated efficient slurries for InGaAs CMP in different pH conditions to maintain removal rates, surface roughness, and abrasive particle contamination. It was found that the removal rate of InGaAs was higher ( $110 \mathrm{~nm} / \mathrm{min}$ ) and with the surface roughness of 1.42 nm when using the alkaline slurry ( pH 10.0 ). The addition of ammonium halide salts to the slurry at pH 10.0 not only further increased the removal rate of InGaAs ( 175 $\mathrm{nm} / \mathrm{min}$ ) and reduced the surface roughness ( $\mathrm{Ra}<0.5 \mathrm{~nm}$ ) with minimal particle contamination.

For STI CMP process, the commonly used slurry is ceria slurry because ceria slurry has a higher removal rate of oxide and nitride surfaces compared to conventional silica slurry [17,18]. However, in an aqueous medium, the large specific surface area and high molecular weight of ceria particles are prone to problems such as inter-particle agglomeration and rapid settling after being formulated into a slurry. This results in the slurry becoming unstable and not conducive to use or storage. Preventing the agglomeration of cerium oxide particles is the key to improving their quality.

The current research on the dispersive suspension properties of ceria slurry mainly focuses on the use of dispersants. It has been widely reported in the literature that additives can improve the dispersion properties of ceria, such as polyacrylic acid (PAA) [19-22], sodium dodecylbenzene sulfonate (SDBS) [23], and poly vinyl pyrrolidone (PVP) [24]. Kim et al. [25] investigated the effect of poly (acrylic acid-co maleic acid) sodium salt (PAMS) on the dispersion of ceria. They found that ceria showed the highest stability at a PAMS concentration of 3.0 wt $\%$. At this concentration, the attractive force between particles was offset by sufficient spatial potential resistance. At lower concentrations, the force of the dispersant was not sufficient to overcome van der Waals gravity, while at higher concentrations, particles tended to agglomerate due to bridging flocculation. Cheng et al. [26] found that the particle size of La/ceria was relatively smaller when using polyacrylamide (PPI) and sodium dodecyl sulfate (SDS) as dispersants. The suspension properties improved with the addition of PVP, and the prepared ceria slurry remained stable at $30^{\circ} \mathrm{C}$ for 7 days.

Other researchers have utilized acidic modifiers to improve the dispersion properties of ceria. Yang et al. [27] used nitric acid as a new dispersant. After wet ball milling at pH 2.0 , the average particle size (D50) of ceria was 230 nm . Xu et al. [28] employed citric acid as a dispersant to obtain a slurry with a zeta potential of -27 mV , which remained stable at pH 5.0 for 24 h . The dispersion of ceria in the wet ball milling environment was also improved by using nitric acid as a new dispersant.

Based on the above analysis, it can be concluded that the purpose of dispersing ceria is primarily achieved through the addition of organic additives and inorganic acids. However, the duration for which ceria remains stabilized is still relatively short. Most slurries still face the problem of settling. At present, fewer studies are using organic acids as dispersants, while this paper conducts a more comprehensive investigation on the use of organic acids.

In this paper, we discuss the use of acetic acid as a dispersant for ceria. A more effective dispersion was achieved using an acetic acidammonium acetate buffer solution, which also helped inhibit the volatilization of acetic acid. Particle size, zeta potential, and SEM measurements revealed that when using acetic acid as the dispersant, the average particle size of cerium oxide abrasive was 266.3 nm before and 289.6 nm after one week, with corresponding zeta potentials of 46.47 mV and 35.01 mV . In contrast, when the acetic acid-ammonium acetate buffer solution was used as the dispersant for one week, the average particle size of cerium oxide abrasive increased from 183.1 nm to 201.5 nm , while the zeta potential decreased from 51.22 mV to 42.19 mV . This comparison indicated that the slurry with the buffer solution exhibited superior dispersion. Moreover, the buffer solution was found to increase the removal rate of $\mathrm{SiO}_{2}$ and improve the surface quality of the wafer. Subsequent mechanism analysis, conducted through XPS and UV-Vis,
revealed that the buffer solution promoted the transfer of $\mathrm{Ce}^{4+}$ to $\mathrm{Ce}^{3+}$ on the ceria surface. An increase in the component of $\mathrm{Ce}^{3+}$ improved the dispersion stability of ceria abrasive and increased the active sites on ceria particles. Molecular dynamics simulations demonstrated that the higher concentration of acetate ions led to more stable adsorption with ceria. Finally, the mechanism behind the removal of $\mathrm{SiO}_{2}$ by buffer solution was investigated.

## 2. Experimental

### 2.1. Materials

The TEOS wafer with a film thickness of 2000 nm were provided by Innotronix Technologies Co., Ltd. The ceria suspension supplied by Shenzhen Juxin Semiconductor Material Co., Ltd, was used for the chemical mechanical polishing of the TEOS. The original pH of the ceria suspension was $9-10$ and the average particle size of the abrasive was about 500 nm . The dispersants and pH adjuster used in this study were acetic acid and a buffer solution. The buffer solution was prepared using acetic acid and ammonium acetate crystals. Acetic acid $\left(\mathrm{CH}_{3} \mathrm{COOH}, 99 \%\right.$ purity) was provided by Tianjin Jiuding Chemical Co., Ltd. Ammonium acetate crystals were provided by Tianjin Kermel Chemical Reagent Co., Ltd.

The acetic acid-ammonium acetate buffer solution was prepared using acetic acid (purity: $99 \%$ ) and ammonium acetate crystals. In this paper, the acetic acid-ammonium acetate buffer solution with pH 3.8 was prepared to adjust the slurry to pH 4.0 , according to Eq. (1):
$\mathrm{pH}=\mathrm{pKa}+\log \frac{\mathrm{c} \text { (ammonium acetate) }}{\mathrm{c} \text { (acetic acid) }}$
in which the pKa of acetic acid was 4.76. It can be calculated that the concentrations of acetic acid and ammonium acetate were $9.12 \mathrm{~mol} / \mathrm{L}$ and $1.0 \mathrm{~mol} / \mathrm{L}$, respectively, to achieve a pH of 3.8 . To prepare a 100 ml buffer solution, 54.72 g of acetic acid and 7.7 g of ammonium acetate were used. Therefore, take a quantity of deionized water, add 7.7 g of ammonium acetate, and stir until dissolved. After that, add 54.72 g of acetic acid to the solution. Finally, add deionized water to adjust the total volume of the buffer solution to 100 ml .

### 2.2. Polishing experiments

In this study, the experiments in this paper were carried out on a RuiXuan SSP-500 polisher, and all experiments were conducted at pH 4.0. The polishing parameters are listed in Table 1.

For the CMP of the TEOS, the concentration of ceria abrasive was $1.0 \%$. The material removal rate (MRR) was calculated by Eq. (2) (Unit: $\mathrm{nm} / \mathrm{min})$.

$$
M R R=\left(h_{7}-h_{0}\right) \times t_{0}
$$

where $h_{0}$ and $h_{1}$ (Unit: nm ) were the thickness of $\mathrm{SiO}_{2}$ film before and after polishing, respectively. Each $h_{0}$ and $h_{1}$ was the average value after three times of measurements, and $t$ is the polishing time ( 20 s ). The thickness of $\mathrm{SiO}_{2}$ film was measured using Filmetrics F50. The surface of the TEOS needs to be rinsed with deionized water for 30 s before and after polishing, and then dried with nitrogen. To ensure the accuracy of MRR, each polishing experiment was repeated three times. The average

Table 1
Polishing parameters.

| parameters | value |
| :-- | :-- |
| Polishing time | 20 s |
| Polishing pressure | 4 psi |
| Slurry flowing rate | $100 \mathrm{ml} / \mathrm{min}$ |
| Polishing head/plate speed | $50 / 50 \mathrm{rpm}$ |

value of the three experimental results was taken as the final value of MRR, and the standard deviation of the three results was taken as the error of MRR.

### 2.3. Characterization measurement

The particle size and zeta potential of ceria abrasives were measured by laser particle size analyzer (NIcomp-380, PSS Inc U.S.A.). The morphology of ceria particles was analyzed using a scanning electron microscope (SEM, Zeiss Sigma500/VP). The surface morphology including scratches and residual ceria particles of TEOS before and after polishing were analyzed by laser scanning confocal microscopy (OLX5000-LAF). The surface roughness of the TEOS was measured using an atomic force microscope (AFM, Agilent 5600LS). X-ray photo electron spectroscopy (XPS, PHI 250Xi) was used to analyze the composition, chemical state, and concentration of elements on the surface of ceria particles. The samples used for XPS were made from TEOS wafer which was cut into small cubes for $1 \mathrm{~cm} \times 1 \mathrm{~cm}$ and immersed in the prepared slurry for 5 min . The characteristic peaks of the absorption spectra on the surface of ceria abrasives were measured using a UV-vis spectrometer (UV-Vis, Lambda $1050+$ spectrometer) after adding different dispersants.

### 2.4. Adsorption and dynamics simulation

The adsorption behavior of acetate ions on the surface of ceria abrasive was simulated using the Forcite module of Material Studio 2019 software. All simulations were carried out in vacuum mode. And the module used for solution modeling is Amorphous cell. The morphology module used the Bravais-Friedel-Donnay-Harker (BFDH) method to estimate the surface morphology of ceria crystals [29]. The adsorption configuration used as the adsorption surface was a $6 \times 6$ supercell crystal model of ceria (1 1 0), which was reserved for a vacuum layer thickness of $40 \AA$. The applied parameters for the Amorphous cell and Forcite are shown in Table 2 and Table 3.

## 3. Results and discussion

### 3.1. Preparation of acetic acid-ammonium acetate buffer solution

The study by Wang et al. demonstrated that acetic acid can serve as an effective dispersant for ceria abrasives. Under acidic conditions, acetic acid ionizes into acetate ions, which adsorb on the surface of ceria particles. This improves the dispersion performance of ceria abrasives through the double electric layer effect [30]. However, the high volatility of acetic acid leads to pH instability in the slurry during the CMP process. Additionally, its strong irritating odor is not conducive to long-duration experiments. The proportion of different ionic forms of acetic acid in an aqueous solution, varying with pH , is shown in Fig. 1. Given that the pKa of acetic acid is 4.76 , in aqueous solutions with a pH below 4.76 , acetic acid predominantly exists as acetic acid molecules. Above a pH of 4.76 , it mainly exists as acetate ions. It is important to note that all the experiments in this study were carried out at a pH of 4.0, very close to the pKa of acetic acid. Fig. 1 indicates that under these conditions, the degree of acetic acid ionization is close to $40 \%$. This implies that about $40 \%$ of acetic acid molecules ionized into acetate ions, thereby contributing to the higher volatility of acetic acid.

Table 2
Amorphous cell parameters for model of solution.

| parameters | value |
| :-- | :-- |
| type of force field | COMPASS II |
| density of solution | $1.13 \mathrm{~g} / \mathrm{cm}^{3}$ |
| number of water molecules | 660 |
| calculation accuracy | Fine |

Table 3
Forcite calculation parameters.

| parameters | value |
| :-- | :-- |
| type of force field | COMPASS II |
| Maximum number of iterations (structural optimization) | 500 |
| calculation accuracy | Fine |

![img-0.jpeg](images\img-0.jpeg)

Fig. 1. The proportion of different ionic forms of acetic acid in aqueous solution along with pH .

According to the ionization formula of acetic acid in Eq. (3), it can be known that when the concentration of acetate ion increases, the ionization of acetic acid can be inhibited, which can decrease the volatilization of acetic acid. Therefore, in this paper, the acetic acid-ammonium acetate buffer solution was prepared, which can inhibit the volatilization of acetic acid.
$\mathrm{CH}_{3} \mathrm{COOH} \mathrm{2CH}_{3} \mathrm{COO}^{-}+\mathrm{H}^{+}$
The buffer solution was prepared by acetic acid (purity: 99\%) and ammonium acetate crystals. It should be noted that in this paper, buffer solution and acetic acid are not only used as a dispersant but also as a pH adjuster for the slurry. This study mainly focused on the dispersion of them. The buffer solution with pH 3.8 was prepared to adjust the pH of the slurry to 4.0 , according to Eq. (1).

Next, the prepared buffer solution was studied for volatility. The remaining volume after volatilization of buffer solution and acetic acid was compared over two weeks, which was the same volume at first. Acetic acid was diluted to the pH of 3.8 , consistent with the pH of the prepared buffer solution. At the same time, 10 ml of acetic acid and buffer solution were taken in a measuring cylinder, and it should be noted that the measuring cylinders used were of the same size. The results of the change in the volume of buffer solution and acetic acid with the number of days are shown in Fig. 2. After two weeks, the amount remaining volume of the buffer solution was 8 ml , while only 4.5 ml of acetic acid remained. It can be concluded that the volume of volatilization of the self-formulated buffer solution is less than that of acetic acid. This indicates that the volatilization of acetic acid can indeed be inhibited by increasing the concentration of acetate ions, and confirms the feasibility of the above method.

### 3.2. Study of dispersion stability

Due to the high surface energy characteristics of ceria, the particles are easily agglomerated with each other. And it is difficult to uniformly

![img-1.jpeg](images\img-1.jpeg)

Fig. 2. The change in volume of buffer solution and acetic acid with pH 3.8 in two weeks.
disperse in deionized water for a long time. The large particle abrasive formed by agglomeration can scratch the wafers during the chemical mechanical polishing process, which seriously affects the efficiency of ceria slurry in practical applications. Therefore, in this paper, the effect of buffer solution and acetic acid on the dispersion stability of ceria suspension was investigated in terms of average particle size and zeta potential experiments. In order to ensure the accuracy of the results, each experiment was repeated three times. The average value of the three results was taken as the final value, and the standard deviation of the three results was taken as the error.

From the previous conclusion, it can be obtained that the prepared buffer solution indeed inhibits the volatilization of acetic acid, and can be considered as a substitute for acetic acid as a dispersant and pH regulator of the ceria suspension. Therefore, the effect of acetic acid and buffer solution on the average particle size of ceria abrasives was investigated. The concentration of ceria abrasives in the suspension was $1.0 \mathrm{wt} \%$ and the pH was adjusted to 4.0 using acetic acid and buffer solution, respectively. Effect of settling time on the average particle size
![img-2.jpeg](images\img-2.jpeg)

Fig. 3. Effect of settling time on the average particle size of ceria abrasives adding different dispersants.
of ceria abrasives adding different dispersants is shown in Fig. 3. It was found that the average particle size of ceria suspension without dispersants is larger ( 512.7 nm ) due to the agglomeration of ceria particles, which increases to 534.3 nm after 7 days. The addition of acetic acid and buffer solution improves the dispersion of ceria suspension. And the average particle size of the ceria abrasives dispersed by buffer solution is smaller than that of which dispersed by acetic acid. When using acetic acid as the dispersant, the average particle size of ceria abrasive increases from 266.3 nm to 289.6 nm after 7 days. When using buffer solution as the dispersant, the average particle size of ceria abrasive increases from 183.1 nm to 201.5 nm after 7 days.

In colloidal processing, the greater the absolute value of the zeta potential, the more charge is on the cerium surface, which results in a longer distance between ceria particles due to repulsive forces. And van der Waals forces are weakened so that the dispersion of ceria abrasives was improved [31]. As shown in Fig. 4, the effect of acetic acid and buffer solution on the zeta potential of the ceria abrasives was studied. The zeta potential of ceria abrasives is 37.89 mV without adding dispersants, which decreases to 29.11 mV after 7 days. It indicates that the dispersion of ceria suspension is poor. After adding acetic acid and buffer solution, respectively, the dispersion of ceria suspension is improved. And the zeta potential of ceria abrasives dispersed by buffer solution is greater than that dispersed by acetic acid. When using acetic acid as the dispersant, the zeta potential of ceria abrasives is 46.47 mV , which decreased to 35.01 mV after 7 days. It indicates that the suspension can maintain the basic dispersion performance. When using the buffer solution as the dispersant, the zeta potential of the ceria abrasive is 51.22 mV at day 0 , which is 42.19 mV at day 7 . It indicates that the suspension has good dispersion stability. As a result, the buffer solution is a more effective dispersion for ceria suspension.

Based on the above analysis of the experimental results of average particle size and zeta potential, it can be determined that the buffer solution is more effective in improving the dispersion of ceria suspension. Therefore, in order to observe more clearly the influence of acetic acid and buffer solution on the distribution of ceria particles at the microscopic level, SEM experiments was carried out on the ceria suspension with and without dispersants added at pH 4.0 , respectively. The result is shown in Fig. 5.

As can be seen in Fig. 5(a1), ceria particle agglomerates without the addition of any dispersant. When the magnification is adjusted to 50,000 times, the measured image is shown in Fig. 5(a2). There is a serious buildup problem between the particles, resulting in a very blurred
![img-3.jpeg](images\img-3.jpeg)

Fig. 4. Effect of settling time on the zeta potential of ceria abrasives adding different dispersants.

![img-4.jpeg](images\img-4.jpeg)

Fig. 5. Effect of different dispersants on the morphology and distribution of ceria abrasives: (a1/a2) without dispersants; (b1/b2) dispersed by acetic acid; (c1/c2) dispersed by buffer solution.
outline of the ceria particles in the image at this point. Longitudinal comparison of Fig. 5(a1), 5(b1), and 5(c1) show that the dispersibility of the ceria abrasive is improved to varying degrees with the addition of both dispersants. By further comparison, it can be seen that when acetic acid is used as the dispersant, there is a slight agglomeration of ceria particles and the size between the particles is not uniform enough. When buffer solution is used as the dispersant, the dispersibility of ceria particles is greatly improved, the size of the particles is uniform, and clear contours and angles of the particles are observed. Therefore, the buffer solution has a more noticeable effect on the dispersion of ceria suspension than acetic acid. In addition, it can be found that the particle size of ceria abrasives is kept around 200 nm after adding the dispersants, while it is smaller when adding the buffer solution.

From the study of average particle size, zeta potential, and SEM, it can be obtained that the improving effect on the dispersion of ceria suspension is better when adding the buffer solution than acetic acid. This is mainly because the buffer solution is formulated by adding ammonium acetate crystals to acetic acid, which increases the concentration of acetate ions, and inhibits the volatilization of acetic acid into the air. Under the effect of electrostatic force, more negatively charged acetate ions are adsorbed on the surface of positively charged ceria particles, increasing the repulsion between ceria particles. After the dispersion of ceria abrasive by the buffer solution, the particles are uniformly dispersed, and also have a small average particle size and high
zeta potential after 7 days. It indicates that the buffer solution enables the ceria suspension to remain stable for a long period of time.

Finally, the removal rate of TEOS by ceria slurry adding acetic acid and buffer solution was studied, as shown in Fig. 6. The concentration of ceria abrasive in the slurry is $1.0 \%$ and the polishing experiments are all carried out at pH 4.0 . When buffer solution is used as the dispersant, the removal rate of the TEOS is $694.77 \mathrm{~nm} / \mathrm{min}$ and $660.35 \mathrm{~nm} / \mathrm{min}$ on day 0 and day 7 , respectively. While using acetic acid as the dispersant, the removal rate of the TEOS is $621.59 \mathrm{~nm} / \mathrm{min}$ and $582.04 \mathrm{~nm} / \mathrm{min}$ on day 0 and day 7 , respectively. It can be concluded that the removal rate of the TEOS after adding buffer solution to the slurry is higher than that of adding acetic acid. It is also further indicated that the buffer solution can replace acetic acid as an effective dispersant in the dispersion of ceria, and the dispersion effect is better than that of acetic acid. In summary, the buffer solution was finally selected as the dispersant and pH adjuster for ceria suspension in this paper.

The effect of different pH under acidic and neutral conditions on the dispersion of ceria suspension and the removal rate of TEOS when adding buffer solution were investigated, as shown in Fig. 7. From Fig. 7 (a) and (b), it can be found that the average particle size of ceria abrasives gradually increases and the zeta potential decreases with the of pH increasing. It indicates that the dispersion of ceria suspension is getting worse. With the pH increasing from 3.0 to 6.0 , the average particle size and zeta potential of ceria change more slowly. However, the average

![img-5.jpeg](images\img-5.jpeg)

Fig. 6. The removal rate of TEOS by ceria slurry after dispersion by acetic acid and buffer solution before and after 7 days.
particle size increases significantly at 7.0 with the zeta potential decreases significantly. It indicates that the dispersion effect of ceria suspension is closer under acidic condition. And under neutral condition, the dispersion effect is poorer. The reason is that the point of zero charge of ceria is 7.9 , and the closer the pH is to 7.9 , the easier the ceria particles are to agglomerate. From Fig. 7(c), it can be found that with the increase of pH , the removal rate of TEOS shows a trend of increasing first and then decreasing. At pH 4.0 , the removal rate is the highest ( 694.77 nm ). Moreover, the removal rate of TEOS decreased significantly at pH
7.0. It indicates that the pH affects the electrostatic force between ceria and silicon dioxide. At pH 4.0 , the electrostatic force is the largest, which accelerates the formation of $\mathrm{Si}-\mathrm{O}-\mathrm{Ce}$ bonds and increases the removal rate of TEOS. Based on the above findings, in order to obtain a higher TEOS removal rate, the optimal pH was finally determined to be pH 4.0 .
3.3. Effect of acetic acid-ammonium acetate buffer solution on the surface morphology of $\mathrm{SiO}_{2}$ wafer (TEOS)

The previous results found that the self-formulated buffer solution can improve the dispersion stability of the ceria slurry and also increase the removal rate of TEOS to some extent. Therefore, the surface morphology of the wafer continued to be further investigated. The surface morphology of the wafer before and after polishing was measured by laser scanning confocal microscopy, and the results are shown in Fig. 8. From Fig. 8(a), it can be seen that there are obvious scratches as well as residual ceria particles on the surface of $\mathrm{SiO}_{2}$ wafer before polishing. From Fig. 8(b), it can be obtained that when acetic acid is used as the dispersant, the surface quality of the $\mathrm{SiO}_{2}$ wafer after polishing by ceria slurry is improved. The scratches become lighter or even disappear, and the residual ceria particles on the surface are also reduced at the same time. From Fig. 8(c), it can be obtained when the buffer solution as the dispersant, the $\mathrm{SiO}_{2}$ wafer surface quality has improved significantly, mainly in the absence of visible scratches on the wafer surface and ceria residues. By comparing the effects of the two dispersants on the surface quality of the wafer, it is found that both have a contributing effect on the improvement of the surface quality, but when the buffer solution is used as the dispersant, the surface quality of the wafer is the best.

In order to further investigate the surface quality of the wafer, the
![img-6.jpeg](images\img-6.jpeg)

Fig. 7. The effect of different pH under acidic and neutral conditions on the dispersion of ceria suspension and the removal rate of TEOS when adding buffer solution: (a) average particle size; (b) zeta penitential; (c) removal rate of TEOS.
![img-7.jpeg](images\img-7.jpeg)

Fig. 8. Images measured by laser confocal microscopy of $\mathrm{SiO}_{2}$ wafer: (a) before polishing; (b) after polishing with acetic acid; (c) after polishing with buffer solution.

surface roughness of the wafer was measured by AFM. The results are shown in Fig. 9. From Fig. 9(a), it can be seen that before polishing, the surface roughness of the $\mathrm{SiO}_{2}$ wafer is 0.37 nm , and the surface is uneven with obvious irregular bumps. When acetic acid is used as the dispersant, the surface morphology of the wafer after polishing is shown in Fig. 9(b) with Sq of 0.18 nm . The surface roughness is reduced and the surface is relatively flat, but scratches can be seen to appear. The surface morphology of the polished wafer with buffer solution as a dispersant is shown in Fig. 9(c), and the Sq is 0.07 nm . The surface quality is better and the roughness is minimized. The surface is flat and there are no scratches and residual ceria particles.

In summary, the combination of laser scanning confocal microscopy and atomic force microscopy measurement studies on the surface of the $\mathrm{SiO}_{2}$ wafer reveals that both dispersants improved the surface quality of the wafer. However, comparing the number of scratches and residual ceria particles, it is found that the self-formulated buffer solution improves the wafer surface quality better than acetic acid. It may be because the addition of buffer solution improves the dispersion of ceria particles and reduces the large particles. The force between the abrasive and the wafer is also more uniform, which improves the surface quality of the wafer. The buffer solution not only improves the dispersion stability of the ceria slurry, but also obtains a higher $\mathrm{SiO}_{2}$ removal rate, and at the same time, it is more capable of obtaining a flat wafer surface, which is of great significance to the chip fabrication process.

### 3.4. Mechanistic analysis through XPS method

In order to investigate the mechanism of action of the acetic acid and buffer solution, the elemental spectra of the following three samples
were measured respectively at pH 4.0 using XPS: (a) $1.0 \mathrm{wt} \%$ ceria, (b) $1.0 \mathrm{wt} \%$ ceria with acetic acid as the dispersant, (c) $1.0 \mathrm{wt} \%$ ceria with buffer solution as the dispersant. XPS is an analytical technique for detecting the composition, chemical state, and concentration of elements on the surface of materials. The results were fitted and analyzed by a software called Avantage. The full spectrum of the elements is shown in Fig. 10 The different element peaks can be assigned for $\mathrm{Si} 2 \mathrm{p}, \mathrm{C}$ 1 s , O 1 s , and Ce 3 d , respectively. By comparing the peak curves of the elemental content on the surface of ceria abrasive after the addition of acetic acid and buffer solution, it can be found that the component of O 1 s decreases and the component of Ce 3 d increases after the addition of acetic acid and buffer solution, and the component of Ce 3 d is higher than that of acetic acid after the addition of buffer solution. It is inferred that the reason why the buffer solution can improve the dispersion and the removal rate is mainly because of the influence of the cerium element.

Fig. 11 shows the fine spectral peak curves of cerium elements of samples on the ceria surfaces, respectively, which were fitted using a nonlinear split-peak fitting method. It can be seen from Fig. 10 that both $\mathrm{Ce}^{3+}$ and $\mathrm{Ce}^{4+}$ valences are present in the samples. The spin orbitals 3d ${ }_{3 / 2}$ and $3 \mathrm{~d}{ }_{5 / 2}$ of the sample are labeled with U and $\mathrm{V}_{\mathrm{t}}$ respectively, where $\mathrm{V}_{0}, \mathrm{~V}_{2}, \mathrm{U}_{1}$, and $\mathrm{U}_{2}$ peaks are characteristic peaks of $\mathrm{Ce}^{4+}$ valence, and $\mathrm{V}_{1}$ and $\mathrm{U}_{0}$ are characteristic peaks of $\mathrm{Ce}^{3+}$ [32,33]. The integral areas of the peaks of ceria samples with different Ce valences are given in Table 4. The components of $\mathrm{Ce}^{3+}$ and $\mathrm{Ce}^{4+}$ are calculated by Eq. (4) and Eq. (5), respectively:
$\left[\mathrm{Ce}^{3+}\right]=\frac{V_{1}+U_{0}}{V_{0}+V_{1}+V_{2}+U_{0}+U_{1}+U_{2}}$
![img-8.jpeg](images\img-8.jpeg)

Fig. 9. AFM Images of $\mathrm{SiO}_{2}$ wafer: (a) before polishing; (b) after polishing with acetic acid; (c) after polishing with buffer solution.

![img-9.jpeg](images\img-9.jpeg)

Fig. 10. Full spectrum of XPS of ceria samples: (a) $1.0 \mathrm{wt} \%$ ceria; (b) $1.0 \mathrm{wt} \%$ ceria with acetic acid as dispersant; (c) $1.0 \mathrm{wt} \%$ Ccria with buffer solution as dispersant.
![img-10.jpeg](images\img-10.jpeg)

Fig. 11. Fitted curves of XPS fine spectra of Ce 3d of ceria samples: (a) $1.0 \mathrm{wt} \%$ ceria; (b) $1.0 \mathrm{wt} \%$ ceria with acetic acid as the dispersant; (c) $1.0 \mathrm{wt} \%$ ceria with buffer solution as the dispersant.
$\left[C e^{4+}\right]=\frac{V_{0}+V_{2}+U_{1}+U_{2}}{V_{0}+V_{1}+V_{2}+U_{0}+U_{1}+U_{2}}$
The specific components of $\mathrm{Ce}^{3+}$ and $\mathrm{Ce}^{4+}$ on the ceria surface of the samples are shown in Fig. 12. The components of $\mathrm{Ce}^{3+}$ and $\mathrm{Ce}^{4+}$ on the surface of ceria are $24 \%$ and $76 \%$, respectively, when no dispersant is added to the slurry. The component of $\mathrm{Ce}^{3+}$ is lower. When acetic acid is added, the components of $\mathrm{Ce}^{3+}$ and $\mathrm{Ce}^{4+}$ on the surface of ceria is $26 \%$
and $74 \%$, respectively. And when the buffer solution is added, the components of $\mathrm{Ce}^{3+}$ and $\mathrm{Ce}^{4+}$ on the surface of ceria is $35 \%$ and $65 \%$, respectively. It can be found that acetic acid and buffer solution are beneficial to the increase in the component of $\mathrm{Ce}^{3+}$. The component of $\mathrm{Ce}^{3+}$ is the highest when the buffer solution is added, which confirms the above conjecture that elemental Ce , crucially $\mathrm{Ce}^{3+}$, indeed has a positive effect on the dispersant of ceria slurry and the removal rate of $\mathrm{SiO}_{2}$.

In addition, a large number of studies have shown that the chemical activity of ceria is related to the concentration of $\mathrm{Ce}^{3+}$ and oxygen vacancy, and the higher the concentration of $\mathrm{Ce}^{3+}$, the stronger the chemical activity of ceria [34-38]. As can be seen from the full spectrum diagram in Figs. 9 and 11, after adding buffer solution to the slurry, the component of O 1 s decreases the most, and the component of $\mathrm{Ce}^{3+}$ of Ce 3d increases the most. The chemical activity of ceria is the strongest at this time. Based on Cook's reaction mechanism, Sabia et al. think that during the CMP process, $\mathrm{Ce}^{3+}$ on the surface of ceria generates more active sites on the particles and the workpiece, which is more favorable for the $\mathrm{Ce}-\mathrm{O}-\mathrm{Si}$ softening layer to be generation so that improving the removal rate of $\mathrm{SiO}_{2}$ [39]. The above study in this paper shows that there is indeed a transition of state between $\mathrm{Ce}^{4+}$ to $\mathrm{Ce}^{3+}$. The buffer solution increases the concentration of $\mathrm{Ce}^{3+}$, which favors the chemical activity of the ceria abrasive and thus increases the $\mathrm{SiO}_{2}$ removal rate. This corresponds to the results of experimental results.

### 3.5. Mechanistic analysis through UV-Vis method

In order to further investigate the effect of the buffer solution on the active substances of ceria, the valence information of Ce element in ceria samples was analyzed by UV-visible spectroscopy. The results are shown in Fig. 13. It has been shown that the absorption peak of ceria near 200 nm is the characteristic absorption peak of $\mathrm{Ce}^{3+}$, and the absorption peak near 300 nm is the characteristic absorption peak of $\mathrm{Ce}^{4+}$ [40]. Therefore, it can be found that when no dispersant is added to the slurry, the intensity of the absorption peak of $\mathrm{Ce}^{3+}$ on the surface of ceria is the lowest and the intensity of the absorption peak of $\mathrm{Ce}^{4+}$ is highest. When the dispersant was added to the slurry, the intensity of the absorption peaks of $\mathrm{Ce}^{3+}$ became higher and this is the highest when the buffer solution is added. In contrast, when adding buffer solution, the intensity of the absorption peak of $\mathrm{Ce}^{4+}$ is lowest. It indicates that there is a conversion of $\mathrm{Ce}^{4+}$ to $\mathrm{Ce}^{3+}$. Compared to acetic acid, the buffer solution mostly promotes the increase of $\mathrm{Ce}^{3+}$ content. Dandu et al. [41] found that the intensity of the UV absorption peak can reflect the strength of the interaction between the additive and ceria. After adding buffer solution, the intensity of the $\mathrm{Ce}^{3+}$ absorption peak is obviously strengthened, indicating that the adsorption of buffer solution and ceria is the strongest, which is more conducive to the improvement of the dispersion performance of ceria slurry. They also found that the higher the peak intensity of the UV absorption peak of $\mathrm{Ce}^{3+}$, the higher the removal rate of $\mathrm{SiO}_{2}$ by the slurry. In this paper, the removal rate of $\mathrm{SiO}_{2}$ by the slurry with the addition of buffer solution is higher than that of

Table 4
Distribution of XPS peaks of Ce 3d of ceria samples: (a) $1.0 \mathrm{wt} \%$ ceria; (b) $1.0 \mathrm{wt} \%$ ceria with acetic acid as dispersant; (c) $1.0 \mathrm{wt} \%$ ceria with buffer solution as dispersant.

| Sample | Peak Assign-ent | $\mathrm{V}_{0}$ | $\mathrm{V}_{1}$ | $\mathrm{V}_{2}$ | $\mathrm{U}_{0}$ | $\mathrm{U}_{1}$ | $\mathrm{U}_{2}$ |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| (a) | BE (eV) | 882.30 | 888.30 | 897.97 | 900.72 | 907.22 | 916.40 |
|  | Area (\%) | 40.08 | 9.46 | 15.46 | 14.08 | 7.76 | 13.16 |
| (b) | BE (eV) | 882.85 | 888.78 | 898.51 | 901.26 | 907.75 | 916.96 |
| (c) | Area (\%) | 35.90 | 13.73 | 18.30 | 12.79 | 6.20 | 13.08 |
|  | BE (eV) | 882.17 | 888.70 | 898.10 | 900.87 | 907.14 | 916.52 |
|  | Area (\%) | 32.03 | 12.51 | 17.31 | 22.37 | 8.86 | 11.72 |

![img-11.jpeg](images\img-11.jpeg)

Fig. 12. Components s of $\mathrm{Ce}^{3+}$ and $\mathrm{Ce}^{4+}$ on the surface of ceria samples: (a) $1.0 \mathrm{wt} \%$ ceria; (b) $1.0 \mathrm{wt} \%$ ceria with acetic acid as dispersant; (c) $1.0 \mathrm{wt} \%$ ceria with buffer solution as dispersant.
![img-12.jpeg](images\img-12.jpeg)

Fig. 13. UV-vis spectra of $\mathrm{Ce}^{3+}$ and $\mathrm{Ce}^{4+}$ on the surface of ceria samples: (a) 1.0 wt $\%$ ceria; (b) $1.0 \mathrm{wt} \%$ ceria with acetic acid as dispersant; (c) $1.0 \mathrm{wt} \%$ ceria with buffer solution as dispersant.
acetic acid, and the component of $\mathrm{Ce}^{3+}$ on the surface of the ceria samples is also the highest after the addition of buffer solution. These findings are in line with the research conducted by Dandu et al., as well as the results obtained from XPS analysis.

In summary, the action mechanism of the buffer solution to improve the dispersion stability of ceria and the removal rate of $\mathrm{SiO}_{2}$ compared to acetic acid was investigated by combining XPS and UV-Vis analysis. The adsorption between the buffer solution and ceria particles was stronger. Because the buffer solution increased the concentration of acetate ions in the slurry, more acetate ions were adsorbed on the surface of ceria particles, which led to the enhancement of the inter-particle electrostatic force, thus improving the dispersion of ceria. Furthermore, the increase in component of $\mathrm{Ce}^{3+}$ and oxygen vacancy contributes to the increase in the active sites of ceria particles, accelerates the chemical reaction between the abrasive and $\mathrm{SiO}_{2}$ wafers, and promotes the formation of the $\mathrm{Si}-\mathrm{O}-\mathrm{Ce}$ softening layer so that improving the removal rate of $\mathrm{SiO}_{2}$.

### 3.6. Mechanistic analysis by adsorption and dynamic simulation

Based on the above experiments, when the buffer solution was used as a dispersant, the dispersion stability of the ceria slurry and the polishing effect of $\mathrm{SiO}_{2}$ were effectively improved. The reason is that the prepared buffer solution increased the components of acetate ions in the slurry. And the mechanism was next investigated by adsorption and dynamic simulation using Material Studio software. The adsorption model of acetate ions in different concentrations on ceria was constructed as shown in Fig. 14. The concentration of acetate ion is (a1/a2) $0.5 \%$, (b1/b2) $1.0 \%$, (c1/c2) $2.0 \%$, and (d1/d2) $3.0 \%$, respectively. The adsorption energy $\left(E_{\text {ads }}\right)$ is calculated from Eq. (6) and the results are shown in Table 3.
$E_{\text {ads }}=E_{\text {tot }}-E_{\text {ceria }}-E_{\text {solution }}$
where $E_{\text {tot }}$ represents the total energy, $E_{\text {ceria }}$ represents the energy of ceria (1 1 0), and $E_{\text {solution }}$ represents the energy of the acetate solution.

It is clear from previous studies that when the $E_{\text {ads }}$ is negative, it represents that adsorption is spontaneous. Moreover, the higher absolute value of the $E_{\text {ads }}$ indicates that the adsorption between two substances is stronger [42]. From Table 5, it can be obtained that the relationship between the absolute value of $E_{\text {ads }}$ with the concentration of acetate ions in the slurry increasing is as follows: $0.5 \% \mathrm{CH}_{3} \mathrm{COO}^{-}$ (6653.15 eV) $<1.0 \% \mathrm{CH}_{3} \mathrm{COO}^{-}(6773.53 \mathrm{eV})<2.0 \% \mathrm{CH}_{3} \mathrm{COO}^{-}$ (6814.36 eV ) $<3.0 \% \mathrm{CH}_{3} \mathrm{COO}^{-}(6836.60 \mathrm{eV})$. The greater the concentration of acetate ions, the higher the absolute value of $E_{\text {ads }}$, indicating that the adsorption of acetate ions on ceria is the strongest. The electrostatic force between ceria particles is enhanced, resulting in improving dispersion properties of the slurry. The conclusion is consistent with the previous experimental results. It can be concluded that the buffer solution inhibits the volatilization of acetic acid into the air so that the concentration of acetate ions in the slurry is increased. Moreover, the buffer solution is prepared from acetic acid and ammonium acetate crystals. The addition of ammonium acetate also increases the amount of acetate ions in the slurry. Therefore, combined with the previous XPS and UV-Vis analysis results, it can be concluded that the

![img-13.jpeg](images\img-13.jpeg)

Fig. 14. Molecular dynamics simulations between different concentrations of acetate ions with ceria abrasives ( $\mathrm{a} 1 / \mathrm{b} 1 / \mathrm{c} 1 / \mathrm{d} 1$ : front view; $\mathrm{a} 2 / \mathrm{b} 2 / \mathrm{c} 2 / \mathrm{d} 2$ : top view): (a1/a2) $0.5 \%$; (b1/b2) $1.0 \%$; (c1/c2) $2.0 \%$ and (d1/d2)3.0\%.

Table 5
Energies between acetic acid ions and ceria at different concentrations.

| Ion | $E_{\text {int }}(\mathrm{eV})$ | $E_{\text {ceria }}(\mathrm{eV})$ | $E_{\text {solution }}(\mathrm{eV})$ | $E_{\text {ads }}(\mathrm{eV})$ |
| :-- | :-- | :-- | :-- | :-- |
| $0.5 \% \mathrm{CH}_{3} \mathrm{COO}^{-}$ | $-323103.40$ | $-312208.30$ | $-4241.95$ | -6653.15 |
| $1.0 \% \mathrm{CH}_{3} \mathrm{COO}^{-}$ | $-322164.14$ | $-311284.12$ | $-4106.49$ | -6773.53 |
| $2.0 \% \mathrm{CH}_{3} \mathrm{COO}^{-}$ | $-322718.05$ | $-311918.41$ | $-3985.28$ | -6814.36 |
| $3.0 \% \mathrm{CH}_{3} \mathrm{COO}^{-}$ | $-321582.31$ | $-310687.89$ | $-4057.82$ | -6836.60 |

increase in the concentration of acetate ions not only improves the dispersion of the ceria slurry, but also further promotes the transformation of $\mathrm{Ce}^{4+}$ to $\mathrm{Ce}^{3+}$ on the surface of ceria, increasing the chemical reactivity of the abrasives and active sites between the abrasives with wafer. Ultimately. the removal rate of $\mathrm{SiO}_{2}$ is increased.

### 3.7. Study on the removal mechanism of $\mathrm{SiO}_{2}$ by buffer solution

The removal mechanism of $\mathrm{SiO}_{2}$ by buffer solution is shown in Fig. 15. From the above analysis, it can be obtained that the buffer solution improves the dispersion stability of ceria slurry so that the chemical reaction between the slurry with the $\mathrm{SiO}_{2}$ wafer becomes more adequate, and increasing the removal rate of $\mathrm{SiO}_{2}$. Moreover, the improvement in the concentration of $\mathrm{Ce}^{3+}$ is also conducive to increase the removal rate of $\mathrm{SiO}_{2}$. During the CMP process, when the slurry contacts the wafer surface, $\mathrm{SiO}_{2}$ is hydrolyzed to produce the $\mathrm{Si}(\mathrm{OH})_{4}$ hydration layer. The Point of Zero Charge (PZC) of $\mathrm{SiO}_{2}$ is 2.2 and the PZC of ceria is 7.9 [43,44]. Therefore, under the condition of pH 4.0 , ceria with a positive charge adsorbed on the surface of the $\mathrm{SiO}_{2}$ with a negative charge to form the $\mathrm{Si}-O-\mathrm{Ce}$ bond. When the buffer solution is used as the dispersant, $\mathrm{Ce}^{4+}$ on the surface of ceria is transformed into $\mathrm{Ce}^{3+}$ with higher chemical activity. When the $\mathrm{Si}-O-\mathrm{Ce}$ bond is formed, the free electrons in the $\mathrm{Ce}^{3+}$ destroy the $\mathrm{Si}-O-\mathrm{Si}$ bond through electron

![img-14.jpeg](images\img-14.jpeg)

Fig. 15. Removal mechanism of $\mathrm{SiO}_{2}$ by buffer solution.
transfer. And the $\mathrm{Si}-O-\mathrm{Ce}$ soft layer formed on the wafer surface was removed by chemical interaction. Therefore, the removal rate of $\mathrm{SiO}_{2}$ is increased. In contrast, when acetic acid is used as the dispersant, it only weakens the $\mathrm{Si}-O-\mathrm{Si}$ bond, and then the $\mathrm{Si}-O-\mathrm{Ce}$ soft layer is removed by mechanical grinding.

## 4. Conclusions

On the basis of acetic acid as a dispersant of ceria abrasive, the acetic acid-ammonium acetate buffer solution with better-dispersing performance was formulated. The dispersion mechanism of ceria and the removal mechanism of $\mathrm{SiO}_{2}$ were systematically studied. Firstly, the volatilization of acetic acid and buffer solution at the same time was investigated, and it was confirmed that the buffer solution could inhibit the volatilization of acetic acid, which would increase the concentration of acetate ions in the slurry. Through the detailed study of particle size, zeta potential, and SEM, it was found that the buffer solution had a better dispersion effect (average particle size: 183.1 nm , zeta potential: 51.22 mV ) on ceria slurry. Confocal microscopy and AFM results showed that the addition of buffer solution resulted in the least scratches and residual ceria on the wafer surface and the surface roughness was the lowest $(0.07 \mathrm{~nm})$. And the removal rate of TEOS was increased (from $621.59 \mathrm{~nm} / \mathrm{min}$ to $694.77 \mathrm{~nm} / \mathrm{min}$ ). After that, XPS and UV-Vis results showed that the buffer solution was able to convert $\mathrm{Ce}^{3+}$ to $\mathrm{Ce}^{3+}$ with higher reactivity, improving the dispersion property of ceria particles and increasing the active sites. It was also confirmed by adsorption modeling that the higher the concentration of acetate ions, the higher the adsorption energy between acetate ions and ceria, resulting in better stability of ceria slurry. The final mechanism analysis shows that the free electrons of $\mathrm{Ce}^{3+}$ break the $\mathrm{Si}-O-\mathrm{Si}$ bond by electron transfer, achieving the purpose of removing $\mathrm{SiO}_{2}$. Therefore, the acetic acid-ammonium acetate buffer solution that can effectively improve the dispersion performance of ceria slurry. And this conclusion provides valuable insights to the research of promoting the ceria slurry to remain stable for a long time.

## CRediT authorship contribution statement

Min Liu: Writing - original draft, Methodology, Investigation, Formal analysis. Baoguo Zhang: Writing - review \& editing, Supervision, Project administration, Funding acquisition, Conceptualization. Jihoon Seo: Writing - review \& editing. Wenhao Xian: Investigation, Formal analysis. Dexing Cui: Supervision, Investigation. Shitong Liu: Investigation, Data curation. Yijun Wang: Supervision, Methodology. Sihui Qin: Writing - review \& editing, Supervision. Yang Liu: Investigation.

## Declaration of competing interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

## Data availability

No data was used for the research described in the article.

## Acknowledgments

This work was supported by Major National Science and Technology Special Projects (No.2016ZX02301003-004-007), One Hundred Talent Project of Hebei Province of China (E2013100006).

## References

[1] H. Li, C. Zhang, J. Liu, Z. Liu, K. Chen, T. Tughawa, H. Ding, F. Li, B. Lee, A. GowerHall, Y.-C. Chiu, Characterization of shallow trench isolation CMP process and its application. https://doi.org/10.1117/12.2219912, 2016.
[2] P.B. Zantye, A. Kumar, A.K. Sikder, Chemical mechanical planarization for microelectronics applications, Mater. Sci. Eng. R Rep. 45 (2004) 89-220, https:// doi.org/10.1016/j.marr.2004.06.002.
[3] A. Gowda, J. Seo, C.K. Ranaweera, S.V. Babu, Cleaning solutions for removal of $\sim 30 \mathrm{~nm}$ ceria particles from proline and citric acid containing slurries deposited on silicon dioxide and silicon nitride surfaces, ECS J. Solid State Sci. Technol. 9 (2020) 044013, https://doi.org/10.1149/2162-8777/sb8ffe.
[4] Y. Li, C. Wang, J. Zhou, C. Xu, Y. Cheng, Y. Tian, Z. Cui, H. Li, Q. Liu, Role of slurry additives on chemical mechanical planarization of silicon dioxide film in colloidal silica based slurry, ECS J. Solid State Sci. Technol. 10 (2021) 123008, https://doi. org/10.1149/2162-8777/sc3e44.
[5] M. He, X. Zhang, T. Nogami, X. Lin, J. Kelly, H. Kim, T. Spooner, D. Edelstein, L. Zhao, Mechanism of Ce liner as enhancement layer for Cu interconnect gap-fill, J. Electrochem. Soc. 160 (2013) D3040, https://doi.org/10.1149/2.009312jbn.
[6] D.S. Lim, J.W. Ahn, H.S. Park, J.H. Shin, The effect of Ceria abrasive size on dishing and step height reduction of silicon oxide film in STI-CMP, Surf. Coat. Technol. 200 (2005) 1751-1754, https://doi.org/10.1016/j.surfcoat.2005.08.047.
[7] X. Cui, Z. Zhang, C. Shi, F. Meng, G. Xu, W. Xie, Z. Liu, J. Wang, W. Wen, A novel green chemical mechanical polishing for potassium dihydrogen phosphate using corn oil slurry, Mater. Today Sustain. 20 (2022) 100257, https://doi.org/10.1016/1.ntnot.2022.100257.
[8] W. Xie, Z. Zhang, L. Liao, J. Liu, H. Su, S. Wang, D. Guo, Green chemical mechanical polishing of sapphire wafers using a novel slurry, Nanoscale 12 (2020) 22518-22526, https://doi.org/10.1039/18093047034.
[9] Z. Zhang, J. Cai, J. Zhang, D. Liu, Z. Yu, D. Guo, Environment friendly chemical mechanical polishing of copper, Appl. Surf. Sci. 467-468 (2019) 5-11, https://doi. org/10.1016/j.apssoc.2018.10.133.
[10] L. Liao, Z. Zhang, F. Meng, D. Liu, B. Wu, Y. Li, W. Xie, A novel slurry for chemical mechanical polishing of single crystal diamond, Appl. Surf. Sci. 564 (2021) 150431, https://doi.org/10.1016/j.apssoc. 2021.150431.
[11] L. Liao, Z. Zhang, F. Meng, D. Liu, J. Liu, Y. Li, X. Cui, Novel rotary chemical mechanical polishing on an integral impeller, J. Manuf. Process. 66 (2021) 198-210, https://doi.org/10.1016/j.imoprc.2021.04.010.
[12] Z. Zhang, L. Liao, X. Wang, W. Xie, D. Guo, Development of a novel chemical mechanical polishing slurry and its polishing mechanisms on a nickel alloy, Appl. Surf. Sci. 506 (2020) 144670, https://doi.org/10.1016/j.apssoc.2019.144670.

[13] T. Hoshino, Y. Kurata, Y. Terasaki, K. Susa, Mechanism of polishing of SiO2 films by Ceria particles, J. Non-Cryst. Solids 283 (2001) 129-136, https://doi.org/ 10.1016/S0022-3093(01)00364-7
[14] L. Cook M, Chemical processes in glass polishing, J. Non-Cryst. Solids 120 (1990) 152-171, https://doi.org/10.1016/S022-3093(90)90200-6.
[15] S. Sahir, H.-W. Cho, P. Jalalzai, S. Samanta, S. Hamada, T.-G. Kim, J.-G. Park, Effect of slurry particles on PVA brush contamination during post-CMP cleaning, Mater. Sci. Semicond. Process. 151 (2022) 107043, https://doi.org/10.1016/j. mesp.2022.107043.
[16] S. Samanta, S. Jin, C.-H. Lee, S.-S. Lee, H. Struyf, T.-G. Kim, J.-G. Park, Effect of ammonium halide salts on wet chemical nanoscale etching and polishing of InGaAs surfaces for advanced CMOS devices, Mater. Sci. Semicond. Process. 161 (2023) 107469, https://doi.org/10.1016/j.mssp.2023.107469.
[17] M. Jiang, N.O. Wood, R. Komanduri, On chemo-mechanical polishing (CMP) of silicon nitride (Si3N4) workmaterial with various abrasives, Wear 220 (1998) 59-71, https://doi.org/10.1016/S0043-1648(98)00245-2.
[18] N.K. Penta, H.P. Amanapu, B.C. Peethala, S.V. Babu, Use of anionic surfactants for selective polishing of silicon dioxide over silicon nitride films using colloidal silicabased slurries, Appl. Surf. Sci. 283 (2013) 986-992, https://doi.org/10.1016/j. apsusc.2013.07.057.
[19] M.-H. Oh, J.-S. Nho, S.-B. Cho, J.-S. Lee, R.K. Singh, Polishing behaviors of ceria abrasives on silicon dioxide and silicon nitride CMP, Powder Technol. 206 (2011) 239-245, https://doi.org/10.1016/j.powter.2010.09.025.
[20] Y.-H. Kim, S.-K. Kim, J.-G. Park, U. Paik, Increase in the adsorption density of anionic molecules on ceria for defect-free STI CMP, J. Electrochem. Soc. 157 (2009) H72, https://doi.org/10.1149/1.3251009.
[21] J.-G. Park, T. Katoh, W.-M. Lee, H. Jeon, U. Paik, Surfactant effect on oxide-tonitride removal selectivity of nano-abrasive ceria slurry for chemical mechanical polishing, Jpn. J. Appl. Phys. 42 (2003) 5420, https://doi.org/10.1143/ JJAP 42.5420.
[22] J.-H. Park, H. Cui, J.-Y. Cho, H.-S. Hwang, W.-J. Hwang, U. Paik, H.-G. Kang, N.J. Kwak, J.-G. Park, Multiselectivity chemical mechanical polishing for NAND flash memories beyond 32 nm , J. Electrochem. Soc. 157 (2010) H607, https://doi.org/ $10.1149 / 1.3368675$.
[23] Q. Wei, Y. Meng, J. He, G. Tang, Chemical-mechanical dispersing behavior of a nanoceria abrasive, J. Rare Earths 28 (2010) 478-481, https://doi.org/10.1016/ S1002-0721(10)60310-9.
[24] S. Kim, J.-H. So, D.-J. Lee, S.-M. Yang, Adsorption behavior of anionic polyelectrolyte for chemical mechanical polishing (CMP), J. Colloid Interface Sci. 319 (2008) 48-52, https://doi.org/10.1016/j.jcis.2007.11.004.
[25] H.-M. Kim, R. Prasanna Venkatesh, T.-Y. Kwon, J.-G. Park, Influence of anionic polyelectrolyte addition on ceria dispersion behavior for quartz chemical mechanical polishing, Colloids Surf. A Physicochem. Eng. Asp. 411 (2012) 122-128, https://doi.org/10.1016/j.caburfa.2012.07.009.
[26] J. Cheng, S. Huang, X. Lu, Preparation of surface modified ceria nanoparticles as abrasives for the application of chemical mechanical polishing (CMP), ECS J. Solid State Sci. Technol. 9 (2020) 024015, https://doi.org/10.1149/2162-8777/s07098.
[27] Z.X. Yang, B.G. Zhang, X.F. Yang, Y. Li, H.R. Li, Research on preparation of ceria polishing slurry with high dispersion stability and its polishing performance, Chinese Rare Earths 43 (2022) 128-136, https://doi.org/10.16533/J.CNKI.15-1099/TF.202202015.
[28] C. Xu, J.W. Zhou, C.W. Wang, Y. Tian, Y. Li, Z.H. Cui, S. Li, Effect of citric acid on the dispersion stability and polishing performance of ceria abrasive, Semiconductor Technology 47 (2022) 111-116, https://doi.org/10.13290/j.cnki. bshjs.2022.02.006.
[29] M. Wang, F.-L. Duan, Atomic-level wear behavior of sliding between silica (010) surfaces, Appl. Surf. Sci. 425 (2017) 1168-1175, https://doi.org/10.1016/j. apsusc. 2017.07.055.
[30] W. Ye, Z. Baoguo, W. Pengfei, L. Min, C. Dexing, X. Wenhao, Improving the dispersion stability and chemical mechanical polishing performance of ceria slurries, ECS J. Solid State Sci. Technol. 12 (2023) 044004, https://doi.org/ 10.1149/2162-8777/accxa5.
[31] Y. Wei, Y. Liu, Study of dispersion mechanisms of modified SiC powder: electrostatic repulsion and steric hindrance mechanism, New J. Chem. 43 (2019) 14036-14044, https://doi.org/10.1039/C9NJ02131K.
[32] S. Sooi, V.S. Vats, S. Kumar, B. Dalela, M. Mishra, R.S. Meena, G. Gupta, P.A. Alvi, S. Dalela, Structural, optical and magnetic properties of Fe-doped Ceria samples probed using X-ray photoelectron spectroscopy, J. Mater. Sci. Mater. Electron. 29 (2018) 10141-10153, https://doi.org/10.1007/s10854-018-9060-x.
[33] A. Chen, Y. Duan, Z. Mu, W. Cai, Y. Chen, Meso-silica/Erbium-doped ceria binary particles as functionalized abrasives for photochemical mechanical polishing (PCMP), Appl. Surf. Sci. 550 (2021) 149353, https://doi.org/10.1016/j. apsusc.2021.149353.
[34] S.N. Matusim, M.H. Harumani, M.M. Khan, Ceria and Ceria-based nanomaterials for photocatalytic, antioxidant and antimicrobial activities, J. Rare Earths 41 (2023) 167-181, https://doi.org/10.1016/j.jre.2022.09.003.
[35] J. Seo, J. Moon, J.H. Kim, K. Lee, J. Hwang, H. Yoon, D.K. Yi, U. Paik, Role of the oxidation state of cerium on the ceria surfaces for silicate adsorption, Appl. Surf. Sci. 389 (2016) 311-315, https://doi.org/10.1016/j.apnusc.2016.06.193.
[36] X. Xia, Y. Lan, J. Li, C. Chen, B. Xu, X. Lao, X. Mao, Facile synthesis of nanoceria by a molten hydroxide method and its photocatalytic properties, J. Rare Earths 38 (2020) 951-960, https://doi.org/10.1016/j.jre.2019.11.007.
[37] Y.-C. Zhang, Z. Li, L. Zhang, L. Pan, X. Zhang, L. Wang, Fazal-e-Aleem, J.-J. Zou, Role of oxygen vacancies in photocatalytic water oxidation on ceria oxide: experiment and DFT studies, Appl. Catal. B Environ. 224 (2018) 101-108, https:// doi.org/10.1016/j.apcadr.2017.10.049.
[38] T. Bao, H. Zhou, Y. Zhang, C. Guo, W. Guo, H. Qin, P. Gao, H. Xiao, W. Liu, Effect of Ceria on carbon deposition resistance of Ni/Ceria catalyst supported on SiC porous ceramic for ethanol steam reforming, J. Rare Earths 41 (2023) 1703-1713, https:// doi.org/10.1016/j.jre.2022.09.006.
[39] R. Sabia, H.J. Stevens, Performance characterization of cerium oxide abrasives for chemical-mechanical polishing of glass, mach, Sci. Technol. 4 (2000) 235-251, https://doi.org/10.1080/1094034000945708.
[40] R.V.S. Praveen, R. Manivannan, T.D. Umashankar, B.-J. Cho, J.-G. Park, S. Ramanathan, Abrasive and additive interactions in high selectivity STI CMP slurries, Microelectron. Eng. 114 (2014) 98-104, https://doi.org/10.1016/j. mse.2013.10.004.
[41] P.R.V. Dandu, B.C. Peethala, S.V. Babu, Role of different additives on silicon dioxide film removal rate during chemical mechanical polishing using ceria-based dispersions, J. Electrochem. Soc. 157 (2010) H869, https://doi.org/10.1149/ 1.3457387.
[42] Y. Wang, S. Zhang, R. Tan, W. Li, J. Ji, M. Yan, Z. Cui, Effect of corrosion inhibitor BTA on silica particles and their adsorption on copper surface in copper interconnection CMP, ECS J. Solid State Sci. Technol. 11 (2022) 044002, https:// doi.org/10.1149/2162-8777/ac627c.
[43] M. Nabavi, O. Spalla, B. Cabane, Surface chemistry of nanometric ceria particles in aqueous dispersions, J. Colloid Interface Sci. 160 (1993) 459-471, https://doi.org/ 10.1006/jco.1993.1417.
[44] S. Ramarajan, Y. Li, M. Hariharaputhiran, Y.-S. Her, S.V. Babu, Effect of pH and ionic strength on chemical mechanical polishing of tantalum, Electrochem. Solid State Lett. 3 (2000) 232, https://doi.org/10.1149/1.1391010.

