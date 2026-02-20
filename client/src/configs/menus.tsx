import {
  LayoutDashboard,
  Plus,
  House,
  // MapPinHouse,
  Search,
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
  }
];

export default menus;
