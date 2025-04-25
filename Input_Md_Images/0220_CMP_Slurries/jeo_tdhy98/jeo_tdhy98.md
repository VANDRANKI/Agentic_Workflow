# Investigation of abrasive behavior between pad asperity and oxide thin film in chemical mechanical planarization 

Sanghuck Jeon ${ }^{\mathrm{a}, 1}$, Jungryul Lee ${ }^{\mathrm{a}, 1}$, Seokjun Hong ${ }^{2}$, Hyeonmin Seo ${ }^{2}$, Yeongkwang Cho ${ }^{2}$, Pengzhan Liu ${ }^{3}$, Kihong Park ${ }^{3}$, Taesung Kim ${ }^{\mathrm{a}, \mathrm{b}, *}$<br>${ }^{a}$ School of Mechanical Engineering, Sungkyunkwan University (SKKU), Suwon-si, Gyeonggi-do, 16419, South Korea<br>${ }^{b}$ SKKU Advanced Institute of Nano Technology (SAINT), Sungkyunkwan University (SKKU), Suwon-si, Gyeonggi-do, 16419, South Korea<br>${ }^{2}$ Semiconductor R\&D Center, Samsung Electronics, Hwaseong-si, Gyeonggi-do, 445-701, South Korea

## A R T I C L E I N F O

Keywords:
Chemical mechanical planarization (CMP)
Oxide CMP
Pad asperity

A B S T R A C T

In this paper, tribological effects on the material removal rate (MRR) are investigated using two types of slurry abrasives (i.e., ceria and silica) and three types of pads. From a micro to macro viewpoint, the physico-chemical interaction between the pad-wafer interface and abrasive was studied based on multi-asperity contact. First, the relative contact pressure in high or low proportions among all asperities was calculated using a contact mechanics model. The results indicate that for the commercial slurry used in the semiconductor industry, relatively high contact pressure due to the asperities can be transferred to the ceria abrasives, and only a low contact pressure can be supported by these silica abrasives. Furthermore, it was confirmed that the two different slurry abrasives showed opposite behaviors according to the real contact area of the pad asperities. That is, as the pad texture changed from 'Desired pad' to 'Smoothed pad', the MRR of the ceria increased by $47 \%$, while the MRR of the silica decreased $59 \%$. Lastly, the Stribeck curve, which is suitable for the CMP process, was re-analyzed to clarify the abrasion mechanism under the pad asperity scale. The results showed that two-body abrasion may be maintained for the ceria CMP, and transition is possible from two-body to three-body abrasion at the silica CMP as the contact area increases. The present paper is expected to clarify the tribological mechanism of the oxide CMP and can provide further insight into optimizing and selecting consumables such as conditioner, pad, and slurry.

## 1. Introduction

Chemical mechanical planarization/polishing (CMP) is a state-of-the-art technique for creating the multi-layered structure found in integrated circuits (IC) in the semiconductor industry. As the name indicates, the CMP process is also capable of ultra-precision surface finishing using slurry abrasives, which affects the quality of the final device. Recently, an ultraprecision polishing method using nano-sized abrasive was developed [1-3]. This approach opens new avenues for investigating basic abrasion mechanisms [4]. In addition, a new concept of eco-friendly slurry for polishing various surfaces was developed [5-8]. These works have contributed significantly to CMP process development $[9,10]$.

In general, various types of pad groove patterns have been utilized, such as radial, circular, offset, and combined patterns, and the circular
groove among them is widely used in the CMP process [11]. The polishing pad, typically made of polyurethane, is much rougher than the thin film on the wafer surface. Thus, optimizing the pad surface texture defined by "asperities" can enhance CMP performance [12].

To polish the thin film deposited on the wafer, the film reacts with the slurry chemical, and the abrasives located on the pad asperities remove the step height of the film through mechanical abrasion [13,14]. The real contact area between the thin film and pad asperity is less than $1 \%$ under various static pressures [15,16]. It is known that the hydrodynamic pressure from the slurry layer is negligible [17,18]. Thus, the pressure applied to the wafer surface is completely supported by the pad asperities, and the asperities have an effect on the CMP performance. The first mathematical removal model, proposed by Preston, is widely accepted and is given by [19].

[^0]
[^0]:    ${ }^{a}$ Corresponding author. School of Mechanical Engineering, Sungkyunkwan University (SKKU), Suwon-si, Gyeonggi-do, 16419, South Korea
    E-mail address: tkim@skku.edu (T. Kim).
    ${ }^{1}$ Sanghuck Jeon and Jungryul Lee contributed equally to this work.

$\frac{d b}{d t}=k \cdot p \cdot v$
where k is the Preston constant, p is the applied pressure, and v is the relative velocity between the pad and the wafer. The above expression represents only the pressure and velocity, and the other parameters are encompassed by the constant k . To clarify the variables for the pad texture, the improved MRR model is expressed as [20-23].
$\frac{d b}{d t}=n_{p} \cdot A_{\text {real }} \cdot\left(\frac{d V}{d t}\right)_{\text {abrasive }}$
Here, $n_{p}$ is the number of abrasives per unit area that can be trapped on the asperities, $A_{\text {real }}$ is the real contact area between the pad asperity and the wafer, and $\left(\frac{d p}{d t}\right)_{\text {abrasive }}$ is the average volumetric MRR for a single abrasive. This model predicts that the MRR is proportional to the real contact area, $A_{\text {real }}$ or the average MRR of a single abrasive.

