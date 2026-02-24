import {
  LayoutDashboard,
  MapPinHouse,
  Plus,
  Building,
  Tag,
  FolderOpen,
  Users,
  CircleGauge,
  FormInput,
} from "lucide-react";

const menus = [
  {
    name: "Dashboard",
    icon: <CircleGauge className="h-[18px] w-[18px]" />,
    route: "/dashboard",
  },
  {
    name: "Cadastros",
    icon: <Plus className="h-[18px] w-[18px]" />,
    route: "cadastros",
    childs: [
      {
        name: "Categorias",
        route: "/cadastros/categorias",
        icon: <Tag className="h-[18px] w-[18px]" />,
      },
      {
        name: "DREs",
        route: "/cadastros/dres",
        icon: <Building className="h-[18px] w-[18px]" />,
      },
      {
        name: "UEs",
        route: "/cadastros/ues",
        icon: <Building className="h-[18px] w-[18px]" />,
      },
      {
        name: "Publicos Alvos",
        route: "/cadastros/publicos-alvos",
        icon: <Users className="h-[18px] w-[18px]" />,
      },
      {
        name: "Formulários",
        route: "/cadastros/formularios",
        icon: <LayoutDashboard className="h-[18px] w-[18px]" />,
      },
    ],
  },
  {
    name: "Projetos Sociais",
    icon: <FolderOpen className="h-[18px] w-[18px]" />,
    route: "/projetos-sociais",
  },
  {
    name: "Projetos Sociais Escolares",
    icon: <MapPinHouse className="h-[18px] w-[18px]" />,
    route: "/projetos-sociais-escolares",
  },
];

export default menus;
