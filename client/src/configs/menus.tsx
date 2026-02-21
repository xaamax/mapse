import {
  LayoutDashboard,
  House,
  MapPinHouse,
} from "lucide-react";

const menus = [
  {
    name: "Dashboard",
    icon: <LayoutDashboard className="h-[18px] w-[18px]" />,
    route: "/dashboard",
  },
  {
    name: "Projetos Sociais",
    icon: <House className="h-[18px] w-[18px]" />,
    route: "/projetos-sociais", 
  },
  {
    name: "Projetos Sociais Escolares",
    icon: <MapPinHouse className="h-[18px] w-[18px]" />,
    route: "/projetos-sociais-escolares", 
  }
];

export default menus;