The interlayer dielectric (ILD) and shallow trench isolation (STI) process is conducted by an oxide CMP. The basic slurry utilized in the oxide CMP process consists of abrasives such as silica and ceria. The prevailing mechanism for the silica slurry in oxide film is mechanical abrasion through surface hydration in an alkaline environment [24,25]. The softened film followed by the hydration is influenced by the concentration of $\mathrm{OH}^{-}$ions [26]. In terms of the interaction between the ceria and oxide, it is known that a higher ratio of $\mathrm{Ce}^{3+}$ ions is considered to be highly reactive [27-31]. On the other hand, $\mathrm{Ce}^{4+}$ at the ceria surface can reduce chemical reactivity [32]. As a result, the $\mathrm{Ce}^{3+}$ species can play a critical role in determining the MRR. The most important challenge in the CMP is consistent process performance. However, difficulty in understanding the abrasion mechanism of ceria and silica slurry in terms of the polishing pad may result in performance degradation. The MRR variation across different polishing pads has been studied extensively. Liao et al. pointed out that higher contact pressure caused by a higher conditioner force produces a high MRR for the silica slurry [33]. Jeong et al. also indicated that the contact pressure decreased as the contact area between the pad and wafer goes up because of the pad wear, resulting in a lower MRR [34]. Recently, many researchers stated that an increased contact area leads to higher MRR for ceria slurry, contrary to the fact that the contact pressure is inversely proportional to the contact area [35-37]. Their experimental results require additional theoretical studies for understanding the abrasion mechanism of ceria and silica slurry in terms of the pad.

In addition, pad texture and the real contact area between the pad and the wafer can be affected by the pad wear rate (PWR) of the conditioner, which can lead to a change of CMP performance depending on the slurry abrasive types. Therefore, it is very important to understand the abrasion mechanism based on the pad asperities while considering each slurry type and the real contact area between the two interfaces.

Accordingly, our research focused on the contact area caused by pad asperities considering slurry abrasive type. First, the pad surface texture was analyzed via various parameters by significantly changing the real contact area. Second, asperity contact pressure, real contact area, and the number of active abrasives were considered to study the MRR variations in detail. Finally, the pads with different groove up-features were introduced to validate the behavior of the mechanical abrasion for each abrasive type, and we analyzed the tribological contact mode using the Stribeck curve.

## 2. Theoretical background

### 2.1. Relative contact pressure among all asperities

CMP pad provides a channel to transport the slurry abrasives to the wafer surface and transfers mechanical force to enable the tribological
wear required for a high MRR. Pad surface roughness plays a very important role in transporting the abrasives to the contact spot. It is also composed of numerous asperities and is in direct contact with the wafer. To combine the topographic properties of the rough polishing pad, the plasticity index, which determines a relative proportion of plastically deformed asperities, is defined as [21,38,39].
$\psi=\frac{4}{\pi}\left(\frac{\sigma}{R_{a}}\right)^{\frac{1}{2}} \frac{E_{a}}{H_{a}}$
Here, $\psi$ is a function of the ratio of asperity modulus to asperity hardness, $E_{a} / H_{a}$, and the ratio of the standard deviation of the asperity height to the radius of asperity curvature, $\sigma / R_{a}$. For a polyurethane pad, $E_{a}$ and $H_{a}$ do not usually change independently and so cannot be varied much. Thus, $\sigma$ and $R_{a}$ can determine the extent of the plasticity. For high $\psi$, the high contact pressure can be transmitted to the surface. In the CMP process where slurry abrasives are present at the interface, the MRR can be enhanced by controlling the contact pressure through $\psi$.

Since the hardness of the thin films on the wafer is much larger than that of the pad, the asperities in contact are compressed and deformed. However, the asperities of each pad are randomly distributed, and the asperities deform in different modes at a certain load [40]. Each of the deformed asperities may transmit high or low contact pressure to the thin film and abrasives. Furthermore, depending on the property of the slurry abrasives, the contact pressure caused by the pad asperity may be delivered differently even under the same pad texture. Thus, it is essential to define the relative pressure of asperities according to the slurry abrasives. To establish a criterion for the threshold, a critical asperity contact pressure, $p_{c}$, can be estimated as [21,39]:
$p_{c}=\frac{3}{2} H_{a} \cdot C_{v a l}$
Thus, $p_{c}$ is determined by the hardness of the asperity, $H_{a}$, and slurry concentration, $C_{\text {val }}$.

Assuming that the height distribution of the pad asperities is exponentially distributed [41,42], the probability density function of the asperity height is as follows
$\mathfrak{D}(z)=\frac{1}{\sigma} \cdot \exp \left(-\frac{z}{\sigma}\right)$
If N asperities per unit area, which has only the asperities of heights, z , taller than the separation distance, d , are in contact with a flat thin film, the number of asperities in contact per unit area, n , can be written as
$n=N \int_{d}^{\infty} \mathfrak{D}(z) d z=N \cdot \exp \left(-\frac{z}{\sigma}\right)$
When the asperities are pressed by the thin film to be polished, the relatively tall asperities may have a high pressure $\left(p_{a} \geq p_{c}\right)$ above the critical pressure, $p_{c}$, and the relatively short asperities may have a low pressure $\left(p_{a}<p_{c}\right)$ below the critical pressure, $p_{c}$. Thus, the relative pressure based on the asperity height is expressed as [21,39].
$\frac{n_{\text {high,p }}}{n}=\exp \left(-\frac{C_{c}}{\psi^{2}}\right)$
$\frac{n_{\text {low, }}}{n}=1-\exp \left(-\frac{C_{c}}{\psi^{2}}\right)$
Here, $C_{c}$ is a coefficient of the slurry abrasive concentration, $C_{\text {val }}$, from $[21,39]$.

$$
C_{c}= \begin{cases}\left(\frac{9}{2} C_{v a l}\right)^{2} \cdot\left(C_{v a l}<\frac{2}{9}\right) & \\ \exp \left[2 \cdot\left(\frac{9}{2} C_{v a l}-1\right)\right] \cdot\left(C_{v a l} \geq \frac{9}{2}\right) & \end{cases}
$$

![img-0.jpeg](images\img-0.jpeg)
(b)

Pad 1
Pad 2
Pad 3
![img-1.jpeg](images\img-1.jpeg)

Fig. 1. (a) Schematic of the CMP pad geometry. (b) Cross-sectional optical microscope images of the CMP pad geometry.
Therefore, the relative pressure of the asperities depends on $C_{\text {ref }}$ and $\psi$. As $C_{\text {ref }}$ increases, the critical pressure increases according to Equation (4). For the increased $\psi$, there may be more asperities that transmit high contact pressure to the thin film and abrasives.

