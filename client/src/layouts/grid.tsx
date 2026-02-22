import { useEffect, useMemo } from "react";

interface GridProps {
  xs?: number;
  sm?: number;
  md?: number;
  lg?: number;
  className?: string;
  children?: React.ReactNode;
}

const clamp = (v: number) => Math.max(1, Math.min(12, Math.floor(v || 1)));

export default function Grid({
  xs,
  sm,
  md,
  lg,
  className = "",
  children,
}: GridProps) {
  const xsN = clamp(Number(xs ?? 1));
  const smN = clamp(Number(sm ?? xsN));
  const mdN = clamp(Number(md ?? smN));
  const lgN = clamp(Number(lg ?? mdN));

  const dynamicClass = useMemo(
    () => `grid-d-${xsN}-${smN}-${mdN}-${lgN}`,
    [xsN, smN, mdN, lgN],
  );

  useEffect(() => {
    if (typeof document === "undefined") return;

    const styleId = `style-${dynamicClass}`;
    if (document.getElementById(styleId)) return;

    const style = document.createElement("style");
    style.id = styleId;
    style.innerHTML = `
    .${dynamicClass} {
      display: grid;
      gap: 1rem;
      grid-template-columns: repeat(${xsN}, minmax(0, 1fr));
    }
    @media (min-width: 640px) {
      .${dynamicClass} { grid-template-columns: repeat(${smN}, minmax(0, 1fr)); }
    }
    @media (min-width: 768px) {
      .${dynamicClass} { grid-template-columns: repeat(${mdN}, minmax(0, 1fr)); }
    }
    @media (min-width: 1024px) {
      .${dynamicClass} { grid-template-columns: repeat(${lgN}, minmax(0, 1fr)); }
    }
  `;

    document.head.appendChild(style);
  }, [dynamicClass, xsN, smN, mdN, lgN]);

  return <div className={`${dynamicClass} ${className}`}>{children}</div>;
}
