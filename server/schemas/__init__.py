from schemas.dre import DreCompact, DreListPaginated, DreSchema, DrePartial, DrePublic
from schemas.ue import (
    UeCompact,
    UeListPaginated, 
    UeSchema, 
    UePartial, 
    UePublic 
)
from schemas.projeto_social import (
	ProjetoSocialListPaginated,
	ProjetoSocialSchema,
	ProjetoSocialPartial,
	ProjetoSocialPublic,
)
from schemas.categoria import (
	CategoriaCompact,
	CategoriaListPaginated,
	CategoriaSchema,
	CategoriaPartial,
	CategoriaPublic,
)
from schemas.publico_alvo import (
    PublicoAlvoCompact,
	PublicoAlvoListPaginated,
	PublicoAlvoSchema,
	PublicoAlvoPartial,
	PublicoAlvoPublic,
)
from schemas.projeto_social_escolar import (
    ProjetoSocialEscolarSave,
	ProjetoSocialEscolarListPaginated,
	ProjetoSocialEscolarSchema,
	ProjetoSocialEscolarPublic,
)
from schemas.usuario import (
    	UsuarioCreate, 
    	UsuarioSchema, 
     	UsuarioPartial, 
      	UsuarioPublic, 
       	UsuarioLogin, 
        UsuarioListPaginated
    )