The material removal is caused by the abrasives located in the real contact area between the thin film to be polished and the fine asperities of the pad. The real contact area with the asperities that undergo elastic/ plastic deformation is related by the plasticity index [21,38,39]. In the case of a typical CMP process, a pad break-in is performed to stabilize the micro-texture of a brand-new pad [43]. Accordingly, the plasticity index of the pad can converge close to 1 [44], and the portion of asperities that elastically deform increases. Thus, assuming the asperity is in elastic deformation, the real contact area, $A_{\text {real }}$, can be estimated based on a Hertzian model from [41].
$A_{\text {real }}=\chi^{\frac{1}{2}} \frac{P \cdot A}{E_{a}}\left(\frac{R_{a}}{\sigma}\right)^{\frac{1}{2}}$
For the polyurethane pad, the radius of the asperity curvature $\left(R_{a}\right)$ and the standard deviation of asperity height $(\sigma)$ can be key parameters that determines the real contact area between the thin film and asperities.

## 3. Experimental method

### 3.1. Consumable preparation

The main CMP process was conducted on 300 mm tetraethyl orthosilicate (TEOS) oxide wafers using commercial ceria and silica slurries that are widely used in industry. Normally, it is known that the ceria slurry abrasive concentration is much lower than that of silica. The diameters of the two slurry abrasives were both about 130 nm , and the

Table 1
Pad texture parameters of the desired and smoothed pad based on Pad 2.

| Variables | Desired | Smoothed |
| :-- | :-- | :-- |
| $R_{a}(\mu \mathrm{~m})$ | 50.2 | 122.6 |
| $\sigma(\mu \mathrm{~m})$ | 3.4 | 2.9 |
| $\psi$ | 2.5 | 1.5 |

dilution ratio of each slurry was recommended by the slurry supplier. The polishing process was carried out on three types of CMP pads (DuPont Chemical, USA), which are based on IC1000 pad: Pad 1, Pad 2, and Pad 3. The pads have the same depth and width, but the up-features of each pad are different, Fig. 1. The ratio of the up-feature area of the flat pad area can be expressed as dimensionless parameter, $\chi$ [45]. $\chi$ for Pad 1, Pad 2, and Pad 3 is $0.73,0.83,0.92$, respectively.

### 3.2. Experimental procedure

In this experiment, the process was performed using a 300 mm polisher (Poli-762; GnP Technology, Korea). The polisher is a rotary type with a single platen and can measure the in-situ friction force between the pad asperities and the wafer surface. The MRR calculation was carried out by measuring film thickness via a reflectometer (ST5030-SL; K-MAC, Korea). The average MRR was calculated for three wafers. The polishing test was conducted for 1 min at a carrier/platen speed of $87 /$ 93 rpm , a carrier down pressure of 3 psi , and a slurry flow rate of 160 $\mathrm{ml} / \mathrm{min}$.

Before the CMP experiment, pad break-in was conducted using a commercial standard conditioner (Seasol Diamond, Korea) to obtain an optimal pad surface, and the pad was referred to as the 'Desired pad'. Before every experiment, dummy wafers were polished for stable performance.

### 3.3. Smoothed pad procedure

To evaluate the increase of the contact area based on the asperity, the pad texture was smoothed. To make the pad asperities flatter, dummy wafers were polished for 30 min each without a conditioning process, and pad cleaning was performed in between. This pad was referred to as 'Smoothed pad'.

### 3.4. Pad texture analysis

In the experiment, Pad 2 was used as a reference pad, and an asperity-flattened experiment also was performed using Pad 2. After making the pad smooth, the uncompressed surface texture of the polishing pad was measured using the Nano-focus tool (usprint, Nanofocus,

![img-2.jpeg](images\img-2.jpeg)

Fig. 2. (a) Schematic representation of measurement points. Confocal microscopic images of the (b) Desired pad texture and (c) Smoothed pad texture.

GERMANY). Pad surface roughness and asperity properties were extracted from the measurement tool. A 3D confocal microscope (OLS5100; OLYMPUS, JAPAN) was used to measure the average radius of the asperity curvature $\left(R_{a}\right)$ and standard deviation of asperity heights $\langle\sigma\rangle$. To calculate the plasticity indexes, we used the properties of the IC $1000 \mathrm{pad}\left(E_{a} / H_{a}\right)$ [46]. The variables of the pad asperities are summarized in Table 1. The optical microscope images of three types of pads were analyzed using a digital microscope (Dino lite Edge, AnMo Electronics Corporation, Taiwan)

## 4. Results and discussion

First, the surface roughness analysis was performed to check whether the pad asperities were flattened or not. We studied the pad surface state based on reference Pad 2. Second, we considered the relative contact pressure of asperities based on the contact mechanics. Furthermore, we investigated the removal characteristic based on slurry abrasive type, changing the pad asperity state. Lastly, a tribological approach was performed using the Stribeck curve to determine the abrasion behavior between the pad and the wafer based on the slurry abrasives.
(a)
![img-3.jpeg](images\img-3.jpeg)
(b)
![img-4.jpeg](images\img-4.jpeg)

Fig. 3. Roughness profile of wafer/pad contact spots. (a) The reduced peak region (Rpk) and (b) the root mean square roughness (Rms) according to the pad texture state.

![img-5.jpeg](images\img-5.jpeg)

Fig. 4. Schematic of the asperity contact area between two interfaces according to the pad texture. (a) The 'Desired pad' with high $\sigma$ and low $\boldsymbol{R}_{\boldsymbol{e}}$ and (b) 'Smoothed pad' with low $\sigma$ and high $\boldsymbol{R}_{\boldsymbol{e}}$.
shallow parts. Based on these topographic images of the pad, it is apparent that most of the asperities of the 'Smoothed pad' were flattened compared to the 'Desired pad'. Thus, it is expected that the actual contact area between the asperities and the wafer surface can be increased on the 'Smoothed pad'.

