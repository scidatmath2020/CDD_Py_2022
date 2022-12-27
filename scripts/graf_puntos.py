# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 13:22:36 2022

@author: hp
"""

import pandas as pd
import numpy as np
from siuba import *
from plotnine import *
import os

os.chdir("C:\\Users\\hp master\\Documents\\SciData\\CDD_Py_2022")

#%%
'''Lectura del archivo'''
cifra_negra = pd.read_csv("cifra_negra.csv",encoding="latin-1")

#%%
cifra_negra = cifra_negra >> mutate(porcentaje = _.cifra_negra*100/_.delitos)

#%%
cifra_negra

#%%

(ggplot() +
     geom_point(data=cifra_negra,
                mapping = aes(x="delitos",y="porcentaje"),
                color = "red"
                )
)



#%%

(ggplot() +
  geom_point(data = cifra_negra,
             mapping = aes(x = "delitos",
                 y="porcentaje",
                 color = "anio.astype('string')"
                            )
             ) 
)

#%%


anio_2021.columns

anio_2021 = cifra_negra >> filter(_.anio == 2021)
anio_2021
#%%

anio_2021 >> mutate(letra = if_else(_.delitos>_.delitos.mean(),1,0))

anio_2021 = anio_2021 >> mutate(letra = np.where(_.Entidad.str.startswith(('C')),1,0))


#%%

(ggplot() +
geom_point(data = anio_2021,
           mapping = aes(x = "delitos",
                         y = "porcentaje",
                         size = "cifra_negra",
                         color = "letra.astype"string")",
                         shape = "zona" 
                         ),
           alpha=0.5)
)

#%%


 +
labs(x="Delitos\ncometidos", 
              y="Cifra\nnegra (%)", 
              title="Porcentaje de cifra negra por entidad" 
              ) +
geom_text(data = anio_2021,
          mapping = aes(label="Entidad",
                        x="delitos",
                        y="porcentaje"),
          va = "top",
          size = 5) 
)

#%%

anio_2021_incompleto = (anio_2021 >>
                        filter(-_.Entidad.isin(["Ciudad de México","Estado de México"]))
                        )

(ggplot() +
geom_point(data = anio_2021_incompleto,
           mapping = aes(x = "delitos",
                         y = "porcentaje",
                         label = "Entidad",
                         #size = "delitos",
                         color = "zona",
                         #shape = "zona" 
                         ),
           alpha=0.5) +
labs(x="Delitos\ncometidos", 
              y="Cifra\nnegra (%)", 
              title="Porcentaje de cifra negra por entidad" 
              ) +
geom_text(data = anio_2021_incompleto,
          mapping = aes(label="Entidad",
                        x="delitos",
                        y="porcentaje",
                        color = "zona"),
          va = "top",
          ha = "left",
          size = 5) 
)