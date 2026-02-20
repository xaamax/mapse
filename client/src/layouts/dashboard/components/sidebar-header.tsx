import { MapPin } from "lucide-react";
import Text from "@/components/commons/text";
import useUserPreference from "@/core/stores/user-preference";
import clsx from "clsx";

function SidebarHeader() {
  const { sidebarCollapsed } = useUserPreference();

  return (
    <div
      className={clsx(
        "flex items-center gap-2 my-3",
        sidebarCollapsed && "justify-center"
      )}
    >
      <div
        className={clsx(
          "h-8 w-8 ml-[5px] flex items-center justify-center rounded-full bg-primary font-semibold text-primary-foreground"
        )}
      >
        <MapPin className="h-4 w-4 text-primary-foreground transition-all group-hover:scale-110" />
      </div>

      {!sidebarCollapsed && (
        <div className="flex flex-col h-[30px] flex-1 overflow-hidden">
          <Text size="lg">MAPSE</Text>                         
        </div>
      )}
    </div>
  );
}

export default SidebarHeader;