The surface roughness of the polishing pad is known to be the critical factor affecting the MRR [47]. Generally, the roughness parameters can be categorized into three types: amplitude parameters, spacing parameters, and hybrid parameters. Among them, the hybrid parameter has been chosen by many researchers for investigating the effect on the contact area, because hybrid parameters such as Reduced peak region $\left(R_{p k}\right)$, Core region $\left(R_{k}\right)$, and Valley region $\left(R_{v k}\right)$ can best represent the roughness changes during the CMP process [34,47-49].
$R_{p k}, R_{k}$, and $R_{v k}$ can be considered to be part of the pad asperities, supports for the applied pressure, and the parts that carry the slurry into the interface, respectively. $\mathrm{R}_{\mathrm{pk}}$ is the main variable related to the MRR and best represents the asperity behavior caused by the conditioning process [34]. Thus, $\mathrm{R}_{\mathrm{pk}}$ is one of the major elements needed to estimate the pad texture state. Fig. 3(a) shows the $\mathrm{R}_{\mathrm{pk}}$ of the 'Desired pad' and 'Smoothed pad' corresponding to each measurement point. The $\mathrm{R}_{\mathrm{pk}}$ value of the polishing pad decreased significantly for the 'Smoothed pad'. This means that both pad asperities were flattened and were much smoother. This may be because of plastic shearing caused by the wafer without the pad conditioning process, resulting in a wider contact area [50].

To analyze the pad surface more accurately, the root mean square roughness (Rms) was considered, as shown in Fig. 3(b). Rms also decreased as the maximum peak height decreased. This may also be because the tall asperities became flat. Therefore, the total contact area between the pad and the wafer may increase.

### 4.2. Material removal rate based on asperity contact in desired pad and smoothed pad

We investigated the removal behavior based on physico-chemical interaction with respect to the contact area between the two interfaces. The planarization process was conducted using the 'Desired pad' and 'Smoothed pad', as shown in Fig. 4. With the two types of pads, Fig. 5 shows the MRR results using ceria/silica abrasives on the oxide film. As the 'Desired pad' changes to a 'Smoothed pad', the surface
roughness of the pad decreases, and the real contact area between the pad asperity and the wafer surface increases. Then, the MRR of ceria slurry increased, and the MRR of silica slurry decreased with the friction force. The reason for this can be explained in terms of both chemical and mechanical aspects.

As shown in Fig. 5(a), the MRR of the oxide film using ceria abrasives increased dramatically from $2990 \AA / \mathrm{min}$ to $4404 \AA / \mathrm{min}$ along with increases in the friction force. As the pad texture defined by the asperity changed from the 'Desired pad' to 'Smoothed pad', the real contact area between the two interfaces can be increased because of the variation of $R_{e} / \sigma$. That is, as $R_{e} / \sigma$ increases, $A_{\text {real }}$ of the smoothed pad increased to $69.8 \%$ from the 'Desired pad' based on Equation (9).

The wider contact area (i.e., smoother surface) between the oxide wafer surface and pad asperities can accelerate chemical reactions [51-53]. It is known that the $\mathrm{Ce}^{3+}$ species on the surface of ceria abrasive interact with hydrated silicate species formed on the oxide film, resulting in the strong chemical bonding of $\mathrm{Ce}-\mathrm{O}-\mathrm{Si}$, which can improve the MRR of the oxide film [27-29]. That is, $\mathrm{Ce}^{3+}$ species on the ceria surface can play a critical role in determining the high MRR, and conversely, $\mathrm{Ce}^{4+}$ can reduce chemical reactivity [27,30,32]. Thus, the ratio of $\mathrm{Ce}^{3+} / \mathrm{Ce}^{4+}$ has to be increased to achieve high MRR. If the contact area is increased, the MRR can be increased by increasing the number of active ceria abrasives while maintaining the ratio of $\mathrm{Ce}^{3+} / \mathrm{Ce}^{4+}$. On the other hand, if the concentration of ceria (wt\%) is increased, although the number of abrasives increases, $\mathrm{Ce}^{4+}$ increases and the MRR decreases [54,55].

It is known that as the $A_{\text {real }}$ increases, the number of active abrasives anchored on the asperities also can be increased [20,51]. Therefore, if the real contact area between the pad asperities and the thin film is increased, the number of abrasives maintaining the ratio of $\mathrm{Ce}^{3+} / \mathrm{Ce}^{4+}$ can also increase. That is, just making the pad texture smooth can be the most efficient technique while maintaining the chemical reactions. As a result, $\mathrm{Ce}-\mathrm{O}-\mathrm{Si}$ bonding due to the abundance of $\mathrm{Ce}^{3+}$ is formed between the film and ceria abrasives, and the abrasives adhered to the oxide film can generate mechanical abrasion by a higher friction force of the pad asperities. Then, ceria abrasives can be removed as a lump, which is cleaved from the film [56].

However, both mechanical interactions and chemical interactions between the film and ceria abrasives are very important. For the high

![img-6.jpeg](images\img-6.jpeg)

Fig. 5. Removal rate, friction force, and calculated contact ratio of (a) ceria slurry and (b) silica slurry according to the pad texture.
![img-7.jpeg](images\img-7.jpeg)

Fig. 6. Relative contact pressure ratio among all the asperities of (a) ceria slurry and (b) silica slurry.

![img-8.jpeg](images\img-8.jpeg)

Fig. 7. Schematic illustration of a single asperity based on pad texture. (a) Ceria abrasives trapped on a single asperity (the 'Smoothed pad' having a larger contact area and sufficiently high contact pressure). (b) Silica abrasives anchored on a single asperity (the 'Smoothed pad' having a larger contact area and lower contact pressure).

MRR, the high contact force caused by the pad asperities needs to be applied to individual abrasives for the abrasion of the oxide surface. The contact pressure near two interfaces may result in a local force under each abrasive. Thus, asperity contact pressure must also be considered. The height distribution of asperities is not narrow because the pad texture is so rough. Thus, the relative proportion of asperities in low and high pressure has to be determined.

