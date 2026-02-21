import React from "react";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";

type Props = {
  title: string;
  actions?: React.ReactNode;
  children: React.ReactNode;
  className?: string;
};

export default function Box({ title, actions, className, children }: Props) {
  return (
    <Card className={`h-full flex flex-col ${className ?? ""}`}>
      <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
        <CardTitle>{title}</CardTitle>
        {actions && <div>{actions}</div>}
      </CardHeader>
      <CardContent className="flex-1">{children}</CardContent>
    </Card>
  );
}
