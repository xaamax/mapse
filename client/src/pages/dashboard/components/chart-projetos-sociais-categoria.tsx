import { Bar, BarChart, CartesianGrid, XAxis, YAxis, Cell } from "recharts";
import { useMemo } from "react";

import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";

import {
  ChartConfig,
  ChartContainer,
  ChartTooltip,
  ChartTooltipContent,
  ChartLegend,
  ChartLegendContent,
} from "@/components/ui/chart";

import Text from "@/components/commons/text";

type Props = {
  chartData: {
    label: string;
    total: number;
  }[];
};

const normalizeKey = (value: string) =>
  value
    .normalize("NFD")
    .replace(/[\u0300-\u036f]/g, "")
    .toLowerCase();

const generateColor = (key: string) => {
  let hash = 0;
  for (let i = 0; i < key.length; i++) {
    hash = key.charCodeAt(i) + ((hash << 5) - hash);
  }
  const hue = Math.abs(hash % 360);
  return `hsl(${hue}, 70%, 50%)`;
};

export default function ChartProjetosSociaisCategoria({ chartData }: Props) {
  const normalizedData = useMemo(() => {
    return chartData.map((item) => {
      const key = normalizeKey(item.label);

      return {
        ...item,
        tipoKey: key,
        fill: generateColor(key),
      };
    });
  }, [chartData]);

  const chartConfig = useMemo(() => {
    const cfg: Record<string, { label: string; color: string }> = {};

    normalizedData.forEach((d) => {
      cfg[d.tipoKey] = {
        label: d.label,
        color: d.fill,
      };
    });

    return cfg as ChartConfig;
  }, [normalizedData]);

  return (
    <Card className="h-full">
      <CardHeader>
        <CardTitle>Projetos Sociais por Categoria</CardTitle>
        <CardDescription>
          Total de projetos sociais por categoria
        </CardDescription>
      </CardHeader>

      <CardContent>
        <ChartContainer config={chartConfig} className="mx-auto aspect-square">
          {!normalizedData.length ? (
            <div className="flex h-full w-full items-center justify-center">
              <Text className="text-muted-foreground">
                Nenhum registro encontrado.
              </Text>
            </div>
          ) : (
            <BarChart
              accessibilityLayer
              data={normalizedData}
              margin={{ top: 20, right: 20, left: 0, bottom: 20 }}
            >
              <CartesianGrid vertical={false} />

              <XAxis
                dataKey="label"
                tickLine={false}
                tickMargin={10}
                axisLine={false}
                interval={0}
                height={64}
              />

              <YAxis
                type="number"
                dataKey="total"
                tickLine={false}
                axisLine={false}
                tick={false}
              />

              <ChartTooltip
                cursor={false}
                content={<ChartTooltipContent hideLabel />}
              />

              <Bar dataKey="total" name="tipoKey" radius={6}>
                {normalizedData.map((entry) => (
                  <Cell key={entry.tipoKey} fill={entry.fill} />
                ))}
              </Bar>

              <ChartLegend
                content={<ChartLegendContent nameKey="tipoKey" />}
                className="pt-4 flex-wrap gap-3"
              />
            </BarChart>
          )}
        </ChartContainer>
      </CardContent>
    </Card>
  );
}