Fig. 6 shows the relative pressure of asperities versus $\varphi$ for each slurry as plotted based on Equation 7. As expressed in Fig. 6(a), most of the asperities transmitted a relatively high contact pressure to the oxide film even under the increased contact area (i.e., 'Smoothed pad'). Among all the asperities, $70.8 \%$ of the asperities transmitted high contact pressure to the film, contrary to the fact that the low contact pressure is dominant as the contact area increases. More importantly, it is reported that the friction force is proportional to the contact area between the film and the abrasive [25]. Therefore, the abrasives were fixed to the wafer surface via the chemical reaction, and the abrasion due to the pad asperities can generate high MRR and friction force with sufficiently high contact pressure. These synergistic effects on the mechanical and chemical factors contribute to the high MRR and friction force.

For silica slurry, a mechanical component such as the contact pressure can dominantly affect the MRR compared to the ceria abrasive [33, 57,58]. To achieve a high MRR in silica CMP, the abrasives enter between the two surfaces and penetrate the hydrated film by the high contact force, and then the surface has to be cut by the rigidly fixed abrasives. In addition, for mechanical abrasion due to contact between the silica abrasive and oxide film, the concentration of the silica slurry should be increased so that there are numerous silica abrasives on the polishing pad. If the concentration of silica is lowered similarly to the ceria, the contact pressure increases according to equation (7), but the contact probability between the oxide film and the silica abrasive decreases, and the RR also decreases.

As shown in Fig. 6(b), since the silica slurry was used in very high concentrations and the pad had a very low plasticity index, the asperity contact pressure was only supported by a large number of slurry
abrasives, unlike the ceria. That is, all the asperities transmit low contact force to the individual abrasives. When the pad texture was smoothed, the tall asperities were also flattened, so that $R_{a}$ increased and $\sigma$ decreased together. Equation (9) indicates that as the value of $R_{a} / \sigma$ increased, $A_{\text {rad }}$ increased, and then the number of abrasives between the pad and the wafer surface increased, as indicated above. Thus, this may result in force distribution over many abrasives for silica CMP, delivering lower contact force to each slurry abrasive.

Fig. 5(b) shows that the MRR decreased by about $59 \%$ in the 'Smoothed pad'. This means that the silica abrasives supported by the pad asperity could penetrate the hydrated film very little, resulting in a reduced MRR with a low friction force. Therefore, increasing the asperity contact pressure by controlling $R_{a} / \sigma$ (i.e., rough pad conditioning) is expected to achieve a high MRR for silica slurry abrasives.

To understand the abrasion mechanism of each slurry abrasive, a schematic illustration of a single asperity along with the pad texture is shown in Fig. 7.

### 4.3. Tribological approach to abrasion behavior based on groove up-

feature

To understand the abrasion mechanism of the slurry abrasives between the pad and the wafer during the CMP, a tribological approach should be carried out with an abrasive wear model. The Stribeck curve is a well-presented plot using CoF vs. the Hersey number, which is a dimensionless grouping parameter [59]. Here, the Hersey number can be expressed as follows:
Hersey number $=\frac{\mu \mathrm{V}}{\mathrm{P}^{\prime}}, \quad \mathrm{P}^{\prime}=\frac{\mathrm{P}}{\chi}$
Where $\mu$ is the viscosity of the slurry, V is the relative velocity of the pad-wafer, and $P^{\prime}$ is the applied pressure with a correction factor, $\chi$. Since each pad groove has different sized surface areas, a different pressure can be applied to the wafer surface even under the same downforce. For this, a dimensionless variable $\chi$, is added to express the

![img-9.jpeg](images\img-9.jpeg)

Fig. 8. The Stribeck curve based on the Hersey Number with a correction factor.
actual pressure.
Once the Stribeck curve is plotted with CoF values as a function of the Hersey number, the contact mode between the two interfaces and the abrasives can be predicted, as in Fig. 8. According to Ludema's definition, three contact modes were proposed [60]: boundary lubrication, partial lubrication, and hydrodynamic lubrication. The first mode of the Stribeck curve is known as boundary lubrication, and result in
direct contact between two interfaces. In the CMP process, slurry abrasives can be penetrated by the contact pressure from the pad asperity or strongly fixed to the wafer-thin film due to the strong adhesion. Thus, the abrasives can cause two-body abrasion between the mating surface [61,62], as shown in Fig. 9(a). The second contact mode is referred to as partial lubrication, which is the intermediate value of the Hersey number. This means that the wafer surface cannot be sufficiently penetrated or fixed by the abrasives. As a result, the abrasives can move freely between the contacting bodies [61,62], and three-body abrasion may occur between the pad-wafer interface and the abrasive, Fig. 9(b). Thus, the CoF value decreases and undergoes a transition from boundary lubrication to partial lubrication. Finally, the hydrodynamic lubrication occurs at a relatively large Hersey number and there is almost no contact between the pad and the wafer surface. In typical CMP, a hydrodynamic situation is not more likely to happen due to the pad roughness [63].

During the CMP process, the pad groove can prevent hydroplaning mode [64]. Contrary to the bearing system that consists of the closed-loop, the CMP process has an open system, continuously feeding and discharging the slurry through the pad groove. Furthermore, since the slurry abrasive has an extremely low Stokes number, the abrasives must follow the fluid streamline caused by the slurry flow of the pad groove [65]. Therefore, it can be assumed that the fluid layer no longer develops and can only have an effect on the abrasive transport on the asperities.

Typically, The Stribeck curves are expressed as log-log plots. However, observation of the curves on a linear scale can better represent the data trends [66]. Fig. 10 shows The Stribeck curves of ceria and silica abrasives based on groove up-feature. During the polishing test of the ceria abrasive, the contact mode may correspond to boundary lubrication because the CoF is almost constant and/or increasing a little, Fig. 10 (a). This also indicates that the lubrication state of the ceria in the
![img-10.jpeg](images\img-10.jpeg)

