"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import { LogoIcon } from "@/components/icons/LogoIcon";
import { Button } from "@/components/ui/button";
import { Sheet, SheetContent, SheetTrigger } from "@/components/ui/sheet";
import { Menu } from "lucide-react";
import clsx from "clsx";

export function AppHeader() {
    const pathname = usePathname();

    const navItems = [
        { href: "/dashboard", label: "Dashboard" },
        { href: "/economic-indicators", label: "Economic Indicators" },
    ];

    return (
        <header className="sticky top-0 z-50 w-full border-b bg-card shadow-sm">
            <div className="container mx-auto flex h-16 items-center justify-between px-4 sm:px-6 lg:px-8">
                <Link href="/dashboard" className="flex items-center gap-2">
                    <LogoIcon className="h-7 w-7 text-primary" />
                    <span className="text-xl font-semibold text-primary font-headline">
            Sales Prophet
          </span>
                </Link>

                {/* Desktop */}
                <nav className="hidden md:flex items-center space-x-2">
                    {navItems.map((item) => {
                        const active = pathname === item.href;
                        return (
                            <Link key={item.href} href={item.href}>
                                <Button
                                    variant="ghost"
                                    className={clsx(
                                        "transition-all",
                                        active
                                            ? "bg-primary/10 text-primary"
                                            : "text-muted-foreground hover:bg-primary/5 hover:text-primary"
                                    )}
                                >
                                    {item.label}
                                </Button>
                            </Link>
                        );
                    })}
                </nav>

                {/* Mobile */}
                <div className="md:hidden">
                    <Sheet>
                        <SheetTrigger asChild>
                            <Button variant="outline" size="icon">
                                <Menu className="h-6 w-6" />
                            </Button>
                        </SheetTrigger>

                        <SheetContent side="right">
                            <nav className="flex flex-col space-y-3 mt-8">
                                {navItems.map((item) => {
                                    const active = pathname === item.href;
                                    return (
                                        <Link key={item.href} href={item.href}>
                                            <Button
                                                variant="ghost"
                                                className={clsx(
                                                    "w-full justify-start text-lg",
                                                    active
                                                        ? "bg-primary/10 text-primary"
                                                        : "hover:bg-primary/5 hover:text-primary"
                                                )}
                                            >
                                                {item.label}
                                            </Button>
                                        </Link>
                                    );
                                })}
                            </nav>
                        </SheetContent>
                    </Sheet>
                </div>
            </div>
        </header>
    );
}
