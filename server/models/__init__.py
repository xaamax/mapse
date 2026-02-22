from models.dre import Dre
from models.ue import Ue
from models.projeto_social import ProjetoSocial, ProjetoSocialEscolar
from models.usuario import Usuario
from models.categoria import Categoria
from models.publico_alvo import PublicoAlvo

# Schemas / DTOs re-export (moved from server/schemas)
from models.dre import (
	DreCompact,
	DreListPaginated,
	DreSchema,
	DrePartial,
	DrePublic,
)
from models.ue import (
	UeCompact,
	UeListPaginated,
	UeSchema,
	UePartial,
	UePublic,
)
from models.projeto_social import (
	ProjetoSocialListPaginated,
	ProjetoSocialSchema,
	ProjetoSocialPartial,
	ProjetoSocialPublic,
	ProjetoSocialEscolarSchema,
	ProjetoSocialEscolarSave,
	ProjetoSocialEscolarPublic,
	ProjetoSocialEscolarListPaginated,
)
from models.categoria import (
	CategoriaCompact,
	CategoriaListPaginated,
	CategoriaSchema,
	CategoriaPartial,
	CategoriaPublic,
)
from models.publico_alvo import (
	PublicoAlvoCompact,
	PublicoAlvoListPaginated,
	PublicoAlvoSchema,
	PublicoAlvoPartial,
	PublicoAlvoPublic,
)
from models.usuario import (
	UsuarioCreate,
	UsuarioSchema,
	UsuarioPartial,
	UsuarioPublic,
	UsuarioLogin,
	UsuarioListPaginated,
)