Fig. 9. Abrasive wear process. (a) Two-body abrasion and (b) three-body abrasion.
![img-11.jpeg](images\img-11.jpeg)

Fig. 10. The Stribeck curves with respect to pad up-features of (a) ceria slurry and (b) silica slurry.

![img-12.jpeg](images\img-12.jpeg)

Fig. 11. Removal rate and friction force of (a) ceria slurry and (b) silica slurry from Pad 1 to Pad 3.
'Smoothed pad' may belong to the boundary lubrication because of the increase of friction force even if the pad asperities were totally flat, Fig. 5 (a). Thus, the behavior of ceria abrasives can occur based on two-body abrasion, Fig. 9(a). In other words, ceria abrasives were well attached to the thin film due to both the strong chemical bonding of $\mathrm{Ce}-\mathrm{O}-\mathrm{Si}$ and the relatively high contact pressure.

However, the silica abrasives show different behavior compared to the ceria abrasives. The contact mode of the silica may move from the boundary lubrication to the partial lubrication with the decrease of CoF, Fig. 10(b). That is, three-body abrasion may be dominant for silica abrasives if the contact area is wider, Fig. 9(b).

Fig. 11(a) shows the MRR and friction force of the ceria abrasive based on groove up-features. As for the groove up-feature test, the MRR
increased as the contact area increased (from Pad 1 to Pad 3), just like for the 'Smoothed pad' as seen Fig. 5(a). This may be because the ceria abrasives attached to the oxide film were removed by the high contact pressure and friction force caused by the pad asperities, showing twobody abrasion for the ceria abrasive.

For the silica abrasive, the contact pressure by asperities is much more critical in terms of the penetration of abrasives, and the contact pressure is only supported by the abrasives as indicated above. If the contact area increases from Pad 1 to Pad 3, the number of abrasives on the asperity also increases and may result in the distribution of loads on the abrasives. As a result, abrasive rolling motion can occur along with the decrease of the friction force [67], and the MRR also decreased, Fig. 11(b).

Although silica abrasives behave based on three-body abrasion as the contact area increases, ceria abrasives may behave based on two-body abrasion because the CoF does not decrease even when the contact area increases. In tribology, the MRR of three-body motion can be an order of magnitude lower than that of two-body motion because most of the abrasives roll at the interface [61,68-70]. As a result, the reason why ceria abrasives have a higher RR than silica abrasives can be explained in terms of tribology.

## 5. Conclusion

Based on tribological approaches, we investigated the abrasion behavior according to the two types of slurry abrasives in the oxide CMP process. Focusing on the pad texture defined as "asperities", we confirmed that the contact state between the wafer film and the pad asperity can affect the MRR performance. To validate the oxide removal caused by abrasives, the relative contact pressure among all the asperities was calculated using a contact mechanics model. The results showed that the ceria abrasive can be supported by relatively a high asperity pressure even under the wider contact area. More importantly, the most efficient way to increase the chemically active ceria abrasives rich in $\mathrm{Ce}^{3+}$ is to increase the real contact area by changing the pad topography. As a result, synergetic action of the physico-chemical effects which are both the chemical boding of $\mathrm{Ce}-\mathrm{O}-\mathrm{Si}$ and the relatively high contact pressure can result in the high MRR and friction force. However, the low contact pressure for silica abrasives may be dominant due to the high abrasive concentration.

Mechanical abrasion of ceria abrasives on the oxide surface is expected to be two-body abrasion. On the other hand, the transition from two-body to three-body abrasion can occur for the silica-based abrasive as the contact area increases. Thus, for ceria slurries, the strong chemical bonding, the mechanical pressure, and the abrasion behavior based on two body motion may result in the high MRR and friction force. However, for silica slurries, the low contact pressure can be dominant. Furthermore, as the contact area increases, the three-body rolling motion may generate a low MRR and friction force for small penetrations of abrasives.

As a result, the oxide CMP process using ceria slurry abrasives may be the better choice for smoothing pad texture (i.e., creating a relatively wider contact area). For silica abrasives with high concentration, making the pad texture rough (i.e., creating a relatively narrow contact area) can improve the MRR. The contact area can be controlled using an appropriate pad conditioner. Finally, the analysis in our study can improve the performance of oxide CMP and optimize the combination of consumables.

## CRediT authorship contribution statement

Sanghuck Jeon: Conceptualization, Formal analysis, Investigation, Writing - original draft, Visualization. Jungryul Lee: Conceptualization, Formal analysis, Investigation, Writing - original draft, Visualization. Seokjun Hong: Resources, Writing - review \& editing. Hyeonmin Seo: Data curation, Investigation. Yeongkwang Cho: Data curation, Investigation. Pengzhan Liu: Visualization, Writing - review \& editing. Kihong Park: Conceptualization. Taesung Kim: Supervision, Writing review \& editing.

## Declaration of competing interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

## Acknowledgements

This work was supported by the Technology Innovation Program (or

Industrial Strategic Technology Development Program-the Technology Innovation Program) (20010754, Development of high efficiency CMP Pad materials and commercialization technology on 7 nm semiconductor) funded By the Ministry of Trade, Industry \& Energy (MOTIE, Korea).

## References

[1] Z. Zhang, et al., Changes in surface layer of silicon wafers from diamond scratching, Crip Annals 64 (1) (2015) 349-352,
[2] Z. Zhang, et al., A novel approach of high speed scratching on silicon wafers at nanoscale depths of cut, Sci. Rep. 5 (1) (2015) 1-9,
[3] Z. Zhang, et al., A novel approach of mechanical chemical grinding, J. Alloys Compd. 726 (2017) 514-524,
[4] B. Wang, et al., New deformation-induced nanostructure in silicon, Nano Lett. 18 (7) (2018) 4611-4617,
[5] W. Xie, et al., Green chemical mechanical polishing of sapphire wafers using a novel slurry, Nanoscale 12 (44) (2020) 22518-22526,
[6] Z. Zhang, et al., Environment friendly chemical mechanical polishing of copper, Appl. Surf. Sci. 467 (2019) 5-11,
[7] Z. Zhang, et al., A novel approach of chemical mechanical polishing for a titanium alloy using an environment-friendly slurry, Appl. Surf. Sci. 427 (2018) 409-415,
[8] Z. Zhang, et al., Development of a novel chemical mechanical polishing slurry and its polishing mechanisms on a nickel alloy, Appl. Surf. Sci. 506 (2020) 144670,
[9] L. Liao, et al., A novel slurry for chemical mechanical polishing of single crystal diamond, Appl. Surf. Sci. (2021) 150431,
[10] Z. Zhang, et al., Chemical mechanical polishing for sapphire wafers using a developed slurry, J. Manuf. Process. 62 (2021) 762-771,
[11] S. Hong, et al., A numerical study on slurry flow with CMP pad grooves, Microelectron. Eng. 234 (2020) 111437,
[12] A.J. Khanna, et al., Engineering surface texture of pads for improving CMP performance of soft-10 nm nodes, ECS Journal of Solid State Science and Technology 9 (10) (2020) 104003,
[13] G. Pu, et al., A plasticity-based model of material removal in chemical-mechanical polishing (CMP), IEEE Trans. Semiconal. Manuf. 14 (4) (2001) 406-417,
[14] Y. Zhao, L. Chang, S. Kim, A mathematical model for chemical-mechanical polishing based on formation and removal of weakly bonded molecular species, Wear 254 (3-4) (2003) 332-339,
[15] C.L. Elmufil, G.P. Muldooney, A novel optical technique to measure pad-wafer contact area in chemical mechanical planarization, MRS Online Proceedings Library Archive, 2006, p. 914,
[16] C.L. Elmufil, G.P. Muldooney, The impact of diamond conditioning on surface contact in CMP pads, MRS Online Proceedings Library (OPL), 2007, p. 991,
[17] T.-K. Yu, C. Yu, M. Orlowski, Combined asperity contact and fluid flow model for chemical-mechanical polishing, in: Proceedings of International Workshop on Numerical Modeling of Processes and Devices for Integrated Circuits: NUPAD V, IEEE, 1994,
[18] D. Wang, et al., Von mises stress in chemical-mechanical polishing processes, J. Electrochem. Soc. 144 (3) (1997) 1121,
[19] F. Preston, The theory and design of plate glass polishing machines, Journal of Glass Technology 11 (44) (1927) 214-256,
[20] K. Qin, B. Moudgil, C.-W. Park, A chemical mechanical polishing model incorporating both the chemical and mechanical effects, Thin Solid Films 446 (2) (2004) 277-286,
[21] S. Kim, N. Saka, J.-H. Chun, The role of pad topography in chemical-mechanical polishing, IEEE Trans. Semiconal. Manuf. 27 (3) (2014) 431-442,
[22] Y. Zhao, L. Chang, A micro-contact and wear model for chemical-mechanical polishing of silicon wafers, Wear 252 (3-4) (2002) 220-226,
[23] J. Luo, D.A. Dornfeld, Material removal mechanism in chemical mechanical polishing: theory and modeling, IEEE Trans. Semiconal. Manuf. 14 (2) (2001) 112-133,
[24] M. Tomozawa, Oxide CMP mechanisms, Solid State Technol. 40 (7) (1997) 169-173,
[25] L.M. Cook, Chemical processes in glass polishing, J. Non-Cryst. Solids 120 (1-3) (1990) 152-171,
[26] M.L. White, L. Jones, R. Romine, The mechanism of low pH colloidal silica-based oxide slurries, MRS Online Proceedings Library Archive, 2010, p. 1249,
[27] P.V. Dandu, R. Porrhalu, S. Babu, Role of different additives on silicon dioxide film removal rate during chemical mechanical polishing using ceria-based dispersions, J. Electrochem. Soc. 157 (9) (2010) H869,
[28] J. Seo, et al., Role of the oxidation state of cerium on the ceria surfaces for silicate adsorption, Appl. Surf. Sci. 389 (2016) 311-315,
[29] K. Kim, D.K. Yi, U. Paik, Increase in $\mathrm{Ce} 3+$ concentration of ceria nanoparticles for high removal rate of SiO2 in chemical mechanical planarization, ECS Journal of Solid State Science and Technology 6 (9) (2017) P681,
[30] K.K. Myong, et al., Direct and quantitative study of ceria-SiO2 interaction depending on $\mathrm{Ce} 3+$ concentration for chemical mechanical planarization (CMP) cleaning, Mater. Sci. Semiconal. Process. 122 (2021) 105500,
[31] J. Seo, et al., Role of the surface chemistry of ceria surfaces on silicate adsorption, ACS Appl. Mater. Interfaces 6 (10) (2014) 7388-7394,
[32] R. Manivannan, S. Ramanathan, The effect of hydrogen peroxide on polishing removal rate in CMP with various abrasives, Appl. Surf. Sci. 255 (6) (2009) 3764-3768.

[33] X. Liao, et al., Effect of pad surface micro-texture on removal rate during interlayer dielectric chemical mechanical planarization process, Jpn. J. Appl. Phys. 52 (1R) (2012), 018001.
[34] H. Jeong, et al., Prediction of real contact area from microtopography on CMP pad, Journal of Advanced Mechanical Design, Systems, and Manufacturing 6 (1) (2012) $113-120$.
[35] N. Kenchappa, et al., Soft chemical mechanical polishing pad for oxide CMP applications, ECS Journal of Solid State Science and Technology 10 (1) (2021), 014008
[36] A.J. Khanna, et al., Investigation of the impact of pad surface texture from different pad conditioners on the CMP performance, ECS Journal of Solid State Science and Technology 9 (6) (2020), 064011.
[37] A.J. Khanna, et al., Impact of pad material properties on CMP performance for sub10 nm technologies, ECS Journal of Solid State Science and Technology 8 (5) (2019) P3063.
[38] J.A. Greenwood, J.P. Williamson, Contact of nominally flat surfaces, Proc. Roy. Soc. Lond. Math. Phys. Sci. 295 (1442) (1966) 300-319.
[39] S. Kim, Micro-scale Scratching by Soft Pad Asperities in Chemical-Mechanical Polishing, Massachusetts Institute of Technology, 2013.
[40] Y. Zhao, D.M. Maietta, L. Chang, An asperity microcontact model incorporating the transition from elastic deformation to fully plastic flow, J. Tribol. 122 (1) (2000) 86-93.
[41] K.L. Johnson, K.L. Johnson, Contact Mechanics, Cambridge university press, 1987.
[42] B. Vasilev, et al., Pad roughness evolution during break-in and its abrasion due to the pad-wafer contact in oxide CMP, Microelectron. Eng. 111 (2013) 21-28.
[43] J. McAllister, et al., Effect of conditioner type and downforce, and pad break-in time, on pad surface micro-texture in chemical mechanical planarization, ECS Journal of Solid State Science and Technology 7 (11) (2018) P677.
[44] S. Kim, N. Saka, J.-H. Chun, The effect of pad-asperity curvature on material removal rate in chemical-mechanical polishing, Procedia City 14 (2014) 42-47.
[45] A. Philiponian, S. Olsen, Fundamental tribological and removal rate studies of inter-layer dielectric chemical mechanical planarization, Jpn. J. Appl. Phys. 42 (10R) (2003) 6371.
[46] S. Kim, N. Saka, J.-H. Chun, Pad scratching in chemical-mechanical polishing: the effects of mechanical and tribological properties, ECS Journal of Solid State Science and Technology 3 (5) (2014) P169.
[47] B. Park, et al., Pad roughness variation and its effect on material removal profile in ceria-based CMP slurry, J. Mater. Process. Technol. 203 (1-3) (2008) 287-292.
[48] K. Park, et al., Effects of pad properties on material removal in chemical mechanical polishing, J. Mater. Process. Technol. 187 (2007) 73-76.
[49] J. McGrath, C. Davis, Polishing pad surface characterisation in chemical mechanical planarisation, J. Mater. Process. Technol. 153 (2004) 666-673.
[50] C. Stuffle, et al., Effect of CVD-coated diamond discs on pad surface micro-texture and polish performance in copper CMP, ECS Journal of Solid State Science and Technology 7 (2) (2018) P9.
[51] M. Yoshida, et al., Effect of pad surface roughness on SiO 2 removal rate in chemical mechanical polishing with ceria slurry, Jpn. J. Appl. Phys. 45 (2R) (2006) 733.
[52] S. Han, et al., Effect of pad surface roughness on material removal rate in chemical mechanical polishing using ultrafine colloidal ceria slurry, Electronic Materials Letters 9 (2) (2013) 155-159.
[53] W.-T. Tseng, et al., Post cleaning for FEOL CMP with silica and ceria slurries, ECS Journal of Solid State Science and Technology 6 (10) (2017) P718.
[54] L. Wang, et al., Geria concentration effect on chemical mechanical polishing of optical glass, Appl. Surf. Sci. 253 (11) (2007) 4951-4954.
[55] R. Han, et al., Effect of various slurry injection system configurations on removal rates of silicon dioxide using a ceria-based chemical mechanical planarization slurry, ECS Journal of Solid State Science and Technology 6 (7) (2017) P449.
[56] T. Hoshino, et al., Mechanism of polishing of SiO 2 films by CeO 2 particles, J. NonCryst. Solids 283 (1-3) (2001) 129-136.
[57] T. Sun, et al., Investigating effect of conditioner aggressiveness on removal rate during interlayer dielectric chemical mechanical planarization through confocal microscopy and dual emission ultraviolet-enhanced fluorescence imaging, Jpn. J. Appl. Phys. 49 (2R) (2010), 026501.
[58] K. Hwang, et al., Investigations of the pad trajectory effect on the asymmetric profile and arc-shaped scratches in chemical mechanical polishing, ECS Journal of Solid State Science and Technology 10 (7) (2021). 074005.
[59] B. Mullany, G. Byrne, The effect of slurry viscosity on chemical-mechanical polishing of silicon wafers, J. Mater. Process. Technol. 132 (1-3) (2003) 28-34.
[60] K.C. Ludema, L. Ajayi, Friction, Wear, Lubrication: a Textbook in Tribology, CRC press, 2018.
[61] K.-H. Zum Galn, Wear by hard particles, Tribol. Int. 31 (10) (1998) 587-596.
[62] M. Kandeva-Ivanova, A. Vencl, D. Karanoyanov, Advanced Tribological Costings for Heavy-Duty Applications: Case Studies, Bulgarian Academy of Sciences, Institute of Information and Communication, 2016.
[63] H.J. Kim, et al., Pad surface characterization and its effect on the tribological state in chemical mechanical polishing. Key Engineering Materials, Trans Tech Publ, 2004.
[64] W.-L. Zhu, S.B. Achour, A. Beaucamp, Centrifugal and hydroplaning phenomena in high-speed polishing, CIEP annals 68 (1) (2019) 369-372.
[65] Y. Mu, et al., Effect of pad groove width on slurry mean residence time and slurry utilization efficiency in CMP, Microelectron. Eng. 157 (2016) 60-63.
[66] J.C. Mariscal, et al., Tribological, thermal and kinetic characterization of SiO 2 and Si3N4 polishing for STI CMP on blanket and patterned wafers, ECS Journal of Solid State Science and Technology 9 (4) (2020), 044008.
[67] W. Choi, et al., Effects of slurry particles on silicon dioxide CMP, J. Electrochem. Soc. 151 (8) (2004) 0512.
[68] E. Rabinowicz, L. Dunn, P. Russell, A study of abrasive wear under three-body conditions, Wear 4 (5) (1961) 345-355.
[69] L. Fang, et al., Movement patterns of abrasive particles in three-body abrasion, Wear 162 (1993) 782-789.
[70] Y. Xie, B. Bhushan, Effects of particle size, polishing pad and contact pressure in free abrasive polishing, Wear 200 (1-2) (1996) 281-295.